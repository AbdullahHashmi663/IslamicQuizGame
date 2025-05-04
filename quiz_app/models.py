from django.db import models
from django.utils import timezone

# Create your models here.

class Quiz(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    text = models.CharField(max_length=500)

    def __str__(self):
        return self.text

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text

class QuizAttempt(models.Model):
    user_name = models.CharField(max_length=100)
    user_contact = models.CharField(max_length=50)
    score = models.IntegerField()
    result = models.CharField(max_length=10)
    timestamp = models.DateTimeField(default=timezone.now)
    answers = models.JSONField()  # {question_id: {'selected': answer_id, 'correct': bool, 'correct_answer': answer_text}}

    def __str__(self):
        return f"{self.user_name} - {self.score} - {self.result} @ {self.timestamp}"
