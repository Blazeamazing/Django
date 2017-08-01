from django.shortcuts import render, redirect
from .models import Blog, Comment
from .models import User
# the . says this is where i wanna pull from & you wanna pull Blog & Comment

# Create your views here.
def index(request):
    #context dictionary is going to be caught by this awsome ORM
    context = {
        #this is gonna run a:  select * from Blog
    "blogs" : Blog.objects.all()
    }
    return render(request, 'blog_app/index.html', context)

def blogs(request):
    #using ORM (object relational mappers) here: 
    #this is what ORMs do for us. they help run things, but it is still talking to the 
#1st go to the class = Blog, the manager in that class is named objects, and then we are gonna say to create. (we will build custom managers later)
#2nd then we are gonna pass in Key Value pairs ('x,y')but they are not key pairs we are passing in variables as the perameters. 
    Blog.objects.create(title=request.POST['title'], blog=request.POST['blogs'])
    #insert into Blog (title, blog, created_at, updated_at) values (title, blog, now(), now())
    return redirect('/')

def comments(request, id):
#hey lets make a variable
    blog = Blog.objects.get(id=id)
#hey let's make a comment, so you can pass in all the different values you want to create.
    Comment.objects.create(comment=request.POST['comment'], blog=blog)
    return redirect('/')

#Alright, now we want to be able to get all of the comments for each individual blog showing up. go to html--->

# def index(request):
#     print User.objects.all()
#     # A list of objects (or an empty list)
#     User.objects.create(first_name="mike",last_name="mike",password="1234asdf")
#     # Creates a user object
#     print User.objects.all()
#     # A list of objects (or an empty list)
#     u = User.objects.get(id=1)
#     print u.first_name
#     u.first_name = "Joey"
#     u.save()
#     j = User.objects.get(id=1)
#     print j.first_name
#     # Gets the user with an id of 1, changes name and saves to DB, then retrieves again...
#     print User.objects.get(first_name="mike")
#     # Gets the user with a first_name of 'mike' *** THIS MIGHT NEED TO BE CHANGED ***
#     users = User.objects.raw("SELECT * from {{appname}}_user")
#     # Uses raw SQL query to grab all users (equivalent to User.objects.all()), which we iterate through below
#     for user in users:
#         print user.first_name
#     return HttpResponse("ok")
