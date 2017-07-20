# Meanwhile, in our views.py file.

# Important!
# The following code will work great the first time you hit a route that calls the index function. But if you refresh the page, you'll get an error. Spend some time figuring out why this is true. Start by figuring out from which line the error originates.

# Inside your app's views.py file
from django.shortcuts import render, HttpResponse
# Pull the User class into the file
from .models import User
def index(request):
    print User.objects.all()
    # A list of objects (or an empty list)
    User.objects.create(first_name="mike",last_name="mike",password="1234asdf")
    # Creates a user object
    print User.objects.all()
    # A list of objects (or an empty list)
    u = User.objects.get(id=1)
    print u.first_name
    u.first_name = "Joey"
    u.save()
    j = User.objects.get(id=1)
    print j.first_name
    # Gets the user with an id of 1, changes name and saves to DB, then retrieves again...
    print User.objects.get(first_name="mike")
    # Gets the user with a first_name of 'mike' *** THIS MIGHT NEED TO BE CHANGED ***
    users = User.objects.raw("SELECT * from {{appname}}_user")
    # Uses raw SQL query to grab all users (equivalent to User.objects.all()), which we iterate through below
    for user in users:
      print user.first_name
    return HttpResponse("ok")

# Know that this code: User.objects.raw("SELECT * from {{appname}}_user") relies on the fact that Django builds our database's tables according to a particular pattern. The pattern is: appname + _ + lowercase_model_name. If you need to create a raw query and aren't sure what the table name is you can always find it by printing the following: User._meta.db_table