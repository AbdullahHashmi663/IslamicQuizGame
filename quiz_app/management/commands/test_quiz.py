from django.core.management.base import BaseCommand
from quiz_app.models import Quiz, Question, Answer

class Command(BaseCommand):
    help = "Test quiz command"

    def handle(self, *args, **kwargs):
        self.stdout.write("Testing quiz command...")
        quiz = Quiz.objects.create(
            title="Test Quiz",
            description="A test quiz"
        )
        question = Question.objects.create(
            quiz=quiz,
            text="What is 2+2?"
        )
        Answer.objects.create(
            question=question,
            text="4",
            is_correct=True
        )
        Answer.objects.create(
            question=question,
            text="5",
            is_correct=False
        )
        self.stdout.write(self.style.SUCCESS("Test quiz created successfully!")) 