from django.forms import ModelForm, modelformset_factory
from .models import *

class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ['name','description']

TodoFormSet = modelformset_factory(
    Todo, form=TodoForm, extra=1
)

