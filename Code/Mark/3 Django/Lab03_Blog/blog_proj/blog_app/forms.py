from django.forms import ModelForm
from .models import BlogPost

class EditForm(ModelForm):
    class Meta:
        model = BlogPost
        exclude = ['date_created','user']