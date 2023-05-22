from rest_framework import serializers
from .models import *

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product_View
        fields=('name','description','total_buyers')