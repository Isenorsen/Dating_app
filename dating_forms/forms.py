from django.forms import ModelForm
from .models import DatingForm

class AddForm(ModelForm):
    
    class Meta:
        model = DatingForm
        fields = ['title', 'text', 'image1', 'image2', 'image3']