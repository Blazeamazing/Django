from django.shortcuts import render, redirect
#now we need to start putting this data into our user. step one need access into our user from our view: i.e. User, Product, Post
from .models import User

# Create your views here.
def index(request):
    print "Inside the index method"

    return render(request, 'loginandregister_app/index.html')

#Success page here!
def success(request):
    print "Inside the success method."

    if 'user_id' in request.session:

        user_id = request.session['user_id']

        context = {
            'current_user': User.objects.get(id=user_id)
        }

        return render(request, 'loginandregister_app/success.html', context)

    return redirect('/')

def logout(request):
    request.session.pop('user_id')

    return redirect('/')

def create(request):
    
    print "Inside the create method"
    
    if request.method == "POST":
        form_data = request.POST

        check = User.objects.validate(form_data)

        if check:
            print check

            return redirect('/')

        #Valid Form Data
        user = User.objects.create(
            first_name = form_data['first_name'],
            last_name = form_data['last_name'],
            email = form_data['email'],
            password = form_data['password'],
        )  

        request.session['user_id'] = user.id

        return redirect('/success')
        #so now build out that success page (see above)

    return redirect('/')

def login(request):
    print "Inside the login method."

    if request.method == "POST":
        form_data = request.POST

        check = User.objects.login(form_data)

        if type(check) == type(User()):

            return redirect('/success')

        print check

    return redirect ('/')









