from django.urls import path

from .views import our_work,doner,team

urlpatterns = [
    path('our-work/', our_work),
    path('doner/', doner),
    path('team/', team),
]