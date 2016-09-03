from django import forms

from .models import Todo

class Todoform(forms.ModelForm):
	class Meta:
		model = Todo
		fields = ["name","description"]

	def clean_name(self):
		# does nothing
		name = self.cleaned_data.get("name")
		return name

class Markerform(forms.Form):
	number  = forms.IntegerField()
	
	def clean_number(self):
		number = self.cleaned_data.get('number')
		if number <= 0:
			raise forms.ValidationError("Enter a positive integer.")
		elif number > Todo.objects.all().order_by('created')[len(Todo.objects.all())-1].id:
			raise forms.ValidationError("The id is beyond maximum id.")