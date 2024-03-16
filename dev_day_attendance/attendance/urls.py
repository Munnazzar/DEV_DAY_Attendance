from django.urls import path,include
from . views import landingpage
urlpatterns = [
    path('', landingpage,name="landing-page"),
]
