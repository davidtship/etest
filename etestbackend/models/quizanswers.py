from django.db import models
from django.core.exceptions import ValidationError


from .quizscores import QuizScore
from .questions import Question
from .answers import Answer

from utils.utils import UpdateCreateDate


class QuizAnswers(UpdateCreateDate):

    """
    Defines a QuizAnswers Models that stores Drivers Test's answers information in the databases
    This models is used to store references to the answers to which driver has responded or selected

    fields:
        id: auto generated id
        test_type: it hold two options be (th: Theory), (pr: Pratical)
        ....
        registration_form: used to store used filled form bought from the bank
        driving_school_certificate: used to store the user driving school certificate
        schedule_on: datetime when the driver should take is test
        passed_on: datetime whem the driver has finished the test
        score: driver score of after taking the test

        foreign fields:
            quizscore: reference the quizscore model which defines a test taken by the user
            question: refrence the question model
            answer: reference the answer model


    """

    class Meta:
        app_label = "quiz"

    quizscore = models.ForeignKey(
        QuizScore,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="quiz_score_answers",
    )
    question = models.ForeignKey(
        Question, null=True, blank=True, on_delete=models.SET_NULL
    )
    answer = models.ForeignKey(Answer, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self) -> str:
        return f"{self.quizscore}"

    """
        A method that insures that a instance of quizanswers can be only assign to a quizscore that is a theory
    """

    def clean(self):
        if self.quizscore.test_type != "Th":
            raise ValidationError("Quiz answer are for theory only")
