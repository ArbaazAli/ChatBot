from django.shortcuts import render
from .models import Student


def home(request):
    return render(request, 'index.html')

'''
def home(request):
    user = "hello"
    chatbot = "hello how are you doing!!"
    if request.method == 'POST':
        output = request.POST['input']
        return render(request, 'chatbot.html', {'output' : output})
    return render(request, 'chatbot.html', {'user': user, 'chatbot': chatbot,})
'''

def register(request):
    if request.method == 'POST':
        student_name = request.POST['student-name']
        student_id = request.POST['student-id']
        student_email = request.POST['student-email']
        student_contact = request.POST['student-contact']
        student_branch = request.POST['student-branch']
        student_password = request.POST['student-password']
        student_password2 = request.POST['student-password2']
        data = Student(student_name = student_name, student_id = student_id, student_contact = student_contact, student_email = student_email, student_branch = student_branch, password = student_password, confirm_password = student_password2)
        data.save()
        
    
    else:
        return render(request, 'register.html', {})


def login(request):
    return render(request, 'login.html', {})

