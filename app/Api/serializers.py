from rest_framework import serializers
from .models import Produto 

class ProdudoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Produto
		fields ='__all__'