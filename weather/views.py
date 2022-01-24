from django.shortcuts import render
from django.views import View


# Create your views here.
class Weather(View):
    template_name = "index.html"

    def get(self, request):
        return render(request, template_name=self.template_name)



