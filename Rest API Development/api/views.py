from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Item
from .serializers import Itemserializer


@api_view(['GET'])
def getData(request, id=""):
    if id != "":
        items = Item.objects.get(id=id)
        searlizer = Itemserializer(items, many=False)
    else:
        items = Item.objects.all()
        searlizer = Itemserializer(items, many=True)
    return Response(searlizer.data)


@api_view(['POST'])
def addData(request):
    serializer = Itemserializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(["DELETE"])
def deleteData(request, id=None):
    items = Item.objects.get(id=id)
    items.delete()
    return Response({"status": "success", "data": "Item deleted"})

@api_view(["PUT"])
def updateData(request, id=None):
    items = Item.objects.get(id=id)
    serializer = Itemserializer(items, data =  request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({"status": "success", "data": serializer.data})
    else:
        return Response({"status": "error", "data": serializer.errors})
