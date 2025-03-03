from django import forms 
from core.models import Task

class CreateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = (
            'title', 'description'
        )
        widgets = {
            "title" : forms.TextInput(
                attrs={"class" : "text-field", "max_length":50}),

            "description" : forms.Textarea(
                attrs={"class" : "text-area-field","cols" : 60, "rows":5})
            }
    