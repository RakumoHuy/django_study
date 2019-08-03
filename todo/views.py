from django.shortcuts import render_to_response
from todo.form import TodoSearchForm
from todo.models import Category, Todo

# Create your views here.

def show_categorized_list(request):
    return render_to_response('second_template.html', dict(categories = Category.objects.all()))

def search_todo(request):
    results = None
    if request.GET:
        form = TodoSearchForm(request.GET)
        if form.is_valid():
            cleaned = form.clean()
            queryset = Todo.objects.all()
            category = cleaned['category']
            if category:
                queryset = queryset.filter(category = category)
            include_finished = cleaned.get('include_finished',False)
            if include_finished == False:
                queryset = queryset.filter(is_finished = False)
            key_word = cleaned['keyword']
            queryset = queryset.filter(title__contains = cleaned['keyword'])
            results = queryset
    else:
        form = TodoSearchForm()
    return render_to_response('search_form.html', dict(form = form, results = results))

#def add_todo(request):
#    if request.POST:
#        form = TodoFrom(request.POST)
#        if form.is_valid()
