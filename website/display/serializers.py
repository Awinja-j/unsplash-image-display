from rest_framework import serializers
from .models import unsplash_photos

class UnsplashPhotosSerializer(serializers.Serializer):
    photo_id = serializers.CharField(max_length=11)
    photo_url= serializers.CharField(max_length=255) 
    photo_image_url = serializers.CharField(max_length=255)
    photo_width = serializers.IntegerField(required=False)
    photo_height = serializers.IntegerField(required=False)
    photo_aspect_ratio = serializers.FloatField(required=False) 
    photo_description = serializers.CharField(max_length=5000, allow_blank=True, allow_null=True)
    photographer_first_name  = serializers.CharField(max_length=255, allow_blank=True, allow_null=True)
    photographer_last_name  = serializers.CharField(max_length=255, allow_blank=True, allow_null=True)
    photo_location_country  = serializers.CharField(max_length=255, allow_blank=True, allow_null=True)
    photo_location_city  = serializers.CharField(max_length=255, allow_blank=True, allow_null=True)
    tagged = serializers.BooleanField()

    def create(self, validated_data):
        return unsplash_photos.objects.get_or_create(**validated_data)

    def update(self, instance, validated_data):
        instance.photo_id = validated_data.get('photo_id', instance.photo_id)
        instance.photo_url= validated_data.get('photo_url', instance.photo_url)
        instance.photo_image_url = validated_data.get('photo_image_url', instance.photo_image_url)
        instance.photo_width = validated_data.get('photo_width', instance.photo_width)
        instance.photo_height = validated_data.get('photo_height', instance.photo_height)
        instance.photo_aspect_ratio = validated_data.get('photo_aspect_ratio', instance.photo_aspect_ratio)
        instance.photo_description = validated_data.get('photo_description', instance.photo_description)
        instance.photographer_first_name  = validated_data.get('photographer_first_name', instance.photographer_first_name)
        instance.photographer_last_name  = validated_data.get('photographer_last_name', instance.photographer_last_name)
        instance.photo_location_country  = validated_data.get('photo_location_country', instance.photo_location_country)
        instance.photo_location_city  = validated_data.get('photo_location_city', instance.photo_location_city)
        instance.tagged = validated_data.get('tagged', instance.tagged)
        instance.save()
        return instance