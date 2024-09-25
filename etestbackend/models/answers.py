from django.db import models
from .questions import Question
from utils.utils import UpdateCreateDate


class Answer(UpdateCreateDate):
    class Meta:
        app_label = "quiz"

    """
    Defines a Answers Models that stores Answers information in the databases

    fields:
        id: auto generated id
        answer_text: text to be display as answer
        question: a foreign key to the question models link the answer to the question it belongs to
        is_right: a boolean field used to define the correct answer


    """

    answer_text = models.CharField(max_length=200, verbose_name="Answer", null=True)
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name="Question_answers"
    )
    is_right = models.BooleanField(default=False)

    def __str__(self):
        return self.answer_text
