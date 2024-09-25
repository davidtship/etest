from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter


from .views.categoryViews import CategoryDetailViewSet
from .views.answerView import AnswersViewSet
from .views.questionViews import QuestionsViewSet, QuestionsWithOptionViewSet

from .views.driverViews import DriverInfoViewSet, DriverDetailsViewSet
from .views.quizScoreviews import (
    DriverAnsweredQuizDetailViewSet,
    QuizScoreWithDriverEmbeddedViewSet,
    QuizScoreWithAnswersEmbbededViewSet,
    QuizScoreViewSet,
)

from .views.quizViews import QuizViewSet

from .views.driverViews import DriverMedicalInfoViewSet


router = DefaultRouter()

"""Questions and aswers URLs"""
router.register("categories", CategoryDetailViewSet, basename="category-list")
router.register("answers", AnswersViewSet, basename="answers")
router.register("questions", QuestionsViewSet, basename="questions")
<<<<<<< HEAD
router.register("questions-options", QuestionsWithOptionViewSet, basename="questions")
=======
router.register("questions-options", QuestionsWithOptionViewSet, basename="questions-options")
>>>>>>> fixing bugs


"""Drivers Urls"""
router.register("drivers", DriverInfoViewSet, basename="drivers")


"""Test or Quiz"""
router.register("quiz", QuizViewSet, basename="quiz")


"""Embedded views"""
router.register(
    "quiz-score-driver",
    QuizScoreWithDriverEmbeddedViewSet,
    basename="quiz-score-driver",
)

router.register(
    "quiz-score-answers",
    QuizScoreWithAnswersEmbbededViewSet,
    basename="quiz-answers",
)

router.register(
    "driver-quiz-answers",
    DriverAnsweredQuizDetailViewSet,
    basename="driver-quiz-answers",
)

"""Consummed as GET To return all driver related datas embedded"""
router.register(
    "driver-details",
    DriverDetailsViewSet,
    basename="driver-details",
)

"""GET,POST used to upload medical information"""
router.register("drivers-medical", DriverMedicalInfoViewSet, basename="driver-medical")


"""GET,POST creating new Test score"""
router.register("quiz-score", QuizScoreViewSet, basename="user-quiz-score")


urlpatterns = [
    path("", include(router.urls)),
]
