from rest_framework import serializers
from ..models import Items

class ItemsModelSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)
    
    class Meta:
        model = Items
        #fields = ('id', 'category', 'color', 'image', 'rmbg_image')
        #fields = '__all__'
        fields = ('image', 'category', 'color', 'id', 'rmbg_image')