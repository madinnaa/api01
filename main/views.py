from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from .models import *

from .serializers import StudentSerializer
from  rest_framework.response import Response
from .serializers import StudentSerializerviewsets
from django.shortcuts import get_list_or_404

class StudentView(ViewSet.Model.ViewSet):

    serializer_class = StudentSerializer
    queryset = Students.objects.all()

    # def list(self,request):
    #     queryset = Students.objects.all()
    #     serializer = StudentSerializer(queryset,many=True)
    #     return Response(serializer.data)
    
    # def retrieve(self, request, pk=None):
    #     queryset = Students.objects.all()
    #     user = StudentSerializer(queryset, pk=pk)
    #     serializer = StudentSerializer(user)
    #     return Response(serializer.data)