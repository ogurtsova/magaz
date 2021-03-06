from django.conf.urls import url
from authentication import views


urlpatterns = [
    url(r'^sign-in/$', views.sign_in, name='sign_in'),
    url(r'^sign-up/$', views.sign_up, name='sign_up'),
    url(r'^sign-out/', views.sign_out, name='sign_out'),
    url(r'^settings/', views.settings, name='settings'),
    url(r'^u/(?P<username>\w+)/', views.user_page, name='user_page'),
]