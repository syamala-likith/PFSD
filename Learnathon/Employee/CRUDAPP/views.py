from django.core.mail import send_mail
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee

# Create Employee...
def insert_emp(request):
    if request.method == "POST":
        EmpId = request.POST['EmpId']
        EmpName = request.POST['EmpName']
        EmpGender = request.POST['EmpGender']
        EmpEmail = request.POST['EmpEmail']
        EmpDesignation = request.POST['EmpDesignation']
        data = Employee(EmpId=EmpId, EmpName=EmpName, EmpGender=EmpGender, EmpEmail=EmpEmail,
                        EmpDesignation=EmpDesignation)
        data.save()
        return redirect('show/')
    else:
        return render(request, 'insert.html')

# Retrive Employee
def show_emp(request):
    employees = Employee.objects.all()
    return render(request,'show.html',{'employees':employees} )

# Update Employees...

# Update Employee
def edit_emp(request,pk):
    employees = Employee.objects.get(id=pk)
    if request.method == "POST":
        return redirect('/show')
    context = {
        'employees': employees,
    }
    return render(request,'edit.html',context)
# Delete Employees...

# Delete Employee
def remove_emp(request, pk):
    employees = Employee.objects.get(id=pk)
    if request.method == 'POST':
        employees.delete()
        return redirect('/show')
    context = {
        'employees': employees,
    }
    return render(request, 'delete.html', context)

def mail1(request):
    send_mail(
        'Test Mail Using Django Framework',
        'Hello Sir/Mam',
        'rockylikith9886@gmail.com',
        ['2100031023@kluniversity.in'],
        fail_silently = False,
    )
    return print('Mail Sent')
