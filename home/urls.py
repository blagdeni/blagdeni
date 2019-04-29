from django.urls import path

from .views import HomePageViews, AboutPageView


urlpatterns = [
    path('', HomePageViews.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about')
]
