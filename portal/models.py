from django.db import models
import datetime

# Create your models here.

class Catalog(models.Model):
    name     = models.CharField(max_length=45, null=False, blank=False, verbose_name='名称')
    created_on = models.DateTimeField(null=False, blank=False, auto_now_add=True)
    updated_on = models.DateTimeField(null=False, blank=False, auto_now=True)
    def __str__(self):
        return self.name
    

class Memo(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False, verbose_name='标题')
    content = models.TextField(max_length=255, null=False, blank=False, verbose_name='内容')
    catalog = models.ForeignKey('Catalog', on_delete=models.CASCADE)
    created_on = models.DateTimeField(null=False, blank=False, auto_now_add=True)
    updated_on = models.DateTimeField(null=False, blank=False, auto_now=True)
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name='笔记'
        verbose_name_plural='笔记'

