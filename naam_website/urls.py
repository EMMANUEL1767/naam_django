from django.urls import path
from . import views

urlpatterns = [
    path('', views.buildIndexPage, name='index'),
    path('about-us', views.buildAboutUsPage, name='about-us'),
    path('events', views.buildEventsPage, name='events'),
    path('gallery', views.buildGalleryPage, name='gallery'),
    path('career', views.buildCareerPage, name='career'),
    path('contact-us', views.buildContactUsPage, name='contact-us'),
    path(r'^event_detail/(?P<event_id>\w+\$', views.buildEventDetailPage, name='event-details'),
    path(r'^single_album/(?P<album_identifier>\w+\$', views.buildSingleAlbumPage, name='single-album'),
]