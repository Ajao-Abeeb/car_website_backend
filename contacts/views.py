from django.shortcuts import render , redirect
from .models import Contact
from django.contrib import messages

# Create your views here.
def inquiry(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        car_id = request.POST['car_id']
        customer_need = request.POST['customer_need']
        city = request.POST['city']
        car_title = request.POST['car_title']
        state = request.POST['state']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        
        contact = Contact.objects.create( first_name = first_name, last_name=last_name,car_id=car_id,customer_need=customer_need,city=city,car_title=car_title,state=state,email=email,phone=phone,message=message, user_id=user_id )
        contact.save()
        messages.success(request,"Your requests submitted, we will get back to you shortly")
    return redirect('/cars/'+car_id )