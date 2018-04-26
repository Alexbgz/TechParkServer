from django.contrib.auth.models import User
from rest_framework import generics, permissions, parsers
from TestAPI.models import Test, Question, Answer, UserTest, UserAnswer
from TestAPI.serializers import \
    UserCreateSerializer, UserDetailSerializer,  \
    TestCreateSerializer, TestSerializer,\
    QuestionSerializer, \
    AnswerSerializer, UserTestSerializer, UserAnswerSerializer
from TestAPI.permissions import UserPermission


class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    permission_classes = [
        permissions.AllowAny
    ]


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    lookup_field = 'username'
    permission_classes = [
        permissions.AllowAny
    ]


class UserUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    lookup_field = 'username'
    permission_classes = [
        UserPermission
    ]


class TestCreate(generics.CreateAPIView):
    queryset = Test.objects.all()
    serializer_class = TestCreateSerializer
    permission_classes = [
        permissions.IsAuthenticated
    ]
    parser_classes = (parsers.JSONParser, parsers.MultiPartParser, parsers.FormParser,)


class TestList(generics.ListAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    permission_classes = [
        permissions.AllowAny
    ]


class TestDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    lookup_field = 'id'


class TestUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    lookup_field = 'id'
