from .models import Tareas
from django.forms import ModelForm

class TareasForm(ModelForm):
    class Meta:
        model = Tareas
        fields = '__all__'
