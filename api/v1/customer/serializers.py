from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from customer.models import *

class AddressSerializer(ModelSerializer):
    class Meta:
        fields = ("id", "address","address_type", "landmark","appartment")
        model = Address