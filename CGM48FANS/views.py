from django.shortcuts import render
from django.http import HttpResponse
from .models import Member2, Album, Single
# Create your views here.
def page1(request):
    try:
        # Attempt to get all members
        members = Member2.objects.filter(team="Trainee")
    except Member2.DoesNotExist:
        # If no members exist, return an empty list
        members = []
    
    return render(request, 'home/index.html', {'members': members})

# Create your views here.
def members(request):
    try:
        # Attempt to get all members
        members = Member2.objects.filter(team="Trainee")
    except Member2.DoesNotExist:
        # If no members exist, return an empty list
        members = []
    
    return render(request, 'member/index.html', {'members': members})

# Create your views here.
def song(request):
    try:
        # Attempt to get all members
        members = Member2.objects.filter(team="Trainee")
    except Member2.DoesNotExist:
        # If no members exist, return an empty list
        members = []
    
    return render(request, 'song/index.html', {'members': members})



def song(request):
    import pprint
    albums = Album.objects.prefetch_related('list_songs').all()  # Fetch all albums and their related songs
    singles = Single.objects.prefetch_related('list_songs').all()  # Fetch all singles and their related songs

    context = {
        'albums': albums,
        'singles': singles,
    }
    return render(request, 'song/index.html', context)
