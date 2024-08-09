from rest_framework import serializers
from home_rental.models import AddRentalHome, UserInformation

class AddRentalHomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddRentalHome
        fields = [
            'id',
            'First_Name',
            'Last_Name',
            'Email',
            'Street1',
            'Street2',
            'City',
            'State',
            'Pincode',
            'Contact',
            'Visiting_Start',
            'Visiting_End',
            'Gate_closing_time',
            'Feature1',
            'Feature2',
            'Visiting_day',
            'Rent',
            'Number_Of_People_Allowed',
            'Description',
            'Image',
            'slug'
        ]

class UserInformationSerializer(serializers.ModelSerializer):
    rental_home = AddRentalHomeSerializer(read_only=True)

    class Meta:
        model = UserInformation
        fields = [
            'id',
            'rental_home',
            'name',
            'email',
            'phone',
            'address'
        ]
