from django.urls import path
from .views import landingpage

urlpatterns = [
    path("", landingpage, name="landing-page"),
    path('mark-attendance/', landingpage, name='mark_attendance'),
]