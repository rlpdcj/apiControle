from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^acessos$', AcessoList.as_view()),
    url(r'^acessos/(?P<pk>[0-9]+)$', AcessoDetalhes.as_view()),
]
