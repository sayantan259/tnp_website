from django.shortcuts import render,redirect
from django.contrib.auth.models import User  

# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.views import LoginView
from .models import College
from django.http import HttpResponse
from dashboard.models import Shared_Company,Shared_HR_contact,UserDetails,HRContact

def dashboard(request):
    return render(request,'dashboard/companies.html')

def company_contact(request):
    return render(request,'company_contact.html')

# company_contact_handler
        
def handle_comapany_contact(request):
    if request.method == 'POST':
        company_name = request.POST.get('company-name')
        comp_email = request.POST.get('company-email')
        comp_contact = request.POST.get('company-number')
        ctc = request.POST.get('ctc')
        clg_visited = request.POST.get('clg-vis')
        selected_options = request.POST.getlist('intern1')
        is_company = request.POST.get('is_company')
        locations = request.POST.get('location-id')
        users = request.user
        branch = users.userdetails.college_branch

        res = Shared_Company.objects.filter(company_name=company_name).exists()
        if res==True:
            return render(request,'dashboard/company_contact.html',{'msg':'Company Already Exist !!!'})
        else:
            comp_db_obj = Shared_Company(company_name=company_name,company_email=comp_email,company_contact=comp_contact,ctc=ctc,college_visited=clg_visited,type=selected_options,is_company=is_company,location=locations,college_branch=branch,user=users)
            comp_db_obj.save()
            return render(request,'dashboard/company_contact.html',{'msg':'Data Saved Successfully.'})
    else:    
        return render(request,'dashboard/company_contact.html')
    

def hr_contact(request):
    return render(request,'dashboard/hr_contact.html')
     
# HR_contact_handler

def handle_hr_contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        company_name = request.POST.get('company-name')
        email = request.POST.get('company-email')
        contact_number = request.POST.get('number')
        linkedin = request.POST.get('linkedin')
        
        users = request.user
        print(users.userdetails.college_branch)
        hr_db_obj = Shared_HR_contact(name=name, company_name=company_name, email=email, contact_number=contact_number,linkedin_id=linkedin,college_branch=users.userdetails.college_branch,user=users)
        hr_db_obj.save()
        return redirect(request.path,{'msg':'Data Saved successfully!!!!'})
    else:
        print("devvrat")
        return render(request , 'dashboard/hr_contact.html')



# TNP View of HR contact 
    
def print_list(request):
    res = Shared_HR_contact.objects.all()
    return render(request,'dashboard/hr_list.html',{'hr_list':res})
    
def tnp_view(request):
    res = Shared_HR_contact.objects.all()
    return render(request,'dashboard/tnp_view.html',{'hr_list':res})

def delete_all_contact(request):
    Shared_HR_contact.objects.all().delete()
    return render(request,'dashboard/tnp_view.html')

def transfer_contact(request,hr_id):
    sh_hr_obj =  Shared_HR_contact.objects.get(id=hr_id)
    name = sh_hr_obj.name
    company = sh_hr_obj.company_name
    email = sh_hr_obj.email
    contact = sh_hr_obj.contact_number
    linked = sh_hr_obj.linkedin_id
    clg_branch = sh_hr_obj.college_branch
    # hr_cont_obj = HRContact(name=name, company_name=company_name, email=email, contact_number=contact_number,linkedin_id=linkedin,college_branch=users.userdetails.college_branch,user=users)

    return render(request,'dashboard/tnp_view.html') 
    

# TNP View of Company Details 
 
def tnp_company_view(request):
    res = Shared_Company.objects.all()
    return render(request,'dashboard/tnp_company_view.html',{'company_list':res})

def delete_all_company_contact(request):
    Shared_Company.objects.all().delete()
    return render(request,'dashboard/tnp_view.html')

