from rest_framework import serializers
from users.models import User





class GetUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
             'username',
             'first_name',
             'last_name',
             'about',
             'email',
             'date_joined',
             'phone_number',
         ]