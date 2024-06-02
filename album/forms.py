from django import forms 

from .models import Album

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'
        
        widgets = {
            'rating': forms.Select(choices=[(i,i) for i in range(1,6)]),
            'album_release_date': forms.NumberInput(attrs={'type':'date'}),

        }