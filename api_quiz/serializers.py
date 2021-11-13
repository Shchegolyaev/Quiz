from rest_framework import serializers

from .models import Answer, Choice, Question, Quiz


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = []


class ChoiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Choice
        fields = ['text', 'question']


class QuestionsSerializer(serializers.ModelSerializer):
    choice = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ['question_text', 'choice']


class QuizSerializer(serializers.ModelSerializer):
    question = QuestionsSerializer(many=True, read_only=True)

    class Meta:
        model = Quiz
        fields = ['name', 'date_end', 'description', 'question']
