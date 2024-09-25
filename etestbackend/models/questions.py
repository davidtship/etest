from django.db import models

from .categories import Category
from utils.utils import UpdateCreateDate


class Question(UpdateCreateDate):
    """
    Defines a Question Models that stores Question information in the databases
    it return as __str__ question.id

    fields: id, title, is_active, picture

    picture is the illustration of the question if it exists. it can be null and or blank
    is_active field is used a flags to return the question in the view

    """

    class Meta:
        app_label = "quiz"

    title = models.CharField(max_length=1000, verbose_name="Question")
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="categories",
        null=True,
        blank=True,
    )

    is_active = models.BooleanField(default=True)
    picture = models.ImageField(
        upload_to="Questions_Illustration",
        blank=True,
        null=True,
        verbose_name="Question Picture",
    )

    def __str__(self):
        return f"{self.id}"
