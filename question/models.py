from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    image = models.ImageField()
    html = models.TextField()
    script = models.TextField()
    video = models.FileField()
    audio = models.FileField()
    def __str__(self):
        return self.question_text

class Answers(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    ans_text = models.CharField(max_length=200)
    def __str__(self):
        return self.ans_text
