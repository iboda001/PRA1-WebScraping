# PRA1-WebScraping
En esta primera práctica de la asignatura Tipología y ciclo de vida de los datos del Máster de Ciencia de Datos de la la UOC, se elabora un caso práctico orientado a aprender a identificar los datos relevantes para un proyecto analítico y usar las herramientas de extracción de datos. En este caso que nos ocupa, se extrae la información relevante de los libros en venta de la librería más importate de la CAV: [Elkar Liburu Denda](https://www.elkar.eus/).

Extrae los precios de diferentes alimentos de la página web del SISAP del Ministerio de Agricultura y Riego.

Para ejecutar el script es necesario instalar la siguientes bibliotecas:

pip install pandas
pip install requests
pip install lxml
pip install beautifulsoup4
El script se debe ejecutar de la siguiente manera:

python foodPriceScraper.py --startDate 01/11/2017 --endDate 04/11/2017
Donde startDate es la fecha de inicio y endDate es la fecha de fin del intervalo de tiempo que se deseea extraer. Los registros se almacenan en un archivo de tipo CSV.

Actualmente solo extrae el precio mínimo, promedio y máximo de los siguientes alimentos:

Papa
Limon
Aceite
Ajo
Apio
Arroz
Azucar
Cebolla
Huevos
Leche
Pollo
Tomate
Yuca
Zanahoria

import urllib.request, urllib.parse, urllib.error
import requests 
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import re
import ssl
import os
