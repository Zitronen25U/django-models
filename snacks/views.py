from django.views.generic import TemplateView, ListView, DetailView
from .models import Snacks

class HomePageView(TemplateView):
    template_name = "home.html"

class AboutPageView(TemplateView):
    template_name = "about.html"

class SnacksView(ListView):
    template_name = "snack_list.html"
    model = Snacks

class SnacksDetail(DetailView):
    template_name = "snack_detail.html"
    model = Snacks