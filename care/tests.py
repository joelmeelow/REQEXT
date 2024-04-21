from django.test import TestCase
from django.contrib.auth.models import User
from .models import Pharmmodels
from .models import PharmConverse, PharmMessages
from django.test import Client
from django.urls import reverse
# Create your tests here.
class TestModels(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        
    def test_pharmmodels(self):
        created_by = self.user

        pharmmodells = Pharmmodels.objects.create(name='ebuka', title='pharmacist', username='ugo', created_by=created_by ) 
        
        self.assertEquals(str(pharmmodells), 'pharm_models')
        self.assertTrue(isinstance(pharmmodells, Pharmmodels))
    
    def test_pharm_converse(self):
        pharm_modelss = Pharmmodels.objects.create(name='joel', title='pharmacist', username='chiugo', created_by=self.user)

        pharmconverse = PharmConverse.objects.create(
          Item = pharm_modelss,
          patient = self.user
        )
        self.assertTrue(isinstance(pharmconverse, PharmConverse))
        self.assertEquals(str(pharmconverse), 'conversations')

    def test_pharm_messages(self):
        pharm_modelss = Pharmmodels.objects.create(name='joel', title='pharmacist', username='chiugo', created_by=self.user)
        pharmconverse = PharmConverse.objects.create(Item=pharm_modelss, patient=self.user)
        pharmmessages = PharmMessages.objects.create(
            conversation=pharmconverse,
            content='this is a test',
            created_by=self.user
        )
        self.assertEquals(str(pharmmessages), 'messages')
        self.assertTrue(isinstance(pharmmessages, PharmMessages))
class TestCareView(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        pharm_modelss = Pharmmodels.objects.create(name='joel', title='pharmacist', username='chiugo', created_by=self.user)
        self.pharmconverse = PharmConverse.objects.create(Item=pharm_modelss, patient=self.user)
        self.client = Client()
        self.client.login(username='testuser', password='password')
        #self.index_url = reverse('care:index', kwargs={'project_id':self.pk})

    def test_get_views(self):
        self.client.login(username='testuser', password='password')
        f = PharmConverse.objects.get(patient=self.user)
        self.assertEqual(PharmConverse.objects.count(), 1)
        response = self.client.get(reverse('patients:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'patients/index.html')
        
        #response = self.client.get(reverse('care:index', kwargs={'id':f.id}))
        #self.assertEqual(response.status_code, 301)
        #self.assertTemplateUsed(response, 'patients/login.html' )
    def test_view(self):
        self.client.login(username='testuser', password='password')
        response = self.client.get(reverse('patients:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'patients/index.html')
        print('joyous')

    def test_login_test_view(self):
        self.client.login(username='testuser', password='password')
        response = self.client.get(f'/care/{self.pharmconverse.id}')
        self.assertEquals(response.status_code, 301)
        print('hey')
        #self.assertTemplateUsed(response, 'care/index.html')
        #self.assertEqual(response.context['pharmconverse'].Item.name, 'joel')
        
   
        
