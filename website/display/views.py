import json
from .models import unsplash_photos
from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UnsplashPhotosSerializer

@api_view(['GET'])
def tag_photo(request, pk):
    '''
    change tagged to true or false
    '''
    tag=get_object_or_404(unsplash_photos.objects.all(), pk=pk)
    if tag:
        photo = unsplash_photos.objects.get(photo_id=tag)
        data = {
            "photo_id": photo.photo_id,
            "photo_url": photo.photo_url,
            "photo_image_url": photo.photo_image_url,
            "photo_width": photo.photo_width,
            "photo_height": photo.photo_height,
            "photo_aspect_ratio": photo.photo_aspect_ratio,
            "photo_description": photo.photo_description,
            "photographer_first_name": photo.photographer_first_name,
            "photographer_last_name": photo.photographer_last_name,
            "photo_location_country": photo.photo_location_country,
            "photo_location_city": photo.photo_location_city,
            "tagged": True
        }
        serializer=UnsplashPhotosSerializer(instance=tag, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            tag_saved=serializer.save()
            return index(request._request)

@api_view(['GET'])
def get_photos(request):
    '''
    return all images 
    '''
    photos = unsplash_photos.objects.all()
    serializer=UnsplashPhotosSerializer(photos, many=True)
    return Response({"photos": serializer.data})
  
def index(request):
    images=get_photos(request)
    output_dict = json.loads(json.dumps(images.data['photos']))
    return render(request, 'index.html', {"context":output_dict})
