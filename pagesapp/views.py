from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class HomePageView(TemplateView):
    template_name = 'homepage.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'


class MoreInfo(TemplateView):
    template_name = 'more_info.html'
