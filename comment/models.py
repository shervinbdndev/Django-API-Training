from django.db import models
from django.contrib.auth.models import User



class Comment(models.Model):
    RATES: list[tuple[int, str]] = [
        (1, 'Worst'),
        (2, 'Meh'),
        (3, 'Best'),
    ]
    
    user = models.ForeignKey(to=User, default=None, blank=True, on_delete=models.CASCADE ,verbose_name='User')
    text = models.TextField(max_length=200, default=None, blank=True, verbose_name='Comment')
    rate = models.IntegerField(choices=RATES, default=None, blank=True, verbose_name='Rate')
    viewed_by_admin = models.BooleanField(default=False, blank=True, verbose_name='Viewed By Admin')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated at')
    
    def __str__(self) -> str:
        return str(self.user)
    
    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'