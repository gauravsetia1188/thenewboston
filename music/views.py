from django.http import HttpResponse
from .models import Album, Song
from django.http import Http404
from django.template import loader
from django.shortcuts import render,get_object_or_404,redirect
from django.views import generic
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import authenticate,login,logout
from . forms import UserForm
from django.views.generic import View

'''def index(request):
    all_albums = Album.objects.all()
   # template = loader.get_template('music/index.html')
    context = {
        'all_albums' : all_albums,
    }
    return render(request ,'music/index.html' , context )
  #  return HttpResponse(template.render(context , request))
'''
'''def detail(request, album_id):

  album = get_object_or_404( Album , id=album_id)
  template = loader.get_template('music/detail.html')
  context = {
      'album': album,
  }
  return HttpResponse(template.render(context , request)) '''
""" try :
    album = Album.objects.get(id=album_id)
    except :
    raise Http404(' ERROR 404 PAGE DOESNOT EXIST') """

class ShowUpdate(generic.ListView):
    template_name = 'music/album-update.html'
    context_object_name = 'all_albums'

    def get_queryset(self):
        return Album.objects.all()



class IndexView(generic.ListView):

    template_name = 'music/index.html'
    context_object_name = 'all_albums'
    def get_queryset(self):
        return Album.objects.all()

class DetailView(generic.DetailView):

    model = Album
    template_name = 'music/detail.html'


def favourite(request,album_id):
    album = get_object_or_404( Album , id=album_id)
    try:
        selected_song = album.song_set.get(pk=request.POST['song'])

    except:
        return render(request, 'music/detail.html',{
            'album': album,
            'error_message': 'Invalid Choice - Please make a valid one'
        })

    selected_song.is_favourite = True
    selected_song.save()
    context = {
        'album': album,
    }
    return render(request,'music/detail.html',context)

class AlbumCreate(CreateView):
    model = Album
    fields = ['artist','album_title','genre','album_logo']

class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist','album_title','genre','album_logo']

class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('music:index')


class UserFormView(View):
   form_class = UserForm
   template_name = 'music/registration_form.html'

   def get(self,request):
       form = self.form_class(None)
       return render(request , self.template_name , {'form':form})

   def post(self,request):
       form = self.form_class(request.POST)

       if form.is_valid():
           user = form.save(commit=False)
           username = form.cleaned_data['username']
           password = form.cleaned_data['password']
           user.set_password(password)
           user.save()

           user = authenticate(username=username, password=password)

           if user is not None:
               login(request,user)
               return redirect('music:index')

       return render(request , self.template_name , {'form':form} )



