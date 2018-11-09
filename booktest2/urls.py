from django.urls import path
from . import views

urlpatterns = [
    path('login_ajax/', views.login_ajax),
    path('login_ajax_check/', views.login_ajax_check),

]