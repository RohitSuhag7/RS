from django.shortcuts import render, redirect

from django.contrib.auth.hashers import make_password, check_password
from store.models.customer import Customer
from django.views import View
    

class Signup(View):
    def get(self, request):
        return render(request, "signup.html")
    
    def post(self, request):
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        email = postData.get('email')
        password = postData.get('password')
        # Validation
        value = {
            'first_name': first_name, 'last_name': last_name, 'email': email
        }
        error_message = None

        customer = Customer(first_name=first_name, last_name=last_name, email=email, password=password)

        error_message = self.validateCustomer(customer)

        if not error_message:
            #print(first_name, last_name, email, password)    
            customer.password = make_password(customer.password)       
            customer.register()
            return redirect('index')
        else:
            data = {
                'error': error_message,
                'values': value,
            }
            return render(request, 'signup.html', data)

    def validateCustomer(self, customer):
        error_message = None

        if(not customer.first_name):
            error_message = "First Name required!"
        elif len(customer.first_name) < 3:
            error_message = "First Name must have 3 or more char"
        elif not customer.last_name:
            error_message = "Last Name required!"
        elif len(customer.last_name) < 3:
            error_message = "Last Name must have 3 or more char"
        elif len(customer.email) < 5:
            error_message = "Email required"
        elif not customer.password:
            error_message = "Password required!"
        elif len(customer.password) < 5:
            error_message = "Password must have 5 or more char"
        elif customer.isExists():
            error_message = "Email Already Registered"
            
        return error_message


