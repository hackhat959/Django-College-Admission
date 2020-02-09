from django.shortcuts import render
from django.http import HttpResponse
from .models import AdmissionPerson


def index(request):    
    return render(request, 'app/index.html')


def add_student_info(request):
    #print('hiii')
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    student_email = request.POST['student_email']
    student_number = request.POST['student_number']
    student_address = request.POST['student_address']
    student_address2 = request.POST['student_address2']
    student_city = request.POST['student_city']
    student_state = request.POST['student_state']
    student_zip = request.POST['student_zip']
    student_course = request.POST['student_course']
    all_info = AdmissionPerson(first_name = first_name, last_name = last_name ,student_email = student_email , student_number = student_number , student_address = student_address , student_address2 = student_address2 ,student_city = student_city , student_state = student_state , student_zip = student_zip,student_course = student_course)
    all_info.save()
    return render(request , 'app/index.html')