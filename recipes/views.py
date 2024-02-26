from rest_framework import viewsets
from .models import Image, Ingredient, IngredientType, Recipe
from .serializers import (
    ImageSerializer,
    IngredientSerializer,
    IngredientTypeSerializer,
    RecipeSerializer,
)
from rest_framework import status
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import FileUploadSerializer


class RecipeViewSet(viewsets.ModelViewSet):
    """
    This class provide `list`, `create`, `update`, `retreive`
    and `delete` actions for recipe
    """

    queryset = Recipe.objects.prefetch_related("ingredients").order_by(
        "-created_at", "-id"
    )
    serializer_class = RecipeSerializer


class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer


class IngredientTypeViewSet(viewsets.ModelViewSet):
    queryset = IngredientType.objects.all()
    serializer_class = IngredientTypeSerializer


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class FileUploadAPIView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = FileUploadSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            # you can access the file like this from serializer
            # uploaded_file = serializer.validated_data["file"]
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
