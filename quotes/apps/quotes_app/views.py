from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.db.models import Count
from .models import User, Quote
import bcrypt

# Create your views here.
def flashErrors(request, errors):
    for error in errors:
    
        messages.error(request, error)

def currentUser(request):
    id = request.session['user_id']

    return User.objects.get(id=id)

def index(request):

    return render(request, 'quotes_app/index.html')

def dashboard(request):
    if 'user_id' in request.session:
        
        user = User.objects.currentUser(request)
        wishlist = user.quotes.all()
        posted_by = Quote.objects.exclude(id__in = wishlist)
        context = {
            'current_user': user,
            'posted_by': posted_by,
            'wishlist': wishlist
        }
        
        return render(request, 'quotes_app/dashboard.html', context)

    return redirect('landing')

def register(request):
    if request.method == "POST":

        errors = User.objects.validateRegistration(request.POST)

        if not errors:
            user = User.objects.createUser(request.POST)
            request.session['user_id'] = user.id

            return redirect('dashboard')

        flashErrors(request, errors)

    return redirect('landing')
    

def login(request):
    if request.method == "POST":
        
        errors = User.objects.validateLogin(request.POST)
    
        if not errors:
            user = User.objects.filter(email = request.POST['email']).first()

            if user:
                password = str(request.POST['password'])
                user_password = str(user.password)

                hashed_pw = bcrypt.hashpw(password, user_password)
               
                if hashed_pw == user.password:
                    request.session['user_id'] = user.id

                    return redirect('dashboard')
               
            errors.append("Invalid account information.")

        flashErrors(request, errors)

    return redirect('landing')            

def logout(request):
    if 'user_id' in request.session:

        request.session.pop('user_id')

    return redirect('landing')

# def quotes(request):
#     if 'user_id' not in request.session:
#         return redirect('dashboard')

#     current_user = User.objects.currentUser(request)
#     quotes = Quote.objects.annotate(num_posts=Count('creator_id'))

#     context = {
#         'user': current_user,
#         'quotes': quotes
#     }

#     return render(request, 'quotes_app/quotes.html', context)

def addQuote(request, id):
    if request.method == "POST":
        
        if 'user_id' in request.session:
            current_user = User.objects.currentUser(request)
            quotes = User.objects.get(id=id)
            current_user.quotes.add(quotes)

            return redirect('dashboard')

    return redirect('landing')

def removeQuote(request, id):
    if request.method == "POST":
        
        if 'user_id' in request.session:
            current_user = User.objects.currentUser(request)
            quotes = User.objects.get(id=id)
            current_user.quotes.remove(quotes)

            return redirect('dashboard')

    return redirect('landing')

def deleteQuote(request, id):
    if request.method == "POST":

        if 'user_id' in request.session:
            current_user = User.objects.currentUser(request)
            quotes = User.objects.get(id=id)
            current_user.quotes.delete(quotes)

            return redirect(reverse('dashboard'))

    return redirect('landing')

def create(request):
    if request.method == "POST":
        errors = []
        if len(request.POST['quote']) < 3:
            errors.append('Please enter Quoted By!')
            flashErrors(request, errors)
        if len(request.POST['message']) < 10:
            errors.append('Please enter your Quote!')
            flashErrors(request, errors)
            #so if content is not empty then lets create a quote method
        else:
            user = User.objects.currentUser(request)
            quote = Quote.objects.create(
                content = request.POST['quote'],
                creator = user
            )
            quote.users.add(user)
    return redirect('dashboard')
