from django.db import models

# Create your models here.
class Poll(models.Model):
    question = models.CharField(max_length=200, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question

class Choice(models.Model):
    text = models.TextField(max_length=1000, blank=False, null=False)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name="choices")

    def __str__(self):
        return self.text[:20]


class Answer(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name="answers")
    created_at = models.DateTimeField(auto_now_add=True)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE, related_name="answer_choices")

