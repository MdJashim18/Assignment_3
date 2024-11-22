from django.shortcuts import render, redirect, get_object_or_404
from album.forms import AlbumForm
from album.models import AlbumModel 

def Album(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Album')
    else:
        form = AlbumForm()
    return render(request, 'album.html', {'form': form})

def Edit_Album(request, id):
    album = get_object_or_404(AlbumModel, pk=id)  
    if request.method == 'POST':
        album_form = AlbumForm(request.POST, instance=album)
        if album_form.is_valid():
            album_form.save()
            return redirect('Album')
    else:
        album_form = AlbumForm(instance=album)
    return render(request, 'album.html', {'form': album_form})

def delete_album(request, id):  
    album = get_object_or_404(AlbumModel, pk=id) 
    album.delete()
    return redirect('Album')
