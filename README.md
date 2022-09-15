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
*Recuerda tener activo el entorno virual de desarrollo (venv)*
*Leer junto al scraper*

Debemos crear un archivo nuevo en la carpeta raiz del proyecto llamado scraper.py.

Dentro de este se importaran los modulos requests y lxml, de este ultimo se extraera su funcion html para convertir codigo html y se llamara de la misma forma (html). *(L 1 - 2)*

A continuacion se crearan las constantes a utilizar, en las cuales se almacenaran las expresiones que nos dirigen a los elementos a extraer. *(L 4-9)*

Se definen 2 funciones, una para pasar los links (parse_home), otra para correr todo el script (run), esa segunda por ahora estara ejecutando la anterior funcion.

Para trabajar de forma segura se encapsula el codigo en un try-except, si sucede un error al recibir la peticion, por ejemplo, que el estatus sea diferente a 200, entonces manejara el error. En try se guardara la respuesta a la peticion, con requests.get se traera el documneto html de la pagina principal, y si el estatus de la respuesta es igual a 200 entonces una nueva variable home guardara la respuesta decodificada en 'utf-8'.
        *response.content devuelve el html de la respuesta, al agregarle .decode('utf-8') nos aseguramos de transformar los caracteres especiales a unos que python pueda procesar y guardar en los archivos*
A continuacion se crea una nueva variable parsed que toma todo el codigo html
y lo transforma en un documento especial en el que se puede hacer Xpath.
Por ultimo, se crea una ultima variable en la que se ejecuta parsed.xpath pasandole como parametro la constante donde se almacenan los Links.
Ya para finalizar esta prueba, se imprime la anterior variable.
*(L 11-25)*

*Si llegase a surgir un error en el que no se envia la misma cantidad de urls que en el navegador, entonces se debe cambiar la expresion //h2/a/@href por //text-fill/a/@href (Actualmente ya se encuentra modificado)*

Luego se creara el entrypoint del archivo de python y se ejecutara al final la funcion "run".*(L -)*

####Guardar las noticias en archivos####
