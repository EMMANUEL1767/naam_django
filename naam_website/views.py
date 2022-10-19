from django.shortcuts import render
from .models import *
from django.http import JsonResponse, HttpResponse


def buildIndexPage(request):
    context = {
        'current_screen': 'index'
    }
    return render(request, "index.html", context)


def buildAboutUsPage(request):
    context = {
        'current_screen': 'about-us'
    }
    return render(request, "about_us.html", context)


def buildEventsPage(request):
    context = {
        'current_screen': 'events'
    }
    return render(request, "events.html", context)


def buildGalleryPage(request):
    context = {
        'current_screen': 'gallery'
    }
    return render(request, "gallery.html", context)


def buildCareerPage(request):
    context = {
        'current_screen': 'career'
    }
    return render(request, "career.html", context)


def buildContactUsPage(request):
    context = {
        'current_screen': 'contact-us'
    }
    return render(request, "contact_us.html", context)


def buildEventDetailPage(request, event_id):
    context = {
        'current_screen': 'events'
    }
    return render(request, "event_detail.html", context)


def buildSingleAlbumPage(request, album_identifier):
    context = {
        'current_screen': 'gallery'
    }
    return render(request, "single_album.html", context)
