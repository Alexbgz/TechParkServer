from django.db import models

from django.contrib.auth.models import User


class Test(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(blank=True, upload_to='images')
    date = models.DateField(auto_now_add=True)


class Question(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=255)
    correct_answer = models.IntegerField()


class Answer(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=255)


class UserTest(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    score = models.IntegerField()


class UserAnswer(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
