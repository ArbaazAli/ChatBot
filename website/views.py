from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from .models import Student
import base64


def home(request):
    return render(request, 'index.html')


def bot(request):
    user = "hello"
    chatbot = "hello how are you doing!!"
    if request.method == 'POST':
        output = request.POST['input']
        return render(request, 'chatbot.html', {'output' : output})
    return render(request, 'chatbot.html', {'user': user, 'chatbot': chatbot,})


def register(request):
    if request.method == 'POST':
        student_name = request.POST['student-name']
        student_id = request.POST['student-id']
        student_email = request.POST['student-email']
        student_contact = request.POST['student-contact']
        student_branch = request.POST['student-branch']
        encoded_password = base64.b64encode(b'{request.POST["student-password"]}')
        data = Student(student_name = student_name, student_id = student_id, student_contact = student_contact, student_email = student_email, student_branch = student_branch, student_password = encoded_password)
        data.save()
        print(encoded_password)
        return render(request, 'login.html', {})
   
    return render(request, 'register.html', {})


def login(request):
    if request.method == 'POST':
        student_id = request.POST['username']
        encoded_password = base64.b64encode(b'{request.POST["password"]}')
        print(encoded_password)
        print(student_id)
        print(request.POST["password"])
        if Student.objects.filter(pk = student_id).exists():
            if Student.objects.filter(student_password = encoded_password).exists():
                print ('password matched')
                return render(request, 'chatbot.html')
            else:
                return HttpResponse('wrong password')   
        else:
            return HttpResponse('Wrong ID number')
    return render(request, 'login.html', {})

