from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["POST"])
def login(request) -> Response:
    return Response({})


@api_view(["POST"])
def signup(request) -> Response:
    return Response({})


@api_view(["POST"])
def validate_token(request) -> Response:
    return Response({})