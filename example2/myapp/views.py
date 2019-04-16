from django.shortcuts import render
from django.views import View
from .models import Data

# Create your views here.
class Home(View):
    def get(self, request):
        # return html formatted text
        return render(request, 'index.html')

    def post(self, request):
        val = request.POST['a']
        Data(a=val).save()
        all_data = Data.objects.all()
        return render(request, 'index.html', {'data': all_data})
