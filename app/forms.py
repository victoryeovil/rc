from django import forms
from .models import GalleryImage, Sermon

class GalleryImageForm(forms.ModelForm):
    class Meta:
        model = GalleryImage
        fields = ['image', 'description']

class SermonForm(forms.ModelForm):
    class Meta:
        model = Sermon
        fields = ['title', 'youtube_link', 'description', 'images']
