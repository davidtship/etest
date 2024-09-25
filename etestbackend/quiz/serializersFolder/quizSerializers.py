from rest_framework import serializers
from .answersSerializers import AnswersSerializer

from models.questions import Question


class QuizSerializer(serializers.ModelSerializer):
    """
    A QuizSerializer used to return a quiz of questions to the users

    returned field:
        ["id", "title", "picture", "is_active", "Question_answers"]
        Question_answers is a nested serializer from AnswersSerializer

    Views:
        quiz.views.QuizViewSet

    Embeded in:
        quiz.serializers.QuizSerializer
    """

    Question_answers = AnswersSerializer(many=True)

    class Meta:
        model = Question
        fields = ["id", "title", "picture", "category", "is_active", "Question_answers"]
