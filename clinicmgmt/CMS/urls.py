from urllib.request import HTTPPasswordMgrWithDefaultRealm
from django.urls import URLPattern, path

from CMS import views
    
    


urlpatterns = [
    
    path('CMS/', views.home),
    
]