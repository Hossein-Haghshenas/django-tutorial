from django.db import models
from django.utils import timezone
import datetime


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

# The code defines a simple Question model with a question and a publication date.
#  It also defines a Choice model with a foreign key to Question and a choice text and a vote tally.
#  With these models, Django is able to create a database schema (CREATE TABLE statements) for this app.

# in next step you should run "python manage.py makemigrations polls"

# By running makemigrations, you’re telling Django that you’ve made some changes to your models
# (in this case, you’ve made new ones) and that you’d like the changes to be stored as a migration.

# and then "python manage.py sqlmigrate polls 0001"

# you can also run python manage.py check;
# this checks for any problems in your project without making migrations or touching the database.

# finally run "python manage.py migrate" to create the tables in the database
# The migrate command takes all the migrations that haven’t been applied
# (Django tracks which ones are applied using a special table in your database called django_migrations)
# and runs them against your database - essentially, synchronizing the changes you made to your models
# with the schema in the database.
