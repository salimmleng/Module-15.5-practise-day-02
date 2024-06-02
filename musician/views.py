from django.shortcuts import render,redirect
from .forms import MusicianForm
from .models import Musician
# Create your views here.
def add_musician(request):
    if request.method == 'POST':
        musicForm = MusicianForm(request.POST)
        if musicForm.is_valid():
            musicForm.save()
            return redirect('home')
            
    else:
        musicForm = MusicianForm()

    return render(request,'music.html',{'form':musicForm})


def edit_music(request,id):
    print(id)
    music = Musician.objects.get(pk=id)
    musicForm = MusicianForm(instance = music)
    if request.method == 'POST':
        musicForm = MusicianForm(request.POST,instance = music)
        if musicForm.is_valid():
            musicForm.save()
            return redirect('home')

   

    return render(request,'edit.html',{'form': musicForm})

def delete_music(request,id):
    music = Musician.objects.get(pk=id)
    music.delete()
    return redirect('home')