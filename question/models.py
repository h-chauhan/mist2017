from django.db import models

# Create your models here.
def upload_location(instance, filename):
        return "%s/%s" % (instance.id, filename)

class Question(models.Model):
    level = models.IntegerField()
    question_text = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to=upload_location, blank=True)
    html = models.TextField(blank=True)
    script = models.FileField(upload_to=upload_location, blank=True)
    video = models.FileField(upload_to=upload_location, blank=True)
    audio = models.FileField(upload_to=upload_location, blank=True)

    
     
    def __str__(self):
        return str(self.level)

class Answer(models.Model):
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    ans = models.CharField(max_length=200)
    def __str__(self):
        return self.ans


