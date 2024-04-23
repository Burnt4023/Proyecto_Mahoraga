from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('index/', views.my_view, name='index'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)