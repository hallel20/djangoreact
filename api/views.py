from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet, generics
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.authtoken.models import Token
from .models import Property, AgentProfile, Comment
from .serializers import PropertySerializer, CommentSerializer, UserSerializer, RegisterSerializer, AgentProfileSerializer
from .permissions import IsAdminOrReadOnly

# from rest_framework.authentication import TokenAuthentication, SessionAuthentication
# Create your views here.


def home(request):
    return render(request, 'index.html')


def json(request):
    return render(request, 'manifest.json')


class PropertyView(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

    # authentication_classes = (TokenAuthentication)


class CommentView(ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = CommentSerializer

    def get_queryset(self):
        queryset = Comment.objects.all()
        if self.request.method == 'GET':
            url_property_id = self.request.query_params.get('property_id')
            if url_property_id is not None:
                queryset = queryset.filter(property_id=url_property_id)
            return queryset
        return queryset


class UserView(ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = UserSerializer

    authentication_classes = [TokenAuthentication]


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class AgentView(ModelViewSet):
    queryset = AgentProfile.objects.all()
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = AgentProfileSerializer
