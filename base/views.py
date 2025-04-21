from django.shortcuts import render, redirect
from .models import Note, NoteType

# Create your views here.
def home(request):
    note_objs = Note.objects.all()
    data = {'notes':note_objs}
    return render(request,'index.html', context=data)

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

def delete_note(request,pk):
    note_obj = Note.objects.get(id=pk)
    note_obj.delete()
    return redirect('home')
