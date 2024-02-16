from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
# from rest_framework.authtoken.views import Token
from rest_framework.authtoken.models import Token
from .models import Property, AgentProfile, Comment


class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = ['id', 'name', 'location', 'price',
                  'image_1', 'image_2', 'image_3', 'city', 'district', 'no_of_beds', 'no_of_garages', 'no_of_baths', 'property_type', 'rating', 'description', 'area', 'sold', 'agent']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'property_id',
                  'first_name', 'last_name', 'date_added', 'comment']

        extra_kwargs = {'date_added': {
            'read_only': True,
        }}

        def create(self, validated_data, request):
            user_id = Token.objects.get(key=request.auth.key).user_id
            user = User.objects.get(id=user_id)
            first_name = user.first_name
            last_name = user.last_name
            comment = Comment.objects.create(
                first_name=first_name,
                last_name=last_name,
                property_id=validated_data['property_id'],
                comment=validated_data['comment']
            )
            print(validated_data['property_id'])
            return comment


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'first_name', 'last_name']

        extra_kwargs = {'password': {
            'write_only': True,
            'required': True
        }}

        def create(self, validated_data):
            user = User.objects.create_user(**validated_data)
            user_token = Token.objects.create(user=user)
            return user, user_token


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(
            queryset=User.objects.all(), message="Email Already Used!")]
    )

    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('password', 'password2', 'username',
                  'email', 'first_name', 'last_name')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'],
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user


class AgentProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgentProfile
        fields = ['first_name', 'last_name',
                  'phone', 'email', 'facebook', 'instagram', 'about', 'image']
