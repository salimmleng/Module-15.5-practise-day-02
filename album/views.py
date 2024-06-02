from django.shortcuts import render,redirect
from .forms import AlbumForm
from .models import Album
# Create your views here.
def add_album(request):
    if request.method == 'POST':
        albumForm = AlbumForm(request.POST)
        if albumForm.is_valid():
            albumForm.save()
            return redirect('home')
            
    else:
        albumForm = AlbumForm()

    return render(request,'album.html',{'form':albumForm})


def edit_album(request,id):
    album = Album.objects.get(pk = id)
    albumForm = AlbumForm(instance = album)
    if request.method == 'POST':
        albumForm = AlbumForm(request.POST,instance = album)
        if albumForm.is_valid():
            albumForm.save()
            return redirect('home')
            

    return render(request,'edit_album.html',{'form':albumForm})


