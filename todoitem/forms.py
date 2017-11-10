from django import forms
from .models import TodoItem
from .models import EditItem

class TodoItemForm(forms.ModelForm):
    class Meta:
        model = TodoItem
        fields = ("name", "done")

class EditItemForm(forms.ModelForm):
    class Meta:
        model = EditItem
        fields = ("name", "done")
