import os.path

from django.http import HttpResponse
from django.template.loader import render_to_string
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import serializers as sr
from wkhtmltopdf import wkhtmltopdf, RenderedFile
from django.template import Template, Context, loader
from . import serializers
from . import models
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from string import Template
# Create your views here.




class ChecksViewSet(ModelViewSet):
    serializer_class = serializers.CheckSerializer
    queryset = models.Check.objects.all()


    def list(self, request, *args, **kwargs):
        queryset = models.Check.objects.all()
        serializer_class = serializers.CheckSerializer(queryset, many=True)
        # path_to_file = os.path.realpath('../media/pdf/2_kitchen.pdf')
        # f = open(path_to_file, 'r')
        # myfile = File()
        return Response(serializer_class.data)

    def create(self, request, *args, **kwargs):
        serializer = serializers.OrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(self.serializer_class(self.queryset.filter(order=request.data), many=True).data,
                        status=status.HTTP_201_CREATED)


class CreateOrderView(APIView):
    serializer_class = serializers.OrderSerializer
    # queryset = models.Check.objects.all()




    def post(self, request):
        checks = serializers.OrderSerializer(data=request.data)
        if checks.is_valid():
            checks.save()
            return Response(status=201)

    def create(self, request, *args, **kwargs):
        point_id = request.POST.get('point_id')
        print(self.request.POST)
        print(point_id)

        serializer = serializers.CheckSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        print(serializer.data, 'SERIALIZER DATA')
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    #
    # def perform_create(self, serializer):
    #     x = serializer.save()
    #     print(x)
        # return super(CreateOrderView, self).perform_create(serializer)

    