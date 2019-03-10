from django.db import models


class Interaction(models.Model):
    input = models.CharField(max_length=100)
    output = models.TextField()
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return (self.input)

    class Meta:
        db_table = 'interactions'
