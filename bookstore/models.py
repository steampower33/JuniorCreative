from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Book(models.Model):

    class TYPE_OF_BOOK(models.TextChoices):
        COMPUTER = 'COM', _('Computer')
        NATURAL_SCIENCE = 'NAT', _('Natual_Science')
        ECONOMY = 'ECO', _('ECONOMY')
        HISTORY = 'HIS', _('History')
        
    class TYPE(models.TextChoices):
        GAME = 'GAM', _('Game')

    type_of_book = models.CharField(
        max_length=10,
        choices=TYPE_OF_BOOK.choices,
        default=True,
    )

    type2 = models.CharField(
        max_length=10,
        choices=TYPE.choices,
        default=True
    )

    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    published_date = models.DateField(blank=True)

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