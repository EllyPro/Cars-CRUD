from django.test import TestCase,Client

from .models import Make,Cars

# Create your tests here.

class CarsTest(TestCase):

    def setUp(self):
        m1 = Make.objects.create(name='Pros')
        m2 = Make.objects.create(name='bb')
        m2 = Make.objects.create(name='bxb')
        c1 = Cars.objects.create(nickname='Elly',mileage=125,comment='Best Car ever',make=m1)

    def test_valid_milage(self):
        ca = Cars.objects.get(nickname='Elly')
        self.assertTrue(ca.is_valid_milage())    
    def test_makes(self):
        c = Client()
        res = c.get('/makes/')
        self.assertEqual(res.status_code,200)
        self.assertEqual(res.context['make_list'].count(),3)