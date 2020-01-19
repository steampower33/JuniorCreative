from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Book(models.Model):

    title = models.CharField(max_length=200, null=True)
    link = models.CharField(max_length=1000, null=True)
    author_name = models.CharField(max_length=50, null=True)
    author_link = models.CharField(max_length=1000, null=True)
    pub_name = models.CharField(max_length=50, null=True)
    pub_date = models.CharField(max_length=50, null=True)
    
    class TYPE_BIG(models.TextChoices):
        COMPUTER = 'COM', _('Computer')
        NATURAL_SCIENCE = 'NAT', _('Natual_Science')
        ECONOMY = 'ECO', _('ECONOMY')
        HISTORY = 'HIS', _('History')

    class TYPE_SMALL(models.TextChoices):
        NETWORK = 'NET', _('Network')
        GAME = 'GAM', _('Game')
        GRAPHIC = 'GRA', _('Graphic')
        MOBILE = 'MOB', _('Mobile')

    class TYPE_DETAIL(models.TextChoices):
        NORMAL = 'NOR', _('Normal')
        TCP_IP = 'TCP', _('TCP/IP')
        SECURITY = 'SEC', _('Security')

    type_big = models.CharField(
        max_length=10,
        choices=TYPE_BIG.choices,
        default=True,
    )

    type_small = models.CharField(
        max_length=10,
        choices=TYPE_SMALL.choices,
        default=True
    )

    type_detail = models.CharField(
        max_length=10,
        choices=TYPE_DETAIL.choices,
        default=True
    )

    def __str__(self):
        return self.title

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    author = models.CharField(max_length=50)
    text = models.TextField()
    grade = models.IntegerField(default=1)
    created_date = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.text


