from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model


class Product(models.Model):
    title = models.CharField(max_length=225)
    description = models.TextField()
    price = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)
    img = models.ImageField(upload_to='product_img/')
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    count_view = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('detail_view', args=[self.pk])



class ProductComment(models.Model):
    STARS_CHOICES = (
        ('1', 'VERY BAD'),
        ('2', 'BAD'),
        ('3', 'NORMAL'),
        ('4', 'GOOD'),
        ('5', 'GREAT'),
                        )
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='comments',)
    body = models.TextField()
    stars = models.CharField(max_length=1, choices=STARS_CHOICES)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)


    def get_absolute_url(self):
        return reverse('detail_view', args=[self.product_id])

    def __str__(self):
        return self.body[:50]