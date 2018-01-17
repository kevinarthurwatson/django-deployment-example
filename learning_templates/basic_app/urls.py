from django.conf.urls import url
from basic_app import views

#template tagging
app_name = 'basic_app' #set a variable to the app name

#this tells the program if you go to domain.com/basic_app/relative it will give the relative views.
urlpatterns = [
    url(r'^relative/$',views.relative,name='relative'),
    url(r'^other/$',views.other,name='other'),
]
