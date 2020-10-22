from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

class AddToN(TemplateView):
    template_name = "pages/addton.html"

