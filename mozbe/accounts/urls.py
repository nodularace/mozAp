from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^provider/createprovider$',
        views.ProviderCreate.as_view(), name = "provider-create"),
    url(r'^provider/(?P<pk>[0-9]+)/$',
        views.ProviderDetail.as_view(), name = "provider-detail"),
    url(r'^providers/$',
        views.ProviderList.as_view(), name = "provider-list"),
    url(r'^area/create-area$',
        views.PolygonAreaCreate.as_view(), name = "area-create"),
    url(r'^area/(?P<pk>[0-9]+)/$',
        views.PolygonAreaDetail.as_view(), name = "area-detail"),
    url(r'^areas/$',
        views.PolygonAreaList.as_view(), name = "area-list"),
    url(r'provider-batch-operate/', 
        views.ProviderBulkCUD, name = 'batch-operate-providers'),
    url(r'area-batch-operate/', 
        views.PolygonAreaBulkCUD, name = 'batch-operate-areas')
]
