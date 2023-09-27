from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny

from mentors.models import Ustoz, Mijoz
from mentors.serializers import UstozSerializer, MijozSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'result': data
        })


class UstozCreateListApiView(ListCreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UstozSerializer
    queryset = Ustoz.objects.all()
    pagination_class = CustomPagination


class UstozRetrieveUpdateDeleteApiView(RetrieveUpdateDestroyAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UstozSerializer
    queryset = Ustoz.objects.all()


class MijozCreateListApiView(ListCreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = MijozSerializer
    queryset = Mijoz.objects.all()
    pagination_class = CustomPagination


class MijozRetrieveUpdateDeleteApiView(RetrieveUpdateDestroyAPIView):
    permission_classes = (AllowAny,)
    serializer_class = MijozSerializer
    queryset = Mijoz.objects.all()
