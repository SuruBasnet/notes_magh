from django.shortcuts import render, redirect
from .models import Note, NoteType
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):
    note_objs = Note.objects.all()
    data = {'notes':note_objs}
    return render(request,'index.html', context=data)

@login_required
def create_note(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        type = request.POST.get('type')

        note_type = NoteType.objects.get(id=type)

        Note.objects.create(title=title,description=description,type=note_type)

    note_type_objs = NoteType.objects.all()
    data = {'note_types':note_type_objs}
    return render(request,'create.html',context=data)

@login_required
def edit_note(request,pk):
    note_obj = Note.objects.get(id=pk)

    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        type = request.POST.get('type')

        note_type_obj = NoteType.objects.get(id=type)

        note_obj.title = title
        note_obj.description = description
        note_obj.type = note_type_obj

        note_obj.save()

    note_type_objs = NoteType.objects.all()
    data = {'note_types':note_type_objs, 'note' : note_obj}
    return render(request,'edit.html',context=data)

@login_required
def delete_note(request,pk):
    note_obj = Note.objects.get(id=pk)
    note_obj.delete()
    return redirect('home')

def register_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        username = request.POST.get('username')

        hash_password = make_password(password)

        User.objects.create(username=username,email=email,password=hash_password)
    return render(request,'register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user != None:
            login(request,user)
            return redirect('home')

    return render(request,'login.html')