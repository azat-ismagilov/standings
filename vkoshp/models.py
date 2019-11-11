from django.db import models


class Contest(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    city = models.CharField(max_length=50)

    contest = models.ForeignKey(Contest, on_delete=models.CASCADE)

    def get_rating(self):
        sum = 0
        for i in self.participant_set.all():
            sum += i.codeforces_rating
        return sum

    def __str__(self):
        return self.name


class Participant(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    name = models.CharField(max_length=50, blank=True, default="")

    MEDAL = (("n", "none"), ("g", "gold"), ("s", "silver"), ("b", "bronse"))

    medal = models.CharField(max_length=1, choices=MEDAL, blank=True, default="n")

    codeforces_handle = models.CharField(max_length=50, blank=True, default="")
    codeforces_rating = models.PositiveIntegerField(default=0)

    def has_handle(self):
        return (self.codeforces_handle != "")

    def get_color(self):
        if self.codeforces_rating < 1200:
            return "user-gray"
        if self.codeforces_rating < 1400:
            return "user-green"
        if self.codeforces_rating < 1600:
            return "user-cyan"
        if self.codeforces_rating < 1900:
            return "user-blue"
        if self.codeforces_rating < 2100:
            return "user-violet"
        if self.codeforces_rating < 2400:
            return "user-orange"
        if self.codeforces_rating < 2900:
            return "user-red"
        return "user-legendary"


    def is_legendary(self):
        return self.codeforces_rating >= 2900


    def __str__(self):
        return self.name + '/' + self.team.name

class HandleInvoice(models.Model):
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)

    handle = models.CharField(max_length=50, blank=True, default="")

