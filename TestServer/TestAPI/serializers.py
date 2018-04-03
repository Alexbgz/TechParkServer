from TestAPI.models import Test, Question, Answer, UserTest, UserAnswer
from rest_framework import serializers


class TestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Test
        fields = ('id', 'author', 'title', 'description', 'image', 'date')


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'test', 'question_text', 'correct_answer')


class AnswerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Answer
        fields = ('id', 'question', 'answer_text')


class UserTestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserTest
        fields = ('id', 'user', 'test', 'score')


class UserAnswerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserAnswer
        fields = ('id', 'user', 'question', 'answer')
