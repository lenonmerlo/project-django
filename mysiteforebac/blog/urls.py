from django.urls import path
from blog import views

urlpatterns = [  # Corrigido de `urlspatterns` para `urlpatterns`
    path('', views.PostView.as_view(), name='home')
]
