from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=32)
    publish_date = models.DateField(auto_now_add=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    memo = models.TextField(null=True)
    publisher = models.ForeignKey(to='Publisher')   # 创建外键,关联publisher
    author = models.ManyToManyField(to='Author')

    def __str__(self):
        return f'<Book object : {self.id}--{self.title}>'

class Publisher(models.Model):
    name = models.CharField(max_length=32)
    city = models.CharField(max_length=32)

    def __str__(self):
        return f'<Publiser object: {self.id}--{self.name}>'

class Author(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    phone = models.CharField(max_length=11)

    def __str__(self):
        return f'<Author object: {self.id}--{self.name}>'