# blogging/models.py
from django.db import models

# from blogging.models import Post


class Poll(models.Model):
    title = models.CharField(max_length=128)
    text = models.TextField(blank=True)
    score = models.IntegerField(default=0)
    posts = models.ManyToManyField("blogging.Post", blank=True, related_name="polls")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "polls"


# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')
#     def __str__(self):
#         return self.question_text
#
#
# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)
