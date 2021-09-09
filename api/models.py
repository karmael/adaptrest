import os
from django.db import models


class FilterOrCreateManager(models.Manager):
    """Adds filter_or_create method to objects. Returns:
    - obj: QuerySet for the filtered/created object
    - created: Boolean that specifies if a new object was created"""

    def filter_or_create(self, **kwargs):
        created = False
        obj = self.filter(**kwargs).first()
        if obj is None:
            obj = self.create(**kwargs)
            created = True
        return obj, created


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = FilterOrCreateManager()

    class Meta:
        abstract = True


class User(BaseModel):
    google_id = models.CharField(max_length=21, primary_key=True)
    username = models.CharField(max_length=50, null=True, blank=True)
    fullname = models.CharField(max_length=50, null=True, blank=True)
    picture = models.CharField(max_length=50, null=True, blank=True)
    company = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=50, unique=True)

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
    image = models.ImageField(null=True, blank=True, upload_to=os.environ.get("MEDIA_URL"))
    status = models.BooleanField(default=False)

    class Meta:
        db_table = "todo_item"
