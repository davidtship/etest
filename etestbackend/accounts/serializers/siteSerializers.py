from models.sites import Site
from rest_framework import serializers


class SiteSerializer(serializers.ModelSerializer):
    """
    A SiteSerializer serializer used to serialzes Site model data before saving in db

    returned field:
        ["id", "answer_text", "is_right", "question"]

    Views:
        quiz.views.AnswersViewSet

    Imbeded in:
    """

    class Meta:
        model = Site
        fields = "__all__"
