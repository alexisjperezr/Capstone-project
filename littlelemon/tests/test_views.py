from django.test import TestCase
from restaurant.models import MenuItem

# Create your tests here.
class MenuViewTest(TestCase):
    def setup(self):
        MenuItem.objects.create(title="Calamari", price=12, inventory=100)
        MenuItem.objects.create(title="Spaghetti", price=21, inventory=100)
        MenuItem.objects.create(title="Affogato", price=7, inventory=100)
        
    def test_getall(self):
        MenuItem.objects.all()