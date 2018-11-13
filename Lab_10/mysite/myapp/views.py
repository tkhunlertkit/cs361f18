from django.shortcuts import render
from django.views import View
from myapp.controller import commandList, doStuff

# Create your views here.
class Home(View):
    def get(self, request):
        return render(request, "index.html")

    def post(self, request):
        out = doStuff(request.POST["command"],commandList)
        return render(request,"index.html", {"out":out})