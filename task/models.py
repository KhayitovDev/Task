from django.db import models


class Menu(models.Model):
    title=models.CharField(max_length=250, blank=True)
    url=models.CharField(max_length=250)
    named_url=models.CharField(max_length=250, blank=True)
    parent=models.ForeignKey('self', on_delete=models.CASCADE,  null=True, blank=True)
    is_active=models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title
    
