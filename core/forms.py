from django import forms 
from core.models import Task
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


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
    

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            "username","first_name", "email", "password1", "password2"
        )
        widgets = {
            "username": forms.TextInput(
                attrs={
                    'placeholder': "username",
                    'class': 'field-register-input'
                }
            ),
            "first_name": forms.TextInput(
                attrs={
                    'placeholder': "name",
                    'class': 'field-register-input'
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    'placeholder': "email",
                    'class': 'field-register-input'
                }
            )
        }
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)

        # Adiciona atributos personalizados aos campos de senha
        self.fields['password1'].widget.attrs.update({
            'placeholder': 'password',
            'class': 'field-register-input'
        })
        self.fields['password2'].widget.attrs.update({
            'placeholder': 'confirm password',
            'class': 'field-register-input'
        })


