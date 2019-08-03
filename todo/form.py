from django import forms
from todo.models import Category, Todo


class TodoSearchForm(forms.Form):
    keyword = forms.CharField(max_length = 100, label = u'キーワード')
    include_finished = forms.BooleanField(required = False, label = u'解決したTODOも含める')
    category = forms.ModelChoiceField(Category.objects.all(), required = False, label =u'カテゴリ')

#class TodoForm(forms.ModelForm):
#    class Meta:
#        model = Todo 
