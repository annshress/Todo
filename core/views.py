from django.shortcuts import render
from django.http import Http404
from rest_framework import generics

# Create your views here.

from .models import Todo
from .forms import Todoform, Markerform
from serializers import TodoSerializer

def home(request):
	title = "Home"
	queryset = Todo.objects.all().order_by('created')
	form = Todoform(request.POST or None)
	if form.is_valid():
		instance = form.save(commit = False)
		des = form.cleaned_data.get("description")
		if not des:
			des = "No description!!!"
		instance.description = des
		instance.save()
		title = 'Item Saved'
		# print instance.name, instance.created

	context = {
		'title' : title,
		'queryset' : queryset,
		'form' : form,
		# 'form1' : form1,
	}

	return render(request, 'home.html', context)

def item(request, todo_id):
	title = 'Todo ' + str(todo_id)
	try:
		queryset = Todo.objects.get(id = int(todo_id))
	except:
		raise Http404("Poll does not exist")
	
	context = {
		'title' : title,
		'queryset' : queryset,
		'todo_id' : todo_id,
	}

	return render(request, 'item.html', context)

class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Todo.objects.all()
	serializer_class = TodoSerializer

def delete(request):
	title = "Delete"
	queryset = Todo.objects.all()
	notice = ''

	try:
		del_id = int(request.POST.get('id'))

		if 0 >= del_id or del_id > Todo.objects.all().order_by('created')[len(Todo.objects.all())-1].id:
			notice = "id not found."
		else:
			try:
				Todo.objects.get(id = del_id).delete()
				notice = "Successfully deleted."
			except:
				notice = "id not found."
	except TypeError:
		pass	

	context = {
		'title' : title,
		'queryset' : queryset,
		'notice' : notice,
	}

	return render(request, 'delete.html', context)

def mark(request):
	title = "Mark"
	form = Markerform(request.POST or None)
	notice = ''
	try:
		mark_id = int(request.POST.get('number'))
		item = Todo.objects.get(id = mark_id)
		if item.completed:
			notice = "Already Completed."
		item.save()
	except:
		pass

	context = {
		'title' : title,
		'form' : form,
		'notice' : notice,
	}
	return render(request, 'mark.html', context)