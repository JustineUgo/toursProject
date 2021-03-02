from rest_framework import serializers
from business.models import Business, Endorsement, Wheel, Media, ShelfPhoto, Shelf


#Business Serializer
class BusinessSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Business
        fields = '__all__'

#Endorsements Serializer
class EndorsementSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Endorsement
        fields = '__all__'


#Wheel Serializer
class WheelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Wheel
        fields = '__all__'


#Media Serializer
class MediaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Media
        fields = '__all__'



#Media Serializer
class ShelfPhotoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ShelfPhoto
        fields = '__all__'


#Shelf Serializer
class ShelfSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Shelf
        fields = '__all__'



