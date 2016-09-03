from django.contrib import admin

# Register your models here.
from .models import Todo
from .views import Todoform

class TodoAdmin(admin.ModelAdmin):
	list_display = ["__unicode__","description","created","completed"]
	# form = Todoform
	class Meta():
		model = Todo

admin.site.register(Todo, TodoAdmin)