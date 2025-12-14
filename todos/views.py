from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics, viewsets, mixins
from django.core.paginator import Paginator
from .models import Todo
from .serializers import TodoSerializer
from programmers.serializers import ProgrammerSerializer


class TodoRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoListCreateAPIView(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoAPIViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


@api_view(["GET"])
def todo_paginate(request):
    todos = Todo.objects.all()
    paginator = Paginator(todos, 2)

    page_number = request.GET.get("page")

    if not page_number:
        return Response({"error": "page param required"}, status=400)

    if int(page_number) > paginator.num_pages:
        return Response({"error": f"max page is {paginator.num_pages}"}, status=400)

    page = paginator.get_page(page_number)

    return Response({
        "page": page_number,
        "total_pages": paginator.num_pages,
        "results": TodoSerializer(page.object_list, many=True).data
    })


@api_view(["GET"])
def todo_programmers(request, todo_id):
    try:
        task = Todo.objects.get(id=todo_id)
    except Todo.DoesNotExist:
        return Response({"error": "Task not found"}, status=404)

    programmers = task.programmers.all()
    return Response({
        "todo_id": todo_id,
        "programmers": ProgrammerSerializer(programmers, many=True).data
    })

