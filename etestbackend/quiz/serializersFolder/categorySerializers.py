from models.categories import Category
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    """
    A category serializer used to serialzes Category model data before saving in db

    returned field:
        name: the name field of the Category model

    Views:
        quiz.views.CategoryDetailViewSet
    """

    class Meta:
        model = Category
        fields = "__all__"
