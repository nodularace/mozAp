from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        ' Providers List - ': reverse('provider-list', request=request, format=format),
        ' Create Provider - ': reverse('provider-create', request=request, format=format),
        ' Areas List - ': reverse('area-list', request=request, format=format),
        ' Create Area - ': reverse('area-create', request=request, format=format),
        ' AREA Batch operations: post/put/del - ': reverse('batch-operate-areas', request=request, format=format),
        ' PROVIDER Batch operations: post/put/del - ': reverse('batch-operate-providers', request=request, format=format),
    })

