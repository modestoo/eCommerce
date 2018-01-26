# conding=utf-8

from django.shortcuts import render
from django.http import HttpResponse

def index(request):

	#É uma varíavel que ira carregar textos na homepage
	texts = ['Lorem ipsum dollor sit amen', 'Teste 1, 2, 3...']

	# Context é um dicionário de Variáveis que serão passadas para o template utilizar
	context = {

		#A variável title será utilizada para passar o nome da aplicação para o template, por exemplo.
		'title': 'Django E-commerce',
		'texts': texts,
	}

	return render(request, 'index.html', context)


def contact(request):
	return render(request, 'contact.html')


def product(request):
	return render(request, 'product.html')


def product_list(request):
	return render(request, 'product_list.html')