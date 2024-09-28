from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import SignUpForm
from .models import Member2, Album, Single
from django.contrib.auth.decorators import login_required

@login_required(login_url='/signin/')
def page1(request):
    try:
        # Attempt to get all members
        members = Member2.objects.filter(team="Trainee")
    except Member2.DoesNotExist:
        # If no members exist, return an empty list
        members = []
    
    return render(request, 'home/index.html', {'members': members})


@login_required(login_url='/signin/')
def members(request):
    try:
        # Attempt to get all members
        members = Member2.objects.filter(team="Trainee")
    except Member2.DoesNotExist:
        # If no members exist, return an empty list
        members = []
    
    return render(request, 'member/index.html', {'members': members})

# Create your views here.
@login_required(login_url='/signin/')
def song(request):
    try:
        # Attempt to get all members
        members = Member2.objects.filter(team="Trainee")
    except Member2.DoesNotExist:
        # If no members exist, return an empty list
        members = []
    
    return render(request, 'song/index.html', {'members': members})


@login_required(login_url='/signin/')
def song(request):
    import pprint
    albums = Album.objects.prefetch_related('list_songs').all()  # Fetch all albums and their related songs
    singles = Single.objects.prefetch_related('list_songs').all()  # Fetch all singles and their related songs

    context = {
        'albums': albums,
        'singles': singles,
    }
    return render(request, 'song/index.html', context)

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log the user in after signup
            messages.success(request, 'เย้ สร้าง account สำเร็จแล้วน่ะ ไปลุยกันต่อเลยยยยย!')
            return redirect('/')  # Redirect to the homepage or another page after signup
        else:
            messages.error(request, 'เกิดข้อผิดพลาดด ตายแล้วว!!')
    else:
        form = SignUpForm()
    
    return render(request, 'signup/index.html', {'form': form})


def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')  # เปลี่ยน 'next-page' เป็น URL ของหน้าหลังจากเข้าสู่ระบบ
            else:
                messages.error(request, 'ชื่อผู้ใช้หรือรหัสผ่านไม่ถูกต้อง')
    else:
        form = AuthenticationForm()

    return render(request, 'signin/index.html', {'form': form})
