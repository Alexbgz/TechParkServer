from TestAPI.models import Test, Question, Answer, UserTest, UserAnswer
from rest_framework import serializers
from django.contrib.auth.models import User


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name')


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name')
        write_only_fields = ('password',)
        read_only_fields = ('id',)

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
        return super(UserCreateSerializer, self).update(instance, validated_data)


class TestCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ('id', 'title', 'description', 'image', 'date')

    def pre_save(self, obj):
        """Force author to the current user on save"""
        obj.author = self.request.user
        return obj


class TestSerializer(serializers.ModelSerializer):
    # author = serializers.HyperlinkedRelatedField(read_only=True, view_name='user-detail', lookup_field='username')
    author = UserDetailSerializer()

    class Meta:
        model = Test
        fields = ('id', 'author', 'title', 'description', 'image', 'date')


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'test', 'question_text', 'correct_answer')


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('id', 'question', 'answer_text')


class UserTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTest
        fields = ('id', 'user', 'test', 'score')


class UserAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAnswer
        fields = ('id', 'user', 'question', 'answer')
