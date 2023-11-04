from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProdudoSerializer
from rest_framework import status

from .models import Produto


@api_view(["GET", "POST"])
def apiOverview(request):
    if request.method == "GET":
        try:
            produto = Produto.objects.all().order_by("-id")
            serializer = ProdudoSerializer(produto, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except KeyError:
            return Response({"error": KeyError}, status=status.HTTP_404_NOT_FOUND)
    elif request.method == "POST":
        serializer = ProdudoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(
            {"error": "Produto não cumpriu os requisitos"},
            status=status.HTTP_404_NOT_FOUND,
        )


@api_view(["GET", "PUT", "DELETE"])
def apiController(request, slug):
    try:
        produto = Produto.objects.get(id=slug)
    except Produto.DoesNotExist:
        return Response(
            {"error": "Produto does not exist"}, status=status.HTTP_404_NOT_FOUND
        )

    if request.method == "GET":
        serializer = ProdudoSerializer(produto)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == "DELETE":
        produto.delete()
        return Response(
            {"produto excluído": f"{produto}"}, status=status.HTTP_204_NO_CONTENT
        )

    elif request.method == "PUT":
        serializer = ProdudoSerializer(produto, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(
            {"error": "Produto não cumpriu os requisitos"},
            status=status.HTTP_404_NOT_FOUND,
        )
