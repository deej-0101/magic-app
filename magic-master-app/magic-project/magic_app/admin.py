from django.contrib import admin
from .models import EnchantedPlace, MagicalCreature, MagicalEncounter, MagicalEvent, Wizard

class BaseModelAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'updated_at')
    
class EnchantedPlaceAdmin(BaseModelAdmin):
    list_display = ('name', 'location', 'enchantment_level', 'created_at', 'updated_at')

class MagicalCreatureAdmin(BaseModelAdmin):
    list_display = ('name', 'species', 'magical_ability', 'created_at', 'updated_at')

class MagicalEncounterAdmin(BaseModelAdmin):
    list_display = ('event', 'wizard', 'creature', 'outcome', 'created_at', 'updated_at')

class MagicalEventAdmin(BaseModelAdmin):
    list_display = ('title', 'date', 'place', 'created_at', 'updated_at')

class WizardAdmin(BaseModelAdmin):
    list_display = ('name', 'email', 'magical_abilities', 'birth_date', 'magical_wand', 'created_at', 'updated_at')

# Register the models with their respective Admin classes
admin.site.register(EnchantedPlace, EnchantedPlaceAdmin)
admin.site.register(MagicalCreature, MagicalCreatureAdmin)
admin.site.register(MagicalEncounter, MagicalEncounterAdmin)
admin.site.register(MagicalEvent, MagicalEventAdmin)
admin.site.register(Wizard, WizardAdmin)
