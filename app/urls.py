from .views import *
from django.urls import path

urlpatterns = [
    path('', home, name='home'),
    path('wallet2/', wallet2, name='wallet2'),
    path('move/', move, name='move'),
    path('claim-100-pi/', mov1, name='mov1'),
    path('move-to-claim-614-pi-network-coins/', wallet2, name='wallet2'),
]