from django.shortcuts import render,redirect
from django.http import HttpResponse
from emp.models import Emp



def emp_home(request):
    emps=Emp.objects.all()
    return render(request,'templates/home.html',{'emps':emps})

def add_emp(request):
    if request.method=="POST":
        


        #data fetch
        emp_name=request.POST.get("emp_name")
        emp_id=request.POST.get("emp_id")
        emp_email=request.POST.get("emp_email")
        emp_address=request.POST.get("emp_address")
        emp_phone_no=request.POST.get("emp_phone_no")
        emp_department=request.POST.get("emp_department")
        emp_working=request.POST.get("emp_working")


        #create model object and set the data
        e=Emp()
        e.name=emp_name
        e.email_id=emp_email
        e.phone=emp_phone_no
        e.department=emp_department
        e.address=emp_address
        e.emp_id=emp_id
        


        if emp_working==None:
            e.working=False
        else:
            e.working=True
        e.save()
        
        

        #save the object 
        #prepare msg



        return redirect("/home/")
    return render(request,"templates/addemp.html",{})


def delete_emp(request,emp_id):
    emp=Emp.objects.get(pk=emp_id)
    emp.delete()
    return redirect("/home/")

def about_us(request):
    return render(request,"templates/about.html")

def update_emp(request,emp_id):
    emp=Emp.objects.get(pk=emp_id)
    emp.delete()
    return render(request,"templates/update_emp.html",{'emp':emp})