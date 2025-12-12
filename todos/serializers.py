from rest_framework import serializers
from todos.models import Todo
from programmers.models import Programmer
from programmers.serializers import ProgrammerSerializer


class TodoSerializer(serializers.ModelSerializer):
    programmers = ProgrammerSerializer(many=True, read_only=True)
    programmers_ids = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset= Programmer.objects.all(),
        write_only=True
    )

    class Meta:
        model = Todo
        fields = ['id', 'task', 'is_done', 'deadline', 'programmers_ids']

