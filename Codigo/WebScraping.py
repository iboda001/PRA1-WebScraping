#CARGA DE LIBRERÍAS
import urllib.request, urllib.parse, urllib.error
import requests 
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import re
import ssl
import os


# Ignorar errores ssl
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


#Parámetros a mano
#Directorio donde está localizado el script
#currentDir = os.path.dirname(__file__)
filename = "lista_libros.csv"
max_pag=20
#filePath = os.path.join(currentDir, filename)
url_principal="https://www.elkar.eus/es/katalogoa/liburuak"

#Indicamos el User-Agent
headers = {
    'User-Agent': 'Irati Boda',
    'From': 'iboda001@uoc.edu' 
}


def scraping(num_pag,headers):
    # Obtenemos toda la información de los libros
    lista_libros=[]

    for i in range(num_pag+1):      # Número de páginas +1
        url="https://www.elkar.eus/es/katalogoa/liburuak/-1/{}?a&sort=default&dir=desc".format(i)
        # Realizamos la petición a la web
        req = requests.get(url,headers=headers)
        status_code = req.status_code
        #El status_code 200 significa que la página se ha cargado correctamente
        if status_code == 200:
            html = urllib.request.urlopen(url, context=ctx).read()
            # Pasamos el contenido HTML de la web a un objeto BeautifulSoup()
            soup = BeautifulSoup(html, 'html.parser')

            # Obtenemos toda la información de los libros
            info_libro=soup.find_all("div",{"class":"liburu_box"})

            # Recorremos todas las entradas para extraer el título, autor y fecha
            for i, entrada in enumerate(info_libro):
                # Con el método "getText()" no nos devuelve el HTML
                titulo = entrada.find('p', {'class': 'titulua'}).getText().replace('\n', '') #el título incluye un intro
                autor = entrada.find('p', {'class': 'autorea'}).getText()
                precio=entrada.find('div',{'class': 'liburu_saskia'}).getText()
                #Obtenemos solo el número del precio
                precio=float(re.findall("\d+\,\d+",precio)[0].replace(',', '.'))
                precio_socio=entrada.find('div',{'class': 'bezero_fidela'}).getText()
                precio_socio=float(re.findall("\d+\,\d+",precio_socio)[0].replace(',', '.'))
                link=entrada.find_all("div",{"class":"liburu_img"})[0].a.get("href")
                # adjunto a la lista de libros el título, autor, precio general, precio de socio y link
                lista_libros.append([titulo, autor,precio,precio_socio,link])
        elif "blocked" in req.text:
            print ("Hemos sido bloqueados")
        else:
            print("! Error {} retrieving url {}".format(req.status_code, url))
            
    data = pd.DataFrame(lista_libros,columns=["Titulo", "Autor","Precio","Precio_socio","Link"])   
    
    return data


def data2csv(data,filename):
    """
    Exportación del dataframe a un csv  
    """
    dt=data
    dt.to_csv("./Fichero-csv/" + filename, index=False, header=True, sep=';',encoding='utf-8-sig')

data2csv(scraping(20,headers),filename)   
