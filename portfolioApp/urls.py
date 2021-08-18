from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index, name = 'index'),
    path('about', views.about, name = 'about'),
    path('contacts',views.contacts,name = 'contacts'),
    path('portfolio', views.portfolio, name = 'portfolio')


   
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)