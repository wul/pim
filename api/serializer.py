from rest_framework import serializers

from portal import models

class CatalogSerializer(serializers.ModelSerializer):
    class Meta:
        model  = models.Catalog
        fields = '__all__'


class MemoSerializer(serializers.ModelSerializer):
    class Meta:
        model  = models.Memo
        fields = ('title', 'catalog','created_on', 'updated_on')
        
