from django.conf.urls import url

from demo import views

urlpatterns = [
    url(r'^show/$', views.show)

]