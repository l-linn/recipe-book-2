from django.shortcuts import render, redirect

# Django authentication libraries
from django.contrib.auth import authenticate, login, logout

# Django Form for authentication
from django.contrib.auth.forms import AuthenticationForm


# define a function view called login_view that takes a request from user
def login_view(request):
    # initialize:
    # error_message to None
    error_message = None
    # form object with username and password fields
    form = AuthenticationForm()

    if request.method == "POST":
        # read the data sent by the form via POST request
        form = AuthenticationForm(data=request.POST)

    if form.is_valid():
        username = form.cleaned_data.get("username")  # read username
        password = form.cleaned_data.get("password")  # read password

        # use Django authenticate function to validate the user
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("/recipes")  # & send the user to desired page
        else:
            error_message = "ooops.. something went wrong"
        # prepare data to send from view to template
    context = {
        "form": form,  # send the form data
        "error_message": error_message,  # and the error_message
    }
    # load the login page using "context" information
    return render(request, "auth/login.html", context)


def logout_view(request):
    logout(request)  # the use pre-defined Django function to logout
    return render(
        request, "auth/success.html"
    )  # after logging out go to login form (or whichever page you want)


def about_me_view(request):
    return render(request, "about.html")
