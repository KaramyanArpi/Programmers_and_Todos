from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics, viewsets, mixins
from django.core.paginator import Paginator

from .models import Programmer
from .serializers import ProgrammerSerializer
from todos.serializers import TodoSerializer


class ProgrammerRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Programmer.objects.all()
    serializer_class = ProgrammerSerializer


class ProgrammerListCreateAPIView(generics.ListCreateAPIView):
    queryset = Programmer.objects.all()
    serializer_class = ProgrammerSerializer


class ProgrammerAPIViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Programmer.objects.all()
    serializer_class = ProgrammerSerializer


class ProgrammerViewSet(viewsets.ModelViewSet):
    queryset = Programmer.objects.all()
    serializer_class = ProgrammerSerializer


@api_view(["GET"])
def programmer_paginate(request):
    programmers = Programmer.objects.all()
    paginator = Paginator(programmers, 2)

    page_number = request.GET.get("page")

    if not page_number:
        return Response({"error": "page param required"}, status=400)

    if int(page_number) > paginator.num_pages:
        return Response({"error": f"max page is {paginator.num_pages}"}, status=400)

    page = paginator.get_page(page_number)

    return Response({
        "page": page_number,
        "total_pages": paginator.num_pages,
        "results": ProgrammerSerializer(page.object_list, many=True).data
    })


@api_view(["GET"])
def programmer_todos(request, programmer_id):
    try:
        programmer = Programmer.objects.get(id=programmer_id)
    except Programmer.DoesNotExist:
        return Response({"error": "Programmer not found"}, status=404)

    tasks = programmer.todos.all()
    return Response({
        "programmer_id": programmer_id,
        "tasks": TodoSerializer(tasks, many=True).data
    })
