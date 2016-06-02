from django.conf.urls import url
from . import views

app_name = 'music'

urlpatterns = [

    # /music/
    url(r'^$' , views.IndexView.as_view() , name='index'),


    # /music/783/  or any number maybe
    url(r'^(?P<pk>[0-9]+)/$' , views.DetailView.as_view() , name='detail'),

    # /music/783/favourite/
    url(r'^(?P<album_id>[0-9]+)/favourite/$' , views.favourite , name='favourite'),

    #/music/add_album/
    url(r'^add_album/$',views.AlbumCreate.as_view() ,name='album-add'),

    # /music/update_album/
    url(r'^update_album/$', views.ShowUpdate.as_view(), name='album-update'),

    #/music/update/id/
    url(r'^update_album/(?P<pk>[0-9]+)/$' , views.AlbumUpdate.as_view() , name='album-update-id'),

    # /music/delete_album/
    url(r'^delete_album/$', views.ShowUpdate.as_view(), name='album-delete'),

    # /music/delete/id/
    url(r'^delete_album/(?P<pk>[0-9]+)/$', views.AlbumDelete.as_view(), name='album-delete-id'),

    # /music/registration_form/
    url(r'^register/$', views.UserFormView.as_view(), name='register'),

]

