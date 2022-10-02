from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from . import views
router=routers.DefaultRouter()
router.register(r'priceofbitcoin',views.priceofbitcoinviewset)
urlpatterns = [
    path('',include(router.urls)),
    path('add/',views.add,name='add'),
]