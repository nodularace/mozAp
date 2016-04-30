
from __future__ import absolute_import

from rest_framework import generics
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from rest_framework import serializers

from .models import Provider
from .models import PolygonArea
from .serializers import ProviderSerializer
from .serializers import PolygonAreaSerializer

import logging
logger = logging.getLogger(__name__)

@api_view(['POST', 'PUT', 'GET', 'DELETE'])
@permission_classes((IsAuthenticated,))
def ProviderBulkCUD(request):
    """BATCH Put/Post/Delete for Provider"""
    providers = Provider.objects.all()
    providers_list = []
    if request.method == 'GET':
         for qs in providers:
            providers_list.append({'id': qs.id, 'name':qs.name ,'language':qs.language, 'email':qs.email, 'phone':qs.phone, 'currency':qs.currency})
         return Response(providers_list, status=status.HTTP_200_OK)

    if request.method == 'POST':
         """ Bulk POST """
         providers_post_data = request.data
         bulk_list = []
         if type(request.data) != list:
            return Response({"ERROR": "A list is expected. Not a dictionary.", "data": request.data})

         for prov in providers_post_data:
            bulk_list.append(Provider(**prov))

         Provider.objects.bulk_create(bulk_list)
         return Response({"message": "POST SUCCESSFULL : Got some data!", "data": request.data})

    if request.method == 'DELETE':
         """ Bulk DELETE """
         Provider.objects.all().delete()
         return Response({"message": "DELETE SUCCESSFULL !"})

    if request.method == 'PUT':
         """ Bulk PUT """
         providers_put_data = request.data

         if 'name' in providers_put_data.keys() or 'provider' in providers_put_data.keys() :
              """ Allows everything to change except name"""
              return Response({"message": "Cant be performed: can bulk update not for Name field", "data": request.data})

         Provider.objects.all().update(**providers_put_data)
         return Response({"message": "PUT/Update SUCCESSFULL : Got some data!", "data": request.data})


@api_view(['POST', 'PUT', 'GET', 'DELETE'])
@permission_classes((IsAuthenticated,))
def PolygonAreaBulkCUD(request):
    """BATCH Put/Post/Delete for PolygonArea"""
    areas = PolygonArea.objects.all()
    areas_list = []
    if request.method == 'GET':
         for qs in areas:
            areas_list.append({'id': qs.id, 'name':qs.name, 'latitude':qs.latitude, \
                               'longitude':qs.longitude, 'pricing':qs.pricing, 'provider':qs.provider.id})
         return Response(areas_list, status=status.HTTP_200_OK)

    if request.method == 'POST':
         """ Bulk POST """
         areas_post_data = request.data
         bulk_list = []
         if type(request.data) != list:
            return Response({"ERROR": "A list is expected. Not a dictionary.", "data": request.data})
            
         for area in areas_post_data:
            area['provider_id'] = area['provider'] 
            del area['provider']
            bulk_list.append(PolygonArea(**area))

         PolygonArea.objects.bulk_create(bulk_list)
         return Response({"message": "POST SUCCESSFULL : Got some data!", "data": request.data})

    if request.method == 'DELETE':
         """ Bulk DELETE """
         PolygonArea.objects.all().delete()
         return Response({"message": "DELETE SUCCESSFULL !"})

    if request.method == 'PUT':
         """ Bulk PUT """
         areas_put_data = request.data

         if 'name' in areas_put_data.keys() or 'phone' in areas_put_data.keys() or 'email' in areas_put_data.keys():
              """ Allows only currency and language"""
              return Response({"message": "Cant be performed: can bulk update only currency or language", "data": request.data})

         PolygonArea.objects.all().update(**areas_put_data)
         return Response({"message": "PUT/Update SUCCESSFULL : Got some data!", "data": request.data})



class ProviderCreate(generics.CreateAPIView):
    """
    Provider Create API
    """
    permission_classes = (IsAuthenticated,)
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer


class ProviderDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Provider Detail API
    """
    permission_classes = (IsAuthenticated,)
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer


class ProviderList(generics.ListAPIView):
    """
    Provider List API
    """
    permission_classes = (IsAuthenticated,)
    filter_fields = ('email',)

    def get_serializer_class(self):
            return ProviderSerializer

    def get_queryset(self):
        providers = Provider.objects.all()
        return providers

class PolygonAreaCreate(generics.CreateAPIView):
    """
    PolygonArea Create API
    """
    permission_classes = (IsAuthenticated,)
    queryset = PolygonArea.objects.all()
    serializer_class = PolygonAreaSerializer


class PolygonAreaDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    PolygonArea Detail API
    """
    permission_classes = (IsAuthenticated,)
    queryset = PolygonArea.objects.all()
    serializer_class = PolygonAreaSerializer


class PolygonAreaList(generics.ListAPIView):
    """
    PolygonArea List API
    """
    permission_classes = (IsAuthenticated,)
    queryset = PolygonArea.objects.all()
    filter_fields = ('latitude', 'longitude', )
    serializer_class = PolygonAreaSerializer

