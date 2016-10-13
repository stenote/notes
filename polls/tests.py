import datetime

from django.utils import timezone
from django.test import TestCase
from django.urls import reverse

from .models import Question

# Create your tests here.

def create_question(question_text, days):

    time = timezone.now() + datetime.timedelta(days=days)

    # 如果直接 Question(question_test=question_text, pub_date=time), 就无法正常 Question.objects 进行 filter 了
    return Question.objects.create(question_text=question_text, pub_date=time)

class QuestionMethodTests(TestCase):
    
    def test_was_published_recently_with_future_question(self):
        
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        time = timezone.now() - datetime.timedelta(hours=1)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)

class QuestionViewTest(TestCase):

    def test_index_view_with_no_question(self):

        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_index_view_with_future_question_and_past_question(self):

        create_question(question_text='Past question.', days=-30)
        create_question(question_text='Future question', days=30)
        response = self.client.get(reverse('polls:index'))

        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question.>']
        )

    def test_index_view_with_two_past_questions(self):
        create_question(question_text="Past question 1.", days=-30)
        create_question(question_text="Past question 2.", days=-5)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question 2.>', '<Question: Past question 1.>']
        )
