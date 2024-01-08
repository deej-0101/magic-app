from django.core.management.base import BaseCommand
from magical_app.models import MagicalCreature, Wizard, EnchantedPlace, MagicalEvent, Spell, MagicalEncounter
from datetime import date

class Command(BaseCommand):
    help = 'Creates initial data for the magical application'

    def handle(self, *args, **kwargs):
        self.create_magical_data()

    def create_magical_data(self):
        # Create Magical Creatures
        creature1 = MagicalCreature(name="Phoenix", species="Bird", magical_ability="Fire Manipulation")
        creature1.save()

        creature2 = MagicalCreature(name="Dragon", species="Reptile", magical_ability="Flight, Fire Breath")
        creature2.save()

        # Create Wizards
        wizard1 = Wizard(name="Merlin", magical_abilities="Sorcery, Transfiguration", birth_date=date(500, 6, 20), magical_wand="Oak, Dragon Heartstring")
        wizard1.save()

        wizard2 = Wizard(name="Morgana", magical_abilities="Dark Magic, Shape-shifting", birth_date=date(520, 9, 15), magical_wand="Ebony, Basilisk Fang")
        wizard2.save()

        # Create Enchanted Places
        place1 = EnchantedPlace(name="Avalon", location="Unknown", enchantment_level=10)
        place1.save()

        place2 = EnchantedPlace(name="Eldritch Forest", location="Realm of Magica", enchantment_level=8)
        place2.save()

        # Create Magical Events
        event1 = MagicalEvent(title="The Grand Conclave", date=date(2024, 6, 1), place=place1)
        event1.save()

        event2 = MagicalEvent(title="Dragon's Eclipse", date=date(2024, 8, 15), place=place2)
        event2.save()

        # Create Spells
        spell1 = Spell(name="Lumos", description="Produces light at the wand tip")
        spell1.save()

        spell2 = Spell(name="Expelliarmus", description="Disarms your opponent")
        spell2.save()

        # Create Magical Encounters
        encounter1 = MagicalEncounter(event=event1, wizard=wizard1, creature=creature1, outcome="Alliance forged with the Phoenix")
        encounter1.save()

        encounter2 = MagicalEncounter(event=event2, wizard=wizard2, creature=creature2, outcome="Subdued the Dragon")
        encounter2.save()

        self.stdout.write(self.style.SUCCESS('Successfully created initial magical data.'))
