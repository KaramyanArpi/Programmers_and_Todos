from rest_framework import serializers
from programmers.models import Programmer


class ProgrammerSerializer(serializers.ModelSerializer):
        class Meta:
            model = Programmer
            fields = ['id', 'name', 'surname', 'experience', 'todos_ids']
