from rest_framework import serializers
from .models import priceofbitcoin
class priceofbitcoinserializer(serializers.ModelSerializer):
    class Meta:
        model=priceofbitcoin
        fields=['id','price','dateandtime']