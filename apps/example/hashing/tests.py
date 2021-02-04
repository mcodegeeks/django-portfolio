import hashlib
from django.test import TestCase
from django.urls import reverse 
from .forms import HashForm
from .models import Hash

class UnitTestCase(TestCase):
    
    def test_index_template(self):
        response = self.client.get(reverse('hashing:index'))
        self.assertTemplateUsed(response, 'example/hashing/index.html')

    def test_hash_form(self):
        form = HashForm(data={'text':'hello'})
        self.assertTrue(form.is_valid())

    def test_hash_lib(self):
        text_hash = hashlib.sha256('hello'.encode('utf-8')).hexdigest()
        self.assertEqual('2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824', text_hash)

    def test_hash_object(self):
        hash = Hash()
        hash.text = 'hello'
        hash.hash = '2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824'
        hash.save()
        pulled_hash = Hash.objects.get(hash=hash.hash)
        self.assertEqual(hash.text, pulled_hash.text)
