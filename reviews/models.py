from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from movies.models import Movie


class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.PROTECT, related_name='reviews')
    stars = models.IntegerField(
        validators=[
            MinValueValidator(1, 'Escolha de 1 à 5 estrelas.'),
            MaxValueValidator(5, 'Escolha de 1 à 5 estrelas.')
        ]
    )
    comment = models.TextField(max_length=2000, null=True, blank=True)

    def __str__(self):
        return f'{self.movie}'
