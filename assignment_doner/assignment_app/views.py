from django.shortcuts import render, redirect
from .models import User_data, App_content
from django.core.mail import send_mail
from .helper import generate_otp, send_otp, send_confirmation_mail
from django.core.cache import cache
from django.http import JsonResponse
from django.urls import reverse
from django.contrib import messages
# Create your views here.
def index(request):
    images = App_content.objects.all()
    return render(request, "assignment_app/index.html", {'images': images})

def about(request):
    return render(request, "assignment_app/about.html")

def form(request):
    if request.method == "POST":
        Name = request.POST.get('Name')
        Phone = request.POST.get('Phone')
        Email = request.POST.get('Email')
        WorkType = request.POST.get('WorkType')
        Sheet = request.POST.get('Sheet')
        Date = request.POST.get('Date')
        File = request.POST.get('File')
        
        if Email:
            exist = User_data.objects.filter(Email=Email).exists()
            if exist:
                messages.success(request, "Email Already Exists")
                return redirect(form)
            else:
                otp = generate_otp()
                cache.set(Email, otp, timeout=600)
                send_otp(Email, otp)
                request.session['customer_data'] = {
                                    'Name':Name, 
                                    'Phone':Phone, 
                                    'Email':Email, 
                                    'WorkType':WorkType, 
                                    'Sheet':Sheet, 
                                    'Date':Date, 
                                    'File':File
                }
                
                return redirect(reverse('otp'))
    return render(request, "assignment_app/form.html")


def otp(request):
    if request.method == 'POST':
        entered_otp = request.POST.get('Otp')
        email = request.POST.get('Email')
        cached_otp = cache.get(email)
        if entered_otp == cached_otp:
            customer_data = request.session.get('customer_data')
            if customer_data:
                new_customer = User_data(
                    Name = customer_data['Name'],
                    Phone=customer_data['Phone'], 
                    Email=customer_data['Email'], 
                    WorkType=customer_data['WorkType'], 
                    Sheet=customer_data['Sheet'], 
                    Date=customer_data['Date'], 
                    File=customer_data['File']
                )
                
                new_customer.save()
                customer_detail = {
                    'Name': new_customer.Name,
                    'Phone': new_customer.Phone,
                    'Email': new_customer.Email,
                    'WorkType': new_customer.WorkType,
                    'Sheet': new_customer.Sheet,
                    'Date': new_customer.Date,
                    'File': new_customer.File
                }
                send_confirmation_mail(customer_detail['Email'], customer_detail)
                del request.session['customer_data']
                messages.success(request, "Your order is placed successfully kindly check your email")
                return redirect(index)
        else: 
            messages.success(request, "Invalid otp")
            return redirect(otp)
                
    return render(request, "assignment_app/otp.html")