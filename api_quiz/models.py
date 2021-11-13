from django.db import models


class Quiz(models.Model):
    name = models.CharField(max_length=200,
                            verbose_name='Название опроса')
    date_start = models.DateField(auto_now_add=True,
                                  verbose_name='Дата начала опроса')
    date_end = models.DateField(verbose_name='Дата конца опроса')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.name


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    quiz = models.ForeignKey(Quiz,
                             related_name='question',
                             on_delete=models.CASCADE)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question,
                                 related_name='choice',
                                 on_delete=models.CASCADE)
    text = models.TextField(verbose_name='Вариант ответа')

    def __str__(self):
        return self.text


class Answer(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    question = models.ForeignKey(Question, on_delete=models.DO_NOTHING)
    choice = models.ForeignKey(Choice, on_delete=models.DO_NOTHING)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.choice
