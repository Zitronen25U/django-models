from django.urls import path
from django.urls.resolvers import URLPattern
from .views import HomePageView, SnacksView, SnacksDetail, AboutPageView

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('about/', AboutPageView.as_view(), name="about"),
    path('', SnacksView.as_view(), name="snack_list"),
    path("<int:pk>/", SnacksDetail.as_view(), name="snack_detail"),
]
