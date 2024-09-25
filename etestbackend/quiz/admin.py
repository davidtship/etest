from django.contrib import admin

from models.sites import Site
from models.answers import Answer
from models.questions import Question
from models.quizanswers import QuizAnswers
from models.quizscores import QuizScore
from models.medicalinfos import MedicalInfo
from models.drivers import Driver
from models.categories import Category

# Register your models here.


class AnswersInline(admin.TabularInline):
    """
    Define an Answer Inline class that inherit from TablurInline
    an Inline is a class that can be embeded inside another admin class model to which it has Foreign Field
    used in:
        QuestionAdmin

    usage:
        class custAdmin(admin.ModelAdmin):
            inlines = [AnswersInline]
    """

    model = Answer


class QuestionAdmin(admin.ModelAdmin):
    """
    Define a quesstion Admin class that inherit from admin.ModelAdmin
    that can be registered inside the admin site.

    used in:
        admin site for create and updating questions
    usage:
        admin.site.register(Question, QuestionAdmin)
    """

    inlines = [AnswersInline]

    list_display = ["title", "is_active"]


class User_AnswerAdmin(admin.ModelAdmin):
    """
    Define an admin class that inherit from dmin.MofelAdmin which aare used to customize the dmin site

    """

    model = QuizAnswers

    list_display = ["quizscore", "question", "answer"]
    # readonly_fields = ["quizscore", "answer", "question"]


class DriverAdmin(admin.ModelAdmin):
    """
    Define an admin class that inherit from dmin.MofelAdmin which aare used to customize the dmin site

    """

    list_display = ["first_name", "first_name", "sex"]


class QuizScoreAdmin(admin.ModelAdmin):
    """
    Define an admin class that inherit from dmin.MofelAdmin which aare used to customize the dmin site

    """

    model = QuizScore

    list_display = ["driver", "test_type", "score", "schedule_on", "taken"]
    # readonly_fields = ["taken"]


class MedicalInfoAmin(admin.ModelAdmin):
    """
    Define an admin class that inherit from dmin.MofelAdmin which aare used to customize the dmin site

    """

    model = MedicalInfo

    list_display = ["driver", "medical_test"]


class CategoryAdmin(admin.ModelAdmin):
    """
    Define an admin class that inherit from dmin.MofelAdmin which aare used to customize the dmin site

    """

    model = Category

    list_display = ["name", "updated", "created"]


admin.site.register(Question, QuestionAdmin)
admin.site.register(QuizAnswers, User_AnswerAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Driver, DriverAdmin)
admin.site.register(QuizScore, QuizScoreAdmin)
admin.site.register(MedicalInfo, MedicalInfoAmin)
