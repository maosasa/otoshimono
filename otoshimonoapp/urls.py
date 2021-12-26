from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'otoshimonoapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:otoshimono_id>/', views.detail, name='detail'),
    path('about/', views.about, name="about"),
    path('list/', views.listing, name="list"),
] + static(settings.MEDIA_URL, document_root=settings.BASE_DIR)