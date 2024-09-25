from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.response import Response

from models.questions import Question
from models.categories import Category
from ..serializersFolder.quizSerializers import QuizSerializer


class QuizViewSet(viewsets.ModelViewSet):
    serializer_class = QuizSerializer
    queryset = Question.objects.all()
    http_method_names = ["get"]

    def list(self, request, *args, **kwargs):
        items = []

        categories = Category.objects.all()

        for cat in categories:
            qs = Question.objects.filter(category=cat).order_by("?")[:3]
            items += qs

        serializer = self.get_serializer(items, many=True)
        return Response(serializer.data)

    filterset_fields = ["id", "title"]
    search_fields = ["title"]
    ordering_fields = ["createdAt", "updateAt"]

    permission_classes = [permissions.IsAuthenticated]
