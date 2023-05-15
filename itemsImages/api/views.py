from django.http import HttpResponse
from rest_framework import viewsets
from ..models import Items
from .serializers import ItemsModelSerializer
from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

class ItemsViewSet(viewsets.ModelViewSet):
#class ItemsViewSet(APIView):
    queryset = Items.objects.all()
    serializer_class = ItemsModelSerializer
    parser_classes = (MultiPartParser, FileUploadParser)

    @action(methods=['POST'], detail=True)
    def post(self, request, filename):
        instance=self.get_object()
        print("im here")
        file_obj = request.data['file']
        serializer = ItemsModelSerializer(data=request.data, files=request.file.get('image'))
        if(serializer.is_valid):
            serializer.save
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else :
            return HttpResponse("failed")