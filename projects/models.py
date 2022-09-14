# from enum import unique
# from random import choices
# from django.db import models
# import uuid
# from users.models import Profile

# # Create your models here.
# class Project(models.Model):
#     user_list = Profile.objects.all()
#     owner = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.SET_NULL)
#     title = models.CharField(max_length=200)
#     description = models.TextField(null=True, blank=True)
#     featured_image = models.ImageField(null=True, blank=True, default='default.jpg')
#     # users = models.Choices(choices=user_list)
#     demo_link = models.CharField(max_length=200, null=True, blank=True)
#     source_link = models.CharField(max_length=200, null=True, blank=True)
#     tags = models.ManyToManyField('Tag', blank=True)
#     vote_total = models.IntegerField(default=0, null=True, blank=True)
#     vote_ratio = models.IntegerField(default=0, null=True, blank=True)
#     created = models.DateTimeField(auto_now_add=True)
#     id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

#     def __str__(self):
#         return self.title

#     class Meta:
#         ordering = ['-vote_ratio', '-vote_total', 'title']

#     @property
#     def reviewers(self):
#         queryset = self.review_set.all().values_list('owner__id', flat=True)
#         return queryset

#     @property
#     def getVoteCount(self):
#         reviews = self.review_set.all()
#         upVotes = reviews.filter(value='up').count()
#         totalVotes = reviews.count()

#         ratio = (upVotes / totalVotes) * 100
#         self.vote_total = totalVotes
#         self.vote_ratio = ratio
#         self.save()


# class Review(models.Model):
#     VOTE_TYPE = (
#         ('up', 'Up Vote'),
#         ('down', 'Down Vote'),
#     )
#     owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
#     project = models.ForeignKey(Project, on_delete=models.CASCADE)
#     body = models.TextField(null=True, blank=True)
#     value = models.CharField(max_length=200, choices=VOTE_TYPE)
#     created = models.DateTimeField(auto_now_add=True)
#     id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

#     def __str__(self):
#         return self.value

#     # class Meta:
#     #     unique_together = [['owner', 'project']]

# class Tag(models.Model):
#     name = models.CharField(max_length=200)
#     created = models.DateTimeField(auto_now_add=True)
#     id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

#     def __str__(self):
#         return self.name

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

status = (
    ('1', 'Stuck'),
    ('2', 'Working'),
    ('3', 'Done'),
)

due = (
    ('1', 'On Due'),
    ('2', 'Overdue'),
    ('3', 'Done'),
)


# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=80)
    project_lead = models.ForeignKey(User, on_delete=models.CASCADE)
    assign = models.ManyToManyField(User, related_name="project_assign")
    # efforts = models.DurationField()
    status = models.CharField(max_length=7, choices=status, default=1)
    complete_per = models.FloatField(max_length=2, validators = [MinValueValidator(0), MaxValueValidator(100)])
    description = models.TextField(blank=True)
    deadline = models.DateField()

    add_date = models.DateField(auto_now_add=True)
    upd_date = models.DateField(auto_now_add=False, auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return (self.name)


class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="task_project_assign")
    assign = models.ManyToManyField(User, related_name="task_assign")
    task_name = models.CharField(max_length=80)
    status = models.CharField(max_length=7, choices=status, default=1)
    due = models.CharField(max_length=7, choices=due, default=1)
    description = models.TextField(blank=True)
    deadline = models.DateField()

    class Meta:
        ordering = ['project', 'task_name']

    def __str__(self):
        return(self.task_name)

# class ProjectAssign(models.Model):
#     user_id = models.ForeignKey(User, on_delete=models.CASCADE)
#     project_id = models.ForeignKey(Project, on_delete=models.CASCADE)

#     class Meta:
#         db_table = 'project_assign_user'

#     def __str__(self) -> str:
#         return f"{self.user_id} with project {self.project_id}"