from django.shortcuts import render, redirect, get_object_or_404
from .models import TodoItem
from .models import EditItem
from .forms import TodoItemForm
from .forms import EditItemForm

# Create your views here.
def get_index(request):
    results = TodoItem.objects.all()
    return render(request, "index.html", {'items': results})
    
def add_item(request):
    if request.method == "POST":
        form = TodoItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(get_index)
    else:
        form = TodoItemForm()    
    
    return render(request, "item_form.html", { 'form': form })
    
    
def edit_item(request, id):
    
   item = get_object_or_404 (TodoItem, pk = id)
    
   if request.method == "POST":
        form = TodoItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect(get_index)
        
       
   else:
        form = TodoItemForm(instance=item)
        
       
   return render(request, "item_form.html", { 'form': form })