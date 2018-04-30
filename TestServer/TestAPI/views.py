from django.contrib.auth.models import User
from rest_framework import generics, permissions, parsers
from TestAPI.models import Test, Question, Answer, UserTest, UserAnswer
from TestAPI.serializers import UserCreateSerializer, UserDetailSerializer, TestSerializer, QuestionSerializer, \
    AnswerSerializer, UserTestSerializer, UserTestCreateSerializer,  UserAnswerSerializer, UserAnswerCreateSerializer
from TestAPI.permissions import UserPermission, TestPermission, QuestionPermission, AnswerPermission, \
    UserTestPermission, UserAnswerPermission


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


class TestListCreate(generics.ListCreateAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    parser_classes = (parsers.JSONParser, parsers.MultiPartParser, parsers.FormParser,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        serializer.save(author=self.request.user)


class TestDetailUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    permission_classes = [
        TestPermission
    ]
    lookup_field = 'id'
    parser_classes = (parsers.JSONParser, parsers.MultiPartParser, parsers.FormParser,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        serializer.save(author=self.request.user)


class QuestionCreate(generics.CreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [
        permissions.IsAuthenticated
    ]


class QuestionList(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [
        permissions.AllowAny
    ]
    lookup_field = 'test'


class QuestionUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [
        QuestionPermission
    ]
    lookup_field = 'id'


class AnswerCreate(generics.CreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [
        permissions.IsAuthenticated
    ]


class AnswerList(generics.ListAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [
        permissions.AllowAny
    ]
    lookup_field = 'question'


class AnswerUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [
        AnswerPermission
    ]
    lookup_field = 'id'


class UserTestCreate(generics.CreateAPIView):
    queryset = UserTest.objects.all()
    serializer_class = UserTestCreateSerializer
    permission_classes = [
        permissions.IsAuthenticated
    ]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


class UserTestList(generics.ListAPIView):
    queryset = UserTest.objects.all()
    serializer_class = UserTestSerializer
    permission_classes = [
        permissions.AllowAny
    ]

    def get_queryset(self):
        queryset = super(UserTestList, self).get_queryset()
        try:
            return queryset.filter(user=User.objects.get(username=self.kwargs.get('username')).id)
        except Exception:
            return []


class UserTestUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserTest.objects.all()
    serializer_class = UserTestCreateSerializer
    permission_classes = [
        UserTestPermission
    ]
    lookup_field = 'id'

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


class UserAnswerCreate(generics.CreateAPIView):
    queryset = UserAnswer.objects.all()
    serializer_class = UserAnswerCreateSerializer
    permission_classes = [
        permissions.IsAuthenticated
    ]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


class UserAnswerList(generics.ListAPIView):
    queryset = UserAnswer.objects.all()
    serializer_class = UserAnswerSerializer
    permission_classes = [
        permissions.AllowAny
    ]

    def get_queryset(self):
        queryset = super(UserAnswerList, self).get_queryset()
        try:
            return queryset.filter(user=User.objects.get(username=self.kwargs.get('username')).id)
        except Exception:
            return []


class UserAnswerUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserAnswer.objects.all()
    serializer_class = UserAnswerCreateSerializer
    permission_classes = [
        UserAnswerPermission
    ]
    lookup_field = 'id'

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)