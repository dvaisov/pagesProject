from django.urls import path
from .views import HomePageView, AboutPageView, MoreInfo

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about', AboutPageView.as_view(), name='about'),
    path('more_info', MoreInfo.as_view(), name='more_info'),
]
