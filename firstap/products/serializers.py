from rest_framework import serializers

class ProductSerializer(serializers.Serializer):
	title = serializers.CharField(max_length=120)
	name = serializers.CharField(max_length=120)
	summary = serializers.CharField(max_length=120)
