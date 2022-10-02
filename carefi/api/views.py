from django.shortcuts import render,HttpResponse
from .models import priceofbitcoin
from bs4 import BeautifulSoup as BS
import requests
from rest_framework import viewsets
from .serializers import priceofbitcoinserializer
from rest_framework.permissions import IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly
def add(request):
    # getting the request from url
    url = "https://www.google.com/search?q=bitcoin+price"
    data = requests.get(url)
    # converting the text
    soup = BS(data.text, 'html.parser')
    # finding meta info for the current price
    ans = soup.find("div", class_="BNeawe iBp4i AP7Wnd").text
    # returning the price
    user=priceofbitcoin.objects.create(price=ans)
    user.save()
    form=user
    return render(request,'add.html',{'form':form})
class priceofbitcoinviewset(viewsets.ModelViewSet):
    queryset = priceofbitcoin.objects.all()
    serializer_class = priceofbitcoinserializer
    permission_classes = [IsAuthenticatedOrReadOnly]

