from django.conf.urls import url
from AppTwo import views
#from django.urls.resolvers import URLPattern 
#from django.conf.urls import url


urlpatterns = [
    url(r'^$', views.index, name='index'), 
]