##Scraper de Noticias de E-Periodico La Republica:##

####Preparar el Entorno####

Inicializamos proyecto en git
Y luego agregamos el modulo de desarrollo de python
<> py -m venv venv </>
Lo siguiente que se realiza es iniciar un entorno virtual
En windows = venv/Scripts/activate
En windows con terminal Unix = source venv/Scripts/activate
En linux y en mac = source venv/bin/activate

*(opcional) crear un workspace para llevar un historial de trabajo*

Luego se ha de instalar las dependencias a utilizar: Request, LXML y autopep8
<> pip install requests lxml autopep8 </>

//py -m pip install --upgrade pip <- comando para actualizar pip si se necesitara

Con esto ya habremos terminado de preparar el entorno

####Construir las expresiones de Xpath####

*Las direcciones de las expresiones las iremos almacenando en el archivo xpath.txt*

Desde la pagina principal inspeccionamos los titulos para notar si hay alguna
similitud en su construccion, al notar un aspecto igual, lo tomamos como raiz
de la expresion, y comenzamos a escribir desde ese elemento.

El primer elemento que vamos a extraer son los links de las noticias en la pagina principal.

**Importante**: Cada noticia en la pagina principal no es mas que un indexer que nos llevara a la pagina en la que se almacena, los elementos que vamos a extraer realmente los encontraremos dentro de cada link.

En este caso los elementos que queremos extraer son el titulo de la noticia, la descripcion de esta y por ultimo, su cuerpo.

Una vez tengamos sus expresiones, podremos continuar

####Creacion del scripts scraper con Python####

Se creara un archivo nuevo en la carpeta raiz del proyecto llamado scraper.py
