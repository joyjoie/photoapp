from django.test import TestCase
import datetime as dt
# Create your tests here.
from .models import Editor,Image,Category,Location


class EditorTestClass(TestCase):
    
    # Set up method
    def setUp(self):
        self.joy= Editor(first_name = 'Joy', last_name ='W', email ='joy@moringaschool.com')

     # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.joy,Editor))

        
    # Testing Save Method
    def test_save_method(self):
        self.joy.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)

    # Testing delete
    def tearDown(self):
        Editor.objects.all().delete()
        