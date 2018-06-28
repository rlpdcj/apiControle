from rest_framework import serializers
from .models import *


class AcessoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Acesso
        fields = ["id","nome", "validade"]