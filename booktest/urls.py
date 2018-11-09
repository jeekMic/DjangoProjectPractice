from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index),
    path('index2/', views.index2),
    path('index3/', views.query_book),
    path('login/', views.login),
    path('login_ajax/', views.login_ajax),
    path('login_ajax_check/', views.login_ajax_check),
    path('ajax_test/', views.ajax_test),
    path('ajax_handle/', views.ajax_handle),
    path('login_check/', views.login_check),
    path('my_index/', views.my_index),
    path('book/<int:book_id>', views.detail),
    path('book/create', views.create),
    path('book/delete<int:book_id>', views.delete),
    path('book/areas', views.areas),
]