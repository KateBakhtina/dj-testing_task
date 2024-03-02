from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    author = models.CharField(max_length=55)
    title = models.CharField(max_length=255)
    date_start = models.DateTimeField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    users = models.ManyToManyField(User, related_name="products")

    class Meta:
        ordering = ["date_start"]

    def __str__(self):
        return f"{self.id}: {self.author} {self.title} {self.date_start} {self.price}"


class Lesson(models.Model):
    title = models.CharField(max_length=255)
    link = models.URLField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="lessons")

    def __str__(self):
        return f"{self.title}"


class Quantity(models.Model):
    min_quantity = models.PositiveIntegerField()
    max_quantity = models.PositiveIntegerField()
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name="quantity")


    def __str__(self):
        return f"{self.product}: {self.min_quantity} - {self.max_quantity}"

class StudyGroup(models.Model):
    title = models.CharField(max_length=55)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="study_groups")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="study_groups")

    def __str__(self):
        return f"{self.title}: {self.user} {self.product}"










