from django.urls import path,include
from . views import landingpage,success_page
urlpatterns = [
    path('', landingpage,name="landing-page"),
     path('success/', success_page,name="success-page"),

]
