from tempfile import template
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'myapp'
urlpatterns = [
    path('', views.index , name='index'),
    path('category/<int:pk>/', views.category_product, name='category_product'),
    path('about/', views.about, name='about'),
    path('gallery/', views.gallery, name='gallery'),
    path('contact/', views.contact, name='contact'),
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)