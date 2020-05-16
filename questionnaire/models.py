from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.question_text


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=False)
    text = models.CharField(max_length=1000)
    # is_correct = models.BooleanField(default=False)
    score = models.IntegerField()

    def __str__(self):
        return self.text



# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')
#
#
# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)
