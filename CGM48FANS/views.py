from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django import forms
from .forms import SignUpForm, SignInForm,UserCreationForm
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

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()  # บันทึกข้อมูลผู้ใช้ใหม่
            messages.success(request, 'บัญชีของคุณได้ถูกสร้างขึ้นแล้ว! คุณสามารถเข้าสู่ระบบได้.')
            return redirect('song_index')  # เปลี่ยนไปยังหน้าหลักในโฟลเดอร์ song
        else:
            messages.error(request, 'กรุณาแก้ไขข้อผิดพลาดด้านล่าง')
            print(form.errors)  # พิมพ์ข้อผิดพลาดในฟอร์ม
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
                return redirect('home')  # เปลี่ยน 'next-page' เป็น URL ของหน้าหลังจากเข้าสู่ระบบ
            else:
                messages.error(request, 'ชื่อผู้ใช้หรือรหัสผ่านไม่ถูกต้อง')
    else:
        form = AuthenticationForm()

    return render(request, 'signin/index.html', {'form': form})
