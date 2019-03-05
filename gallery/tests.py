from django.test import TestCase
import datetime as dt
# Create your tests here.
from .models import Image,Category,Location
import datetime as dt

class CategoryTestClass(TestCase):
     # Set up method
    def setUp(self):
        self.type= Category(name ='Nature')

    def test_instance(self):
        self.assertTrue(isinstance(self.type,Category))

    def test_init(self):
       
        self.assertTrue(self.type.name == 'Nature')

    def test_save_method(self):
        self.type.save_category()
        categorys = Category.objects.all()
        self.assertTrue(len(categorys)> 0)
    
    def tearDown(self):
       Category.objects.all().delete()
       


      
       