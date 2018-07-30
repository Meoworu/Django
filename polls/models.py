from django.db import models

# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')
#
#
# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)

class Movies(models.Model):
    image = models.CharField(max_length=100)
    time_length = models.CharField(max_length=20)
    text = models.TextField()
    author = models.CharField(max_length=50)
    number = models.IntegerField()
    show_time = models.IntegerField()


class BookInfo(models.Model):
    title = models.CharField(max_length=20)
    pub = models.DateTimeField()

    def __str__(self):
        return self.title


class HeroInfo(models.Model):
    name = models.CharField(max_length=10)
    gender = models.BooleanField()
    content = models.CharField(max_length=1000)
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)

    def __str__(self):
        return self.name