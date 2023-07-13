from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ItemSerializer
from base.models import Item

# get data
@api_view(['GET'])
def getData(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data) #out is in the form of json

# add data
@api_view(['POST'])
def addItem(request):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)