from rest_framework import permissions
from TestAPI.models import Test, Question


class UserPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj=None):
        return obj == request.user


class TestPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj=None):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user


class QuestionPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return Test.objects.get(id=obj.test.id).author == request.user


class AnswerPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return Test.objects.get(id=Question.objects.get(id=obj.question.id).test.id).author == request.user


class UserTestPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user


class UserAnswerPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user
