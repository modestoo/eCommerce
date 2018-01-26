# coding=utf-8

from django.test import TestCase, Client
from django.core.urlresolvers import reverse

class IndexViewTestCase(TestCase):

	# Método executado antes dos testes para criar as instâncias de objetos necessárias para execução dos testes
	def setUp(self):
		self.client = Client() 
		self.url = reverse('index') # 'index' é o nome atribuido a URL '/'

	# Método executado ao final dos testes para destruir os objetos criados
	def tearDown(self):
		pass

	# Testa o status retornado pela requisição da página "index"
	def test_status_code(self):
		response = self.client.get(self.url)
		self.assertEquals(response.status_code, 200)

	# Testa se o template retornado pela url é o template "index"
	def test_template_used(self):
		response = self.client.get(self.url)
		self.assertTemplateUsed(response, 'index.html')
