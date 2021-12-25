from django.urls import path

from . import views

app_name = 'otoshimonoapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:otoshimono_id>/', views.detail, name='detail'),
]