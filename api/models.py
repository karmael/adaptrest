from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class User(BaseModel):
    google_id = models.CharField(max_length=21, primary_key=True)
    username = models.CharField(max_length=31, null=True, blank=True)
    fullname = models.CharField(max_length=127, null=True, blank=True)
    picture = models.CharField(max_length=255, null=True, blank=True)
    company = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=511, unique=True)

    class Meta:
        db_table = "user"


class Todo(BaseModel):
    user = models.ForeignKey(
        User,
        to_field="google_id",
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=127)

    class Meta:
        db_table = "todo"


class TodoItem(BaseModel):
    todo = models.ForeignKey(
        Todo,
        to_field="id",
        on_delete=models.CASCADE,
    )
    desc = models.TextField(null=True, blank=True)
    image = models.TextField(null=True, blank=True)
    status = models.BooleanField(default=False)

    class Meta:
        db_table = "todo_item"
