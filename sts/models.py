from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)

    # Payment statuses for each month from August to May
    august = models.BooleanField(default=False)
    september = models.BooleanField(default=False)
    october = models.BooleanField(default=False)
    november = models.BooleanField(default=False)
    december = models.BooleanField(default=False)
    january = models.BooleanField(default=False)
    february = models.BooleanField(default=False)
    march = models.BooleanField(default=False)
    april = models.BooleanField(default=False)
    may = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    @property
    def payment_status(self):
        """Check if all payments are completed."""
        return all([
            self.august, self.september, self.october, self.november,
            self.december, self.january, self.february, self.march,
            self.april, self.may
        ])
