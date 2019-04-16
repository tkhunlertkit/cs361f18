from django.shortcuts import render, redirect
from django.views import View

from .models import User
from .models import Gift


class Login(View):

    error_messages = ""
    user_not_valid = "username/password incorrect"

    def get(self, request):
        if request.session.get("user"):
            return redirect("user")
        return render(request, "login.html", {"error_messages": self.error_messages})

    def post(self, request):
        self.error_messages = ""
        username = request.POST["username"]
        password = request.POST["password"]
        user = User.objects.all().filter(username=username)

        print(user)
        if len(user) == 0:
            self.error_messages = self.user_not_valid

        elif user[0].password != password:
            self.error_messages = self.user_not_valid

        print(self.error_messages)
        if self.error_messages:
            return redirect("login")

        request.session["user"] = user
        return redirect("user")


class UserView(View):
    def get(self, request):
        pass

    def post(self, request):
        pass


class Register(View):

    data = {}

    def get(self, request):
        return render(request, "register", {"data": self.data})

    def post(self, request):
        pass

