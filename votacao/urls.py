from django.conf.urls import url
from . import views

urlpatterns = [url(r'^$',views.index,name='index'),
               url(r'^(?P<questao_id>[0-9]+)/$', views.detalhe, name='detalhe'),
               url(r'^(?P<questao_id>[0-9]+)/resultados/$', views.resultados,name='resultados'),
               url(r'^(?P<questao_id>[0-9]+)/voto/$', views.voto, name='voto'),
]