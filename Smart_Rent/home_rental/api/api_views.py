from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from home_rental.models import AddRentalHome, UserInformation
from home_rental.api.serializer import AddRentalHomeSerializer, UserInformationSerializer

class AddRentalHomeViewSet(ViewSet):
    queryset = AddRentalHome.objects.all()

    def list(self, request):
        serializer = AddRentalHomeSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        rental_home = get_object_or_404(self.queryset, pk=pk)
        serializer = AddRentalHomeSerializer(rental_home)
        return Response(serializer.data)

    def create(self, request):
        serializer = AddRentalHomeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def update(self, request, pk=None):
        rental_home = get_object_or_404(self.queryset, pk=pk)
        serializer = AddRentalHomeSerializer(rental_home, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def partial_update(self, request, pk=None):
        rental_home = get_object_or_404(self.queryset, pk=pk)
        serializer = AddRentalHomeSerializer(rental_home, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        rental_home = get_object_or_404(self.queryset, pk=pk)
        rental_home.delete()
        return Response(status=204)


class UserInformationViewSet(ViewSet):
    queryset = UserInformation.objects.all()

    def list(self, request):
        serializer = UserInformationSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        user_info = get_object_or_404(self.queryset, pk=pk)
        serializer = UserInformationSerializer(user_info)
        return Response(serializer.data)

    def create(self, request):
        serializer = UserInformationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def update(self, request, pk=None):
        user_info = get_object_or_404(self.queryset, pk=pk)
        serializer = UserInformationSerializer(user_info, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def partial_update(self, request, pk=None):
        user_info = get_object_or_404(self.queryset, pk=pk)
        serializer = UserInformationSerializer(user_info, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        user_info = get_object_or_404(self.queryset, pk=pk)
        user_info.delete()
        return Response(status=204)
