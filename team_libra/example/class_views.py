from django.views.generic import ListView, TemplateView
import requests
import json

#FUNCION EXTRA, EN REALIDAD ES OPCIONAL 
def generate_request(url, params={}):
    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()


class Example(TemplateView):
    template_name = 'example.html' #AQUI VA LA DIRECCION DE TU ARCHIVO HTML
    
    #FUNCION PARA CONSUMIR LA API QUE QUIERAS 
    def get(self, request, *args, **kwargs):
        self.object = None

        #INSTRUCCIONES OPCIONALES 
        params = { 'order': 'desc' } 
        #AQUI VA LA URL O BIEN HAZ UNA VARIABLE Y PASALA AQUI 
        response = generate_request('http://cesunrecursoshumanos.pythonanywhere.com/Cesun-universidad/DocenteAPI', params)
        # SE CONVIERTEN LOS DATOS A json, HAY MAS FORMAS DE HACERLO 
        data_string = json.dumps(response)
        decoded = json.loads(data_string)

        #LOS RETONAMOS EN LAS VARIABLES 'NOTICIA' Y 'AUTOR' 
        return self.render_to_response(
            self.get_context_data(
            cesun_api = decoded
        ))

# NO QUEDO CLARO ?
# IR A https://requests.readthedocs.io/es/latest/