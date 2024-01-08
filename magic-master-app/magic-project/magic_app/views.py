from django.shortcuts import render
from django.views import View
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from .models import MagicalCreature, Wizard, EnchantedPlace, MagicalEncounter, MagicalEvent

class Home(ListView):
    model = Wizard
    content_onject_name = 'home'
    template_name = "base.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['creatures'] = MagicalCreature.objects.all()[:5]  # Fetching a few magical creatures
        context['places'] = EnchantedPlace.objects.all()[:3]  # Fetching a few enchanted places

        return context

class MagicalCreatureListView(ListView):
    model = MagicalCreature
    context_object_name = 'creatures'
    template_name = 'creature_list.html'
    paginate_by = 5  # Adjust the number of items per page as needed
    
    def get_queryset(self):
        return MagicalCreature.objects.order_by('name', 'species', 'magical_ability')

# DRIVER
class WizardListView(ListView):
    model = Wizard
    context_object_name = 'wizards'
    template_name = 'wizard_list.html'
    paginate_by = 3  # Adjust the number of items per page as needed
     
    def get_queryset(self):
        return Wizard.objects.order_by('image', 'name', 'email', 'magical_abilities', 'birth_date', 'magical_wand')


class EnchantedPlaceListView(ListView):
    model = EnchantedPlace
    context_object_name = 'places'
    template_name = 'place_list.html'
    paginate_by = 5  # Adjust the number of items per page as needed
    
    def get_queryset(self):
        return EnchantedPlace.objects.order_by('name', 'location', 'enchantment_level')

class MagicalEncounterListView(ListView):
    model = MagicalEncounter
    context_object_name = 'encounter'
    template_name = 'encounter_list.html'
    paginate_by = 5  # Adjust the number of items per page as needed
    
    def get_queryset(self):
        return MagicalEncounter.objects.order_by('event', 'wizard', 'creature', 'outcome')

class MagicalEventListView(ListView):
    model = MagicalEvent
    context_object_name = 'event'
    template_name = 'event_list.html'
    paginate_by = 5  # Adjust the number of items per page as needed
    
    def get_queryset(self):
        return MagicalEvent.objects.order_by('title', 'date', 'place')

