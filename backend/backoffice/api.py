from django.http import JsonResponse

from rest_framework.decorators import api_view, permission_classes

from .models import Sport
from .serializers import SportSerializer

@api_view(['GET'])
@permission_classes([])
def sports_list(request):
    """
    Returns the sports list in api
    """
    sports = Sport.objects.all()
    serializer = SportSerializer(sports, many=True)

    return JsonResponse({
        'data': serializer.data
    })