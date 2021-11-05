from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=200)

    def __str__(self):
        return self.category_name


class Condition(models.Model):
    condition_name = models.CharField(max_length=200)

    def __str__(self):
        return self.condition_name


class Thing(models.Model):
    brand = models.CharField(max_length=200, default='No name', db_index=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    condition = models.ForeignKey(Condition, on_delete=models.CASCADE)
    cost = models.IntegerField(null=False)
    picture = models.ImageField(upload_to='images/')
    info = models.TextField(blank=True, db_index=True)

    def __str__(self):
        return self.category.category_name + " " + self.brand
