from django.shortcuts import render
from django.views import View
from .models import Ticket

# Create your views here.
class Home(View):
    def get(self, request):
        tickets = Ticket.objects.all()
        return render(request, "index.html", {'tickets': tickets})

    def post(self, request):
        print (request.POST)
        location = request.POST["location"]
        datetime = request.POST["datetime"]

        Ticket(datetime=datetime, location=location).save()

        tickets = Ticket.objects.all()
        print(tickets)
        return render(request,"index.html", {"tickets": tickets})