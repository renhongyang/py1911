from rest_framework import serializers
from .models import *

class AdsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Ads
        fields = "__all__"