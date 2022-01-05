from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'otoshimonoapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:otoshimono_id>/', views.detail, name='detail'),
    path('about/', views.about, name="about"),
    path('form/', views.form, name="form"),
    path('list/', views.listing, name="list"),
    path('add/', views.add, name="add"),
    path('form/location/', views.form_location, name="form_location"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)