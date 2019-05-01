from django.db import models
from django.utils.html import mark_safe
from markdown import markdown
from django.contrib.auth.models import User


class Categorii(models.Model):
    name = models.CharField(max_length=150, blank=False)
    description = models.CharField(max_length=200, blank=False)

    class Meta:
        verbose_name = 'Categorie'
        verbose_name_plural = 'Categorii'

    def count_posts(self):
        return Discutii.objects.filter(topic__categorie=self).count()

    def last_post(self):
        return Discutii.objects.filter(topic__categorie=self).order_by('-created_at').first()

    def __str__(self):
        return self.name


class Topics(models.Model):
    subject = models.CharField(max_length=100, unique=True, blank=False)
    last_updated = models.DateTimeField(auto_now=True)
    categorie = models.ForeignKey(Categorii, related_name='topics', on_delete=models.CASCADE)
    reteta = models.TextField(max_length=5000, blank=False, default='Text reteta')
    starter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='topics', null=True, blank=True)

    class Meta:
        verbose_name = 'Titlu'
        verbose_name_plural = 'Titluri'

    def get_reteta_as_markdown(self):
        return mark_safe(markdown(self.reteta, safe_mode='escape'))

    def __str__(self):
        return self.subject


class Discutii(models.Model):
    message = models.TextField(max_length=4000, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    topic = models.ForeignKey(Topics, related_name='posts', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = 'Discutie'
        verbose_name_plural = 'Discutii'

    def get_message_as_markdown(self):
        return mark_safe(markdown(self.message, safe_mode='escape'))

    def __str__(self):
        return self.message



