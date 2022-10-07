from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from . import views
router=routers.DefaultRouter()
router.register('priceofbitcoin',views.priceofbitcoinviewset,basename='price')
urlpatterns = [
    path('',include(router.urls)),
    path('list',views.pricelistofbitcoin.as_view()),
    path('list/<int:pk>',views.pricelistdetail.as_view())
]