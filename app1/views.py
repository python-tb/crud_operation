from django.shortcuts import render,redirect
from .models import Student

def home(request):
    return render(request,'home.html')


def show_student(request):
    students = Student.objects.all()
    return render(request,'show_student.html',{'std':students},)


def add_student(request):
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        course = request.POST['course']
        address = request.POST['address']
        std = Student(name=name,age=age,course=course,address=address)
        std.save()
        
        return redirect('/show_student')
    else:
        return render(request, 'add_student.html')
    


def update_student(request,pk):
    student = Student.objects.get(id=pk) 
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        course = request.POST['course']
        address = request.POST['address']
        student.name = name 
        student.age = age 
        student.course = course 
        student.address = address 
        student.save()
        return redirect('/show_student')
    else:
        return render(request, 'update_student.html',{'std':student})
    


def delete_student(request,pk):
    student = Student.objects.get(id=pk)
    student.delete()
    return redirect('/show_student')
    