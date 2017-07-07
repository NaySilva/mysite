from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=240)
    closed = models.BooleanField(default=False)
    pub_date = models.DateField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __str__(self):
        return self.question_text



