Magic Method:
<User: Firstname Lastname>
    this method indicates what to do when we ask to display a User object as a string, like when we   print it. This method gives us a way of controlling what we see displayed when we print objects. In our         case, we've set up our User model so that it will be shown as <User: Firstname Lastname> instead of       <User: User object>. It's not required that you add this method to your model classes, but it can be      helpful for viewing objects.

Get
.get(field="val") returns the one object that matches a given condition. If we wanted the one user with last name "Thomas", we could say:
            user = User.objects.get(last_name="Thomas")
            print("QUERY RESULT:", user)

Filter
.filter(field="val"...) returns all of the records where a given condition is true. Here's how we'd find all of the "Thomas"es:
            user = User.objects.filter(last_name="Thomas")
            print("QUERY RESULT:", user)

            user = User.objects.filter(first_name="Horace")
            print("QUERY RESULT:", user)

# What's the difference between .get and .filter in this case? Note that .get returns the object itself, while .filter returns a QuerySet (a type of object that contains a set of query objects). If we changed the code to look like this:

Exclude
.exclude(field="val"...) is the opposite of .filter: It returns all of the records where a given condition is false. Here's every user NOT surnamed "Thomas":
            user = User.objects.exclude(last_name="Thomas")
            print("QUERY RESULT:", user)

Conditions
You can do a more complicated search than just if a given field is equal to a given value. Instead of just passing in the field name as a keyword argument to .get, .filter, or .exclude, you'd pass the field name__lookup type (that's a double underscore, also known as a "dunder" for people on-the-go). For instance, to find users whose first name begins with "S":
            user = User.objects.filter(first_name__startswith="S")
            print("QUERY RESULT:", user)

*That's not the only type of search you can do. Here's everyone whose first name does not contain an "E":
            user = User.objects.exclude(first_name__contains="E")
            print("QUERY RESULT:", user)

*Every user older than 80:
            user = User.objects.filter(age__gt=80)
            print("QUERY RESULT:", user)

Every user 80 or older (see the difference?):
            user = User.objects.filter(age__gte=80)
            print("QUERY RESULT:", user)

Combining queries
Queries can be chained together:
            user = User.objects.filter(last_name__contains="o").exclude(first_name__contains="o")
            print("QUERY RESULT:", user)

            user = User.objects.filter(age__lt=70).filter(first_name__startswith="S")
            print("QUERY RESULT:", user)

If it's the same type of query, instead of being chained you can add multiple arguments to the function:
            user = User.objects.filter(age__lt=70, first_name__startswith="S")
            print("QUERY RESULT:", user)

These are cases where the conditions are joined with AND, as in, all users younger than 70 AND whose first name starts with "S". If you want OR, as in users who are younger than 70 OR whose first_name starts with "S", you can use | (the set union operator):
            user = User.objects.filter(age__lt=70)|User.objects.filter(first_name__startswith="S")
            print("QUERY RESULT:", user)

Displaying on Templates
So far, we've only printed these objects to our terminal. However, it's not difficult to display this information on a template. How do we pass information from our view function into a template? With a context dictionary!

...user_orm_example_project/apps/users/views.py
            def index(request):
                users = User.objects.filter(age__lt=70)|User.objects.filter(first_name__startswith="S")
                context = {"users": users}
                return render(request, "users/index.html", context)

On the template, we can use a for-loop to go over this data.
...user_orm_example_project/apps/users/index.html
#example
<h1>Users</h1>
<table>
  <tr>
    <th>ID</th>
    <th>First Name</th>
    <th>Last Name</th>
    <th>Age</th>
  </tr>
  {% for user in users %}
    <tr>
      <td>{{ user.id }}</td>
      <td>{{ user.first_name }}</td>
      <td>{{ user.last_name }}</td>
      <td>{{ user.age }}</td>
    </tr>
  {% endfor %}
</table>