from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = "pages/home.html"

class AboutMePageView(TemplateView):
    template_name = "pages/aboutme.html"

# def view_function(request):
#     html = "<h1>Hello, World!</h1>"
#     return HttpResponse(html)
