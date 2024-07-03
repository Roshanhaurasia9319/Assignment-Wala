import string
from django.core.mail import send_mail
import random
from django.conf import settings 

def generate_otp(length = 4):
    digits = string.digits 
    otp = ''.join(random.choices(digits, k=length))
    return otp

def send_otp(email, otp):
    subject = 'Your Otp Code'
    message = f'Your otp code for yor Assignment confirmation is {otp}. It is Valid for 10 minutes!! Do not share otp with anyone'
    email_from = settings.DEFAULT_FROM_EMAIL
    recipient_list = [email]
    send_mail(subject, message,email_from, recipient_list)
    
    
    
    
    
def send_confirmation_mail(email, customer_detail):
    try:
        sheet = int(customer_detail['Sheet'])
        work = customer_detail['WorkType']
        price = 0
    
        if work == "Assignment":
            price = 5*sheet
        else:
            price = 50*sheet
        
        total = str(price)
    except:
        print("Error")
        
    message = f"""
    Hello {customer_detail['Name']},

    Your order has been placed successfully! Here are your details:
    Name: {customer_detail['Name']}
    Phone: {customer_detail['Phone']}
    Email: {customer_detail['Email']}
    Work Type: {customer_detail['WorkType']}
    Sheet: {customer_detail['Sheet']}
    Date Of Delivery: {customer_detail['Date']}
    File: {customer_detail['File']}
    Your Charges For Work is : {total}Rs,
    Our team will contact you soon
    Thank you for using our service!
    Best regards,
    Assignment Wala Team
    """
    
    send_mail(
        "Your Order Is Placed Successfully",
        message,
        "appt79825@gmail.com",
        [email],
        fail_silently=False,
    )