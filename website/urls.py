#Importação da função Index() definida no arquivo views.py
from . import views

app_name = 'website'

#urlpatterns contém a lista de roteamento de URLs
urlpatterns = [
    #Get /
    path('', views.index, name='index'),
]
