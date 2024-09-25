from django.db import models
from utils.utils import UpdateCreateDate


class Category(UpdateCreateDate):
    """
    Define a Category Model is used to store categories to which a question belong to
    category can be as an example: 'signalisation' as it only field which is name.


    return self.name

    """

    name = models.CharField(max_length=255, verbose_name="Category_name")

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        app_label = "quiz"
        verbose_name_plural = "Categories"
