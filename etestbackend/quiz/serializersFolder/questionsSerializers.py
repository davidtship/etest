from rest_framework import serializers
from .answersSerializers import AnswersSerializer

from models.questions import Question
from .answersSerializers import AnswersSerializer


class QuestionSerializer(serializers.ModelSerializer):
    """
    A QuestionSerializer used to serialzes Question model data before saving in db

    returned field:
        id, title, is_ative, picture

    Views:
        quiz.views.QuestionsViewSet
    """

    class Meta:
        model = Question
        fields = [
            "id",
            "title",
            "is_active",
            "category",
            "picture",
        ]

    """

    def create(self, validated_data):
        validated = validated_data
        category = validated_data.pop("category")
        categoryInstance = Category.objects.create(**category)

        question_instance = Question.objects.create(
            **validated, category=categoryInstance
        )

        return question_instance
        
    """


class QuestionWithOptionSerializer(serializers.ModelSerializer):
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
