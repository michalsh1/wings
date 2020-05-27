from django.db import models


# class Question(models.Model):
#     question_text = models.CharField(max_length=50, null=False)
#
#     def __str__(self):
#         return self.question_text
#
#
# class Answer(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE, null=False)
#     text = models.CharField(max_length=1000)
#     # is_correct = models.BooleanField(default=False)
#     score = models.IntegerField()
#
#     def __str__(self):
#         return self.text
#
#
class RightAnswer(object):
    YES = 1
    NO = 0

    choices = (
        (YES, 'Yes'),
        (NO, 'No'),
        )

class QuestionYesNo(models.Model):
    question_id = models.IntegerField(primary_key=True)
    question_text = models.CharField(max_length=50, null=False)
    right_answer = models.IntegerField(choices=RightAnswer.choices, default=1, blank= False, null=False)
    score = models.IntegerField(default=1)

    def __str__(self):
        return self.question_text

    # def check_if_correct(self,answer):
    #     if self.right_answer==answer:
    #         return True
    #     else:
    #         return False

# class AnswerYesNo(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE, null=False)
#     text = models.CharField(max_length=1000)
#     # is_correct = models.BooleanField(default=False)
#     score = models.IntegerField()
#
#     def __str__(self):
#         return self.text



# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')
#
#
# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)
