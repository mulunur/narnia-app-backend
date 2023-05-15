from rest_framework import serializers
from ..models import Items
from drf_extra_fields.fields import Base64ImageField

class ItemsModelSerializer(serializers.ModelSerializer):
    #image = serializers.ImageField(use_url=True, max_length=None)
    image = Base64ImageField()
    class Meta:
        model = Items
        fields = ('image', 'category', 'color', 'id', 'rmbg_image')