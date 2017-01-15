from django.db import models

# Create your models here.
class Question(models.Model):
    level = models.IntegerField()
    question_text = models.CharField(max_length=200, blank=True)
    image = models.ImageField(blank=True)
    html = models.TextField(blank=True)
    script = models.FileField(blank=True)
    video = models.FileField(blank=True)
    audio = models.FileField(blank=True)
     
    def __str__(self):
        return self.question_text

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    ans = models.CharField(max_length=200)
    def __str__(self):
        return self.ans
