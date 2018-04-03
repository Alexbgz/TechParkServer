from django.contrib import admin
from TestAPI.models import Test, Question, Answer, UserTest, UserAnswer


class PostTest(admin.ModelAdmin):
    list_display = ('id', 'author', 'title', 'description', 'image', 'date')


admin.site.register(Test, PostTest)


class PostQuestion(admin.ModelAdmin):
    list_display = ('id', 'test', 'question_text', 'correct_answer')


admin.site.register(Question, PostQuestion)


class PostAnswer(admin.ModelAdmin):
    list_display = ('id', 'question', 'answer_text')


admin.site.register(Answer, PostAnswer)


class PostUserTest(admin.ModelAdmin):
    list_display = ('id', 'user', 'test', 'score')


admin.site.register(UserTest, PostUserTest)


class PostUserAnswer(admin.ModelAdmin):
    list_display = ('id', 'user', 'question', 'answer')


admin.site.register(UserAnswer, PostUserAnswer)
