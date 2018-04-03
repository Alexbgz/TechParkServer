from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from TestAPI.models import Test, Question, Answer, UserTest, UserAnswer
from TestAPI.serializers import TestSerializer, QuestionSerializer, AnswerSerializer, UserTestSerializer, UserAnswerSerializer


class TestList(APIView):
    def get(self, request, format=None):
        tests = Test.objects.all()
        serializer_context = {
            'request': request,
        }
        serializer = TestSerializer(tests, context=serializer_context, many=True)
        return Response(serializer.data)
