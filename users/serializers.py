from rest_framework import serializers
from users.models import User




# you can use from django_elasticsearch_dsl_drf.serializers import DocumentSerializer

class GetUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
             'username',
             'first_name',
             'last_name',
             'about',
             'email',
             'date_joined',
             'phone_number',
         ]