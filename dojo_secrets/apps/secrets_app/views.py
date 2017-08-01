from django.shortcuts import render, redirect, reverse
from django.db.models import Count
from ..login_app.models import User
from .models import Secret

#Q: What's the first thing we need inside of our secrets app to get it to work???
#A: We need to be able to create secrets!
# Create your views here.
def index(request):
    #how do i get my currently logged in user?
    current_user = User.objects.currentUser(request)
    # secrets = Secret.objects.all()
    secrets = Secret.objects.annotate(num_likes=Count('liked_by'))

    

    #so how do i see all the users that have liked my secret? liked_by.all()
    #i can access this relationship on the front end: html

    context = {
        'user': current_user,
        'secrets': secrets,
    }

    return render(request, 'secrets_app/index.html', context)

def create(request):
    print "Inside the create method."
    if request.method == "POST":

        if len(request.POST['content']) != 0:
            current_user = User.objects.currentUser(request)
            #so if content is not empty then lets create a secret method
            secret = Secret.objects.createSecret(request.POST, current_user)

    return redirect(reverse('success'))

def like(request, id):
    current_user = User.objects.currentUser(request)
    secret = Secret.objects.get(id=id)
    #so now we just need to relate the two tables = .add method..
    #to get to the relationship from the Secret it would be = Secret.liked_by
    #to get to the rel from the User it would be = User.likes
    #one way: current_user.likes.add(secret) & another way secret.liked_by.add(current_user)
    current_user.likes.add(secret)

    return redirect(reverse('success'))

def unlike(request, id):
    current_user = User.objects.currentUser(request)
    secret = Secret.objects.get(id=id)
    
    current_user.likes.remove(secret)

    return redirect(reverse('success'))

def delete(request, id):
    if request.method == "POST":
        secret = Secret.objects.get(id=id)
        current_user = User.objects.currentUser(request)
# if the user matches the same id of the secret post id 
        if current_user.id == secret.user.id:
            secret.delete()

    return redirect(reverse('success'))

#What do we need to do to count how many times something is liked? See index section. 
#We need an annotation command. count of first names as num first names...
#  select Count(user.id) as num_users = you can use annotate to do the same kind of thing.



