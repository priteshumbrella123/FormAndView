from django.conf.urls import url
from . import views
from django.views.generic import TemplateView


app_name = 'demo'

urlpatterns = [
   url(r'^$', views.hello, name='hello'),
   url(r'^number/(\d+)/', views.viewArticle, name='number'),
   url(r'^year/(\d{2})/(\d{4})', views.viewArticles, name ='year'),
   url(r'^date/$', views.date, name='date'),
   url(r'^dayweek/$', views.dayWeek, name='dayweek'),
   url(r'^redirect/$', views.hello1, name = 'redirect'),
   url(r'^view/$', views.DayList.as_view(), name='view'),
   url(r'^connection/$', TemplateView.as_view(template_name='hello/login.html')),
   url(r'^login/$', views.login, name='login')
]
