from django.db import models


# Create your models here.


class Order(models.Model):
    oid = models.IntegerField()
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=798)
    mail = models.EmailField()
    product = models.CharField(max_length=78)

    def __str__(self):
        return f'OrderId = {self.oid}, Name = {self.name}, Address = {self.address}, Mail = {self.mail}, Product = {self.product}'
