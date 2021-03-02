from rest_framework import viewsets, permissions
from business.models import Business, Endorsement, Wheel, Media, ShelfPhoto, Shelf
from .serializers import BusinessSerializer, EndorsementSerializer, WheelSerializer, MediaSerializer, ShelfPhotoSerializer, ShelfSerializer


#Business ViewSet
class BusinessViewSet(viewsets.ModelViewSet):
    queryset = Business.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = BusinessSerializer


class ABusinessViewSet(viewsets.ModelViewSet):
    #business1 = Business.objects.get(pk=1)
    permission_classes = [
        permissions.AllowAny 
    ]
    serializer_class = BusinessSerializer
    
    def get_queryset(self):
        request_name = self.request.query_params.get('name')
        #get the name parameter from a request to this api(EndorsementViewSet)
        
    #get the business class of the name
    
        
        return Business.objects.filter(name=request_name)



#ENDORSEMENT VIEWSET                    CHECKLISTVIEWSET CODING WITH MICH FOR PAGINATION
#Query all endorsments
class EndorsementViewSet(viewsets.ModelViewSet):
    
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = EndorsementSerializer
    queryset = Endorsement.objects.all()
    

#Query a business endorsers
class BusinessEndorsementViewSet(viewsets.ModelViewSet):
    #business1 = Business.objects.get(pk=1)
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = EndorsementSerializer
    
    def get_queryset(self):
        request_name = self.request.query_params.get('name')
        #get the name parameter from a request to this api(EndorsementViewSet)
        
        business = Business.objects.get(name=request_name)
        #get the business class of the name
        
        queryset = business.business_endorsements_set.all()
        
        return queryset



#WHEEL VIEWSET                    CHECKLISTVIEWSET CODING WITH MICH FOR PAGINATION
#Query a business endorsers
class WheelViewSet(viewsets.ModelViewSet):
    
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = WheelSerializer
    
    def get_queryset(self):
        request_name = self.request.query_params.get('name')
        
        business = Business.objects.get(name = request_name)
        queryset = business.business_wheel_set.all()
        
        return queryset
    
    
    
    
#MEDIA VIEWSET                    CHECKLISTVIEWSET CODING WITH MICH FOR PAGINATION
#Query all media files
class MediaViewSet(viewsets.ModelViewSet):
    
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = MediaSerializer
    queryset = Media.objects.all()
    
    
#Query a business media files
class BusinessMediaViewSet(viewsets.ModelViewSet):
    
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = MediaSerializer
    
    def get_queryset(self):
        requested_name = self.request.query_params.get('name')
        
        business = Business.objects.get(name = requested_name)
        queryset = business.business_media_set.all()

        return queryset    
    
    
    
    
    
    
#SHELF PHOTO VIEWSET                    CHECKLISTVIEWSET CODING WITH MICH FOR PAGINATION
#Query all shelf photos
class ShelPhotoViewSet(viewsets.ModelViewSet):
    
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ShelfPhotoSerializer
    queryset = ShelfPhoto.objects.all()
    


#Query Shelf photo based on id
#class BusinessShelfPhotoViewSet(viewsets.ModelViewSet):
#    permission_classes = [
#        permissions.AllowAny
#    ]
#    serializer_class = ShelfPhotoSerializer
    
#    def get_queryset(self):
#        requested_id = self.request.query_params.get('id')
        
#        #business = Business.objects.get(id = requested_id)
#        queryset = ShelfPhoto.objects.filter(id = int(requested_id))
        
#        return queryset
    
    
    
#SHELF VIEWSET                    CHECKLISTVIEWSET CODING WITH MICH FOR PAGINATION
#Query all shelf photos
class ShelfViewSet(viewsets.ModelViewSet):
    
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = ShelfSerializer
    queryset = Shelf.objects.all()
    


#Query Shelf photo based on category by a business
class BusinessShelfViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = ShelfSerializer
    
    def get_queryset(self):
        
        requested_name = self.request.query_params.get('name')
        
        business = Business.objects.get(name = requested_name)
        queryset = business.business_shelf_set.all()
        #queryset = Category.objects.filter(created_by__email = str(requested_email))
    
        return queryset
    
    

    
    
    
    
    