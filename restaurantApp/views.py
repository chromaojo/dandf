from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import *


# Global Variables


# Create your views here.
def index(request):
    menus = Menu.objects.all()
    orders = OrderItem.objects.all()

    context = {'menus': menus, 'orders': orders}
    return render(request, 'index.html', context)


def details(request, df):
    det = Menu.objects.get(id=df)
    orders = OrderItem.objects.all()
    
    
    context = {'det': det, 'orders': orders}
    return render(request, 'details.html', context)

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username = username, password = password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "Invalid Login Details")
            return redirect('/login')
    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email Already Exists')
                return redirect('register')
            elif User.objects.filter(username= username).exists():
                messages.info(request,'Username Already Taken')
                return redirect('register')
            else:
                messages.info(request, 'Password Not The Same')
                return redirect('register')
                
        else:
            user = User.objects.create(username=username, password = password, email= email)
            user.save()
            return redirect('/customer')
        
    else:
      
        return render(request, 'register.html')
    return render(request, 'register.html')


def customer(request):
    # profile = Customer.objects.get()
    customer = Customer.objects.all()
    if request.method == 'POST':
        
        surname = request.POST['surname']
        midname = request.POST['midname']
        first_name = request.POST['first_name']
        gender = request.POST['gender']
        about = request.POST['about']
        address = request.POST['address']
        Whatsapp_Number = request.POST['Whatsapp_Number']
        Phone_Number = request.POST['Phone_Number']
        profile_image = request.POST['profile_image']

        customer = Customer.objects.create(surname = surname, midname = midname, first_name = first_name, gender = gender, address = address, Whatsapp_Number = Whatsapp_Number, Phone_Number = Phone_Number, profile_image = profile_image)
        messages.info(request, 'Information Saved')
        customer.save()
        return redirect('/')
    else:
        messages.info(request, 'Customer Profile. Kindly Fill The Form carefully')
        return render(request, 'customer.html')

    context = {"profile": profile, 'customer': customer}   

    return render(request, 'customer.html', context)
    

def upload_Menu(request):
    if request.method == 'POST':
        name = request.POST['name']
        price = request.POST['price']
        details = request.POST['details']
        menu_image = request.POST['menu_image']
        new_item = MenuItem.objects.create(name= name, price= price, details= details, quantity= quantity, menu_image= menu_image, unit_total= unit_total)
        new_item.save()
    else:
        messages.info(request, 'Item Not Uploaded')
        return redirect('/')

    return render(request, 'upload.html', context)



def add_to_cart(request, df):
    det = Menu.objects.get(id=df)
    orders = OrderItem.objects.all()
    totally = sum(order.unit_total for order in orders)
    menus = Menu.objects.all()
    if request.method == 'POST':
        item = det
        quantity = request.POST['quantity']
        if quantity <= '0':
            messages.error(request, "No Negative Quantity Allowed - Go Back To Menu")
        else:
            selected, created = OrderItem.objects.get_or_create(item = item, quantity = quantity)
            selected.save()
        return redirect('/cart')
    else:
        messages.info(request, "Kindly Fill In The Quantity Needed")

    context = {'menus': menus, 'orders': orders, 'det': det, 'totally':totally}
    return render(request, 'add_to_cart.html', context)

def cart(request):
    orders = OrderItem.objects.all() 
    totally = sum(order.unit_total for order in orders)
    
    context = {'orders': orders, 'totally':totally}
    return render(request, 'cart.html', context)

def delete_order(request, df):
    orders = OrderItem.objects.get(id=df)
    orders.delete()
    return redirect('/cart')

def delete_reciept(request, df):
    rece = Reciept.objects.get(id=df)
    rece.delete()
    return redirect('/reciept')


def reciept(request):
    rec = Reciept.objects.all()

    context = {'rec': rec}
    return render(request, 'reciept.html', context)


def reciept_details(request,df):
    record = Reciept.objects.get(id=df)
    

    context = {'record': record}
    return render(request, 'reciept_detail.html', context)
    
def checkout(request):
    orders = OrderItem.objects.all()
    profile = Customer.objects.all()
    totally = sum(order.unit_total for order in orders)
    if request.method == 'POST':
        order = request.POST['order']
        Total = totally
        phone_contact = request.POST['phone_contact']
        destination = request.POST['destination']
        complete = False

        new_order = Reciept.objects.create(order = order, Total = Total, phone_contact = phone_contact, destination = destination)
        new_order.save()
        orders.delete()
        return redirect('/reciept')    

    context = {'orders':orders, 'totally': totally}
    return render(request, 'checkout.html', context)

#    profile = Customer.objects.all()