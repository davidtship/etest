from rest_framework import serializers
from django.shortcuts import get_object_or_404

from datetime import datetime

from models.quizscores import QuizScore
from models.quizanswers import QuizAnswers
from models.drivers import Driver


from .driversSerializers import DriverSerializer
from .answersSerializers import AnswersSerializer
from .medicalinfoSerializers import DriverMedicalInfoSerializer


from ..tasks import sendSMS


class QuizAnswersSerializer(serializers.ModelSerializer):
    """
    A DriverAnswersSerilizer serializer used to serializes returned or selected or response from the driver during the test

    returned field:
        [all]

    Views:
        quiz.views.DriverQuizAnswersSerializer

    Embeded in:
        quiz.views.QuizScoreWithAnswersSerializer
    """

    class Meta:
        model = QuizAnswers
        fields = "__all__"


class DriverDetailsAnswersSerializer(serializers.ModelSerializer):
    question = serializers.StringRelatedField()
    answer = AnswersSerializer()

    class Meta:
        model = QuizAnswers
        fields = "__all__"


class QuizScoreSerializer(serializers.ModelSerializer):
    """
    A QuizScoreSerializer serializer used to serializes QuizScore data Model
    returned field:
        [all]

    Views:
        quiz.views.QuizScoreViewSet

    Embeded in:
    """

    class Meta:
        model = QuizScore
        fields = "__all__"

    def create(self, validated_data):
        validated = validated_data
        print(validated["driver"].phone)
        sendSMS.delay(
            address=str(validated["driver"].phone),
            message=f"Bienvenu à SolutestRDC, votre test est prevu pour {validated['schedule_on']} ",
        )
        site = self.context["request"].user.site
        quizscore = QuizScore.objects.create(**validated, site=site)
        return quizscore


class QuizScoreWithDriverEmbeddedSerializer(serializers.ModelSerializer):
    """
    A QuizScoreDriverSerializer serializer used to serializes QuizScore Model
    and embbed drivers info using the DriverSerializer

    returned field:
        ["id", "test_type", "schedule_on", "taken", "score", "driver"]
        driver is a nested serializer from AnswersSerializer

    Views:
        quiz.views.QuizScoreDriverViewSet

    Embeded in:
    """

    driver = DriverSerializer()

    class Meta:
        model = QuizScore
        fields = ["id", "test_type", "schedule_on", "taken", "score", "driver"]


class QuizScoreWithAnswersSerializer(serializers.ModelSerializer):
    """
    A QuizScoreWithAnswersSerializer serializer used to serializes the score with all related information,
    used mostly for Post after user test completed

    returned field:
         [
            "id",
            "driver",
            "test_type",
            "schedule_on",
            "taken",
            "score",
            "quiz_score_answers",
        ]
        quiz_score_answers are answers returned by test taker

    Views:
        quiz.views.QuizScoreWithAnswersViewSet

    Embeded in:
    """

    quiz_score_answers = QuizAnswersSerializer(many=True)
    id = serializers.IntegerField()

    class Meta:
        model = QuizScore
        fields = [
            "id",
            "driver",
            "test_type",
            "schedule_on",
            "taken",
            "site",
            "score",
            "quiz_score_answers",
        ]

    # A override he create method to save nested serializers

    def create(self, validated_data):
        validated = validated_data
        answers = validated_data.pop("quiz_score_answers")

        print(f"answers {answers}")

        quiz_score = get_object_or_404(QuizScore, pk=validated["id"])
        quiz_score.score = validated["score"]
        quiz_score.taken = True

        nl = "\n"

        sendSMS.delay(
            address=str(quiz_score.driver.phone),
            message=f'Cher {quiz_score.driver.first_name}, le score de votre test {"Théorique" if validated["test_type"]=="Th" else "Pratique"} est de {validated["score"]}%.{nl} www.solutechrdc.com',
        )
        quiz_score.save()
        print(quiz_score)

        for answer in answers:
            QuizAnswers.objects.create(**answer)

        return quiz_score


class DriverDetailScoreWithAnswersSerializer(serializers.ModelSerializer):
    quiz_score_answers = DriverDetailsAnswersSerializer(many=True)
    id = serializers.IntegerField()

    class Meta:
        model = QuizScore
        fields = [
            "id",
            "driver",
            "test_type",
            "schedule_on",
            "taken",
            "score",
            "site",
            "quiz_score_answers",
        ]

    def create(self, validated_data):
        validated = validated_data
        answers = validated_data.pop("quiz_score_answers")

        quiz_score = get_object_or_404(QuizScore, pk=validated["id"])
        quiz_score.score = validated["score"]
        quiz_score.taken = True

        quiz_score.save()
        print(quiz_score)

        for answer in answers:
            print(answer)
            QuizAnswers.objects.create(**answer, quizscore=quiz_score)

        return quiz_score


class DriverDetailsSerializers(serializers.ModelSerializer):
    driver_score = DriverDetailScoreWithAnswersSerializer(many=True)
    Driver_medical = DriverMedicalInfoSerializer()

    class Meta:
        model = Driver
        fields = [
            "id",
            "form_number",
            "licence_type",
            "phone",
            "email",
            "first_name",
            "middle_name",
            "last_name",
            "driver_nationality",
            "driver_identity_document",
            "driver_identity_document_number",
            "place_birth",
            "date_of_birth",
            "sex",
            "adress_number",
            "adress_street",
            "adress_area",
            "adress_township",
            "city",
            "state",
            "country",
            "profile_pic",
            "registration_form",
            "driving_school_certificate",
            "driver_score",
            "Driver_medical",
        ]
