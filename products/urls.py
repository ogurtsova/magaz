from django.conf.urls import url
from products import views


urlpatterns = [
    url(r'^upload', views.upload, name='upload'),

]