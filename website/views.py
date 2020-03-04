from django.shortcuts import render, HttpResponseRedirect, HttpResponse, reverse
from .models import Student
import base64


def home(request):
    return render(request, 'index.html')


def bot(request):
    user = "hello"
    chatbot = "hello how are you doing!!"
    if request.method == 'POST':
        output = request.POST['input']
        return render(request, 'chat.html', {'output' : output})
    return render(request, 'chat.html', {'user': user, 'chatbot': chatbot,})


def register(request):
    if request.method == 'POST':
        student_name = request.POST['student-name']
        student_id = request.POST['student-id']
        student_email = request.POST['student-email']
        student_contact = request.POST['student-contact']
        student_branch = request.POST['student-branch']
        student_password = request.POST['student-password']
        data = Student(student_name = student_name, student_id = student_id, student_contact = student_contact, student_email = student_email, student_branch = student_branch, student_password = student_password)
        data.save()
        return HttpResponseRedirect(reverse('login'))
   
    return render(request, 'register.html', {})


def login(request):
    if request.method == 'POST':
        student_id = request.POST['username']
        password = request.POST['password']
        if Student.objects.filter(student_id = student_id, student_password = password).exists():
            return HttpResponseRedirect(reverse('chatbot'))  
        else:
            return HttpResponse('Wrong ID number')
    return render(request, 'login.html', {})

