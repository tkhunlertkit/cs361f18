from django.shortcuts import render, redirect
from django.views import View

from .models import User
from .models import Gift


class Login(View):

    user_not_valid = "username/password incorrect"

    def get(self, request):
        if request.session.get("username"):
            return redirect("user")

        return render(request, "login.html")

    def post(self, request):
        username = request.POST["username"]
        password = request.POST["password"]
        user = User.objects.all().filter(username=username)

        error_messages = ""
        if user.count() == 0:
            error_messages = self.user_not_valid
        elif user[0].password != password:
            error_messages = self.user_not_valid

        print("error messages = " + error_messages)
        if error_messages:
            return render(request, "login.html", {"error_messages": error_messages})

        request.session["username"] = username
        return redirect("user")


class UserView(View):
    def get(self, request):
        if not request.session.get("username"):
            return redirect("login")

        username = request.session["username"]
        users = User.objects.all()
        print("username: " + username)

        return render(request, "user.html", {"username": username, "users": users})

    def post(self, request):
        pass


class Register(View):
    def get(self, request):
        print("here?")
        return render(request, "register.html")

    def post(self, request):
        request.session.pop("error_messages", None)
        email = request.POST["email"]
        username = request.POST["username"]
        password = request.POST["password"]

        check_user = User.objects.all().filter(username=username)
        if check_user.count() != 0:
            error_messages = "%s exists, please use another username" % (username)
            return render(request, "register.html", {"error_messages": error_messages})
        
        User(email=email, username=username, password=password).save()

        return redirect("login")


class GiftView(View):
    pass
