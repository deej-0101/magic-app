from django.db import models
from django.utils import timezone

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class MagicalCreature(BaseModel):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    magical_ability = models.CharField(max_length=100)
    image = models.ImageField(upload_to='static/images/magical_creatures', null=True, blank=True)

    def __str__(self):
        return self.name

class Wizard(BaseModel):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, null=True, blank=True)
    magical_abilities = models.TextField()
    birth_date = models.DateField()
    magical_wand = models.CharField(max_length=100)
    image = models.ImageField(upload_to='static/images/wizards', null=True, blank=True)

    def __str__(self):
        return self.name

class EnchantedPlace(BaseModel):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    enchantment_level = models.IntegerField()

    def __str__(self):
        return self.name

class MagicalEvent(BaseModel):
    title = models.CharField(max_length=200)
    date = models.DateField()
    place = models.ForeignKey(EnchantedPlace, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class MagicalEncounter(BaseModel):
    event = models.ForeignKey(MagicalEvent, on_delete=models.CASCADE)
    wizard = models.ForeignKey(Wizard, on_delete=models.CASCADE)
    creature = models.ForeignKey(MagicalCreature, on_delete=models.CASCADE)
    outcome = models.TextField()

    def __str__(self):
        return f"{self.event.title} - {self.wizard.name} meets {self.creature.name}"
