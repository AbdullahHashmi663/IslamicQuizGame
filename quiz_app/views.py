from django.shortcuts import render, get_object_or_404, redirect
from .models import Quiz, Question, Answer, QuizAttempt
from django.utils import timezone
import random

# Create your views here.

def quiz_list(request):
    quizzes = Quiz.objects.all()
    return render(request, 'quiz_app/quiz_list.html', {'quizzes': quizzes})

def quiz_detail(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    questions = Question.objects.filter(quiz=quiz)
    return render(request, 'quiz_app/quiz_detail.html', {'quiz': quiz, 'questions': questions})

def landing(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        contact = request.POST.get('contact')
        if name and contact:
            request.session['user_name'] = name
            request.session['user_contact'] = contact
            return redirect('quiz_start')
    return render(request, 'quiz_app/landing.html')

def quiz_start(request):
    all_questions = list(Question.objects.all())
    used_question_ids = request.session.get('used_question_ids', [])
    available_questions = [q for q in all_questions if q.id not in used_question_ids]

    # If not enough new questions, reset history
    if len(available_questions) < 10:
        used_question_ids = []
        available_questions = all_questions

    questions = random.sample(available_questions, 10) if len(available_questions) >= 10 else available_questions
    question_ids = [q.id for q in questions]

    # Update session history
    request.session['used_question_ids'] = used_question_ids + question_ids
    request.session['quiz_question_ids'] = question_ids
    request.session['quiz_start_time'] = timezone.now().isoformat()
    return render(request, 'quiz_app/quiz_play.html', {'questions': questions, 'timer': 45})

def quiz_submit(request):
    if request.method == 'POST':
        question_ids = request.session.get('quiz_question_ids', [])
        user_name = request.session.get('user_name', '')
        user_contact = request.session.get('user_contact', '')
        answers_feedback = {}
        correct = 0
        for qid in question_ids:
            selected = request.POST.get(f'question_{qid}')
            question = Question.objects.get(id=qid)
            correct_answer_obj = Answer.objects.filter(question=question, is_correct=True).first()
            correct_answer_id = str(correct_answer_obj.id) if correct_answer_obj else None
            correct_answer_text = correct_answer_obj.text if correct_answer_obj else ''
            is_correct = (selected == correct_answer_id)
            if is_correct:
                correct += 1
            answers_feedback[str(qid)] = {
                'question': question.text,
                'selected': selected,
                'correct': is_correct,
                'correct_answer': correct_answer_text,
                'selected_text': Answer.objects.get(id=selected).text if selected else '',
            }
        result = 'Win' if correct >= 9 else 'Lose'
        # Store attempt
        QuizAttempt.objects.create(
            user_name=user_name,
            user_contact=user_contact,
            score=correct,
            result=result,
            answers=answers_feedback
        )
        # Calculate time taken
        quiz_start_time = request.session.get('quiz_start_time')
        if quiz_start_time:
            from django.utils.dateparse import parse_datetime
            start = parse_datetime(quiz_start_time)
            if start and timezone.is_naive(start):
                start = timezone.make_aware(start)
            now = timezone.now()
            time_taken = int((now - start).total_seconds())
        else:
            time_taken = 0
        request.session['quiz_score'] = correct
        request.session['quiz_result'] = result
        request.session['quiz_feedback'] = answers_feedback
        request.session['quiz_time_taken'] = time_taken
        # Bonus awarded
        bonus_awarded = request.POST.get('bonus_awarded', '0') == '1'
        request.session['quiz_bonus_awarded'] = bonus_awarded
        return redirect('quiz_result')
    return redirect('quiz_start')

def quiz_result(request):
    score = request.session.get('quiz_score', 0)
    result = request.session.get('quiz_result', 'Lose')
    feedback = request.session.get('quiz_feedback', {})
    time_taken = request.session.get('quiz_time_taken', 0)
    bonus_awarded = request.session.get('quiz_bonus_awarded', False)
    return render(request, 'quiz_app/quiz_result.html', {'score': score, 'result': result, 'feedback': feedback, 'time_taken': time_taken, 'bonus_awarded': bonus_awarded})
