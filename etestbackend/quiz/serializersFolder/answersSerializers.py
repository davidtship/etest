from models.answers import Answer
from rest_framework import serializers


class AnswersSerializer(serializers.ModelSerializer):
    """
    A AnswersSerializer serializer used to serialzes Answer model data before saving in db

    returned field:
        ["id", "answer_text", "is_right", "question"]

    Views:
        quiz.views.AnswersViewSet

    Imbeded in:
        quiz.serializers.QuizSerializer
    """

    class Meta:
        model = Answer
        fields = ["id", "answer_text", "is_right", "question"]
