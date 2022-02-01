from unicodedata import name
from django.db import models
from django.conf import settings


class Resume(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True, default=None)
    name = models.CharField(max_length=200, default=None)
    surname = models.CharField(max_length=200, default=None)
    email = models.EmailField(max_length=200, default=None)
    title = models.CharField(max_length=200, default=None)
    description = models.TextField(max_length=1000, default=None, null=True)

    def __str__(self):
        return self.name


class Education(models.Model):
    name = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    resume = models.ForeignKey(
        Resume, on_delete=models.CASCADE, related_name='educations', null=True)

    def __str__(self):
        return self.name


class Experience(models.Model):
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField(blank=True)
    resume = models.ForeignKey(
        Resume, on_delete=models.CASCADE, related_name='experiences')

    def __str__(self):
        return self.company

    class Meta:
        verbose_name = 'Experience'
        verbose_name_plural = 'Experiences'


class Skill(models.Model):
    title = models.CharField(max_length=38)
    resume = models.ForeignKey(
        Resume, on_delete=models.CASCADE, related_name='skills')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'


class Achievement(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    year = models.DateField()
    resume = models.ForeignKey(
        Resume, on_delete=models.CASCADE, related_name='achievements')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Achievement'
        verbose_name_plural = 'Achievements'


LEVEL_CHOICES = (
    ('beginner', 'beginner'),
    ('moderate', 'moderate'),
    ('advanced', 'advanced'),
    ('native', 'native'),
)


class Language(models.Model):
    title = models.CharField(max_length=255)
    level = models.CharField(
        max_length=20, choices=LEVEL_CHOICES, default='beginner')
    resume = models.ForeignKey(
        Resume, on_delete=models.CASCADE, related_name='languages')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Language'
        verbose_name_plural = 'Languages'
