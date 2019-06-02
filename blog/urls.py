from django.urls import path
from . import views

# empty path specifies homepage
urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
]
