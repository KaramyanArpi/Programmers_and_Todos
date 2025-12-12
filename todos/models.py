from django.db import models


class Todo(models.Model):
    task = models.CharField(max_length=80)
    is_done = models.BooleanField(default=False)
    deadline = models.DateField()
    programmers = models.ManyToManyField('programmers.Programmer', related_name='todos')

    def __str__(self):
        return f"{self.task}: {self.is_done} | {self.programmers}: {self.deadline}"

    class Meta:
        verbose_name = "Todo"
        verbose_name_plural = "Todos"
