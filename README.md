# Scraper de Noticias de E-Journal La Republica: #

### Preparar el Entorno ###

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

### Construir las expresiones de Xpath ###

*Las direcciones de las expresiones las iremos almacenando en el archivo xpath.txt*

Desde la pagina principal inspeccionamos los titulos para notar si hay alguna
similitud en su construccion, al notar un aspecto igual, lo tomamos como raiz
de la expresion, y comenzamos a escribir desde ese elemento.

El primer elemento que vamos a extraer son los links de las noticias en la pagina principal.

**Importante**: Cada noticia en la pagina principal no es mas que un indexer que nos llevara a la pagina en la que se almacena, los elementos que vamos a extraer realmente los encontraremos dentro de cada link.

En este caso los elementos que queremos extraer son el titulo de la noticia, la descripcion de esta y por ultimo, su cuerpo.

Una vez tengamos sus expresiones, podremos continuar

### Creacion del scripts scraper con Python ###
*Recuerda tener activo el entorno virual de desarrollo (venv)*
*Leer junto al scraper*

Debemos crear un archivo nuevo en la carpeta raiz del proyecto llamado scraper.py.

Dentro de este se importaran los modulos requests y lxml, de este ultimo se extraera su funcion html para convertir codigo html y se llamara de la misma forma (html). *(Lineas 1 - 2)*

A continuacion se crearan las constantes a utilizar, en las cuales se almacenaran las expresiones que nos dirigen a los elementos a extraer. *(L 8 - 11)*

Se definen 2 funciones, una para pasar los links (parse_home), otra para correr todo el script (run), esa segunda por ahora estara ejecutando la anterior funcion.

Para trabajar de forma segura se encapsula el codigo en un try-except, si sucede un error al recibir la peticion, por ejemplo, que el estatus sea diferente a 200, entonces manejara el error. En try se guardara la respuesta a la peticion, con requests.get se traera el documneto html de la pagina principal, y si el estatus de la respuesta es igual a 200 entonces una nueva variable home guardara la respuesta decodificada en 'utf-8'.

        *response.content devuelve el html de la respuesta, al agregarle .decode('utf-8') nos aseguramos de transformar los caracteres especiales a unos que python pueda procesar y guardar en los archivos*

A continuacion se crea una nueva variable parsed que toma todo el codigo html
y lo transforma en un documento especial en el que se puede hacer Xpath.
Por ultimo, se crea una ultima variable en la que se ejecuta parsed.xpath pasandole como parametro la constante donde se almacenan los Links.
Ya para finalizar esta prueba, se imprime la anterior variable.
*(L 47 - 68)*

*Si llegase a surgir un error en el que no se envia la misma cantidad de urls que en el navegador, entonces se debe cambiar la expresion //h2/a/@href por //text-fill/a/@href (Actualmente ya se encuentra modificado)*

Luego se creara el entrypoint del archivo de python y se ejecutara al final la funcion "run".*(L 70 - 71)*

### Guardar las noticias en archivos ###

Ahora en el script debemos importar 2 nuevos modulos nativos de py: os y datetime.*(L 3 - 4)*

Se crea una nueva variable "today" luego de "links_to_notices" que albergara la ejecucion del metodo que muestra la fecha actual (datetime.date.today().strftime('%d-%m-%Y')). Lo siguiente que se hara es definir mediante el modulo "os" que si no existe una carpeta con nombre de la fecha actual entonces debera crearla. *(L 56 - 58)*

Ahora se definira una nueva funcion que se encargara de guardar en archivos las noticias, se coloca justo despues de las constantes y se le pone por nombre parse_notice con parametros link y today. *(L 14)*

Antes de crearla, hacemos un ciclo for que defina que por cada link en links_to_notices se ejecute parse_notice con sus respectivos parametros.*(L 60 - 61)*

*Para seguir trabajando de forma segura se encapsula el codigo en un try-except, si sucede un error al recibir la peticion, entonces se manejara de forma idonea. En try se guardara la respuesta a la peticion, con requests.get se traera el documneto html del parametro link, y si el estatus de la respuesta es igual a 200 entonces una nueva variable notice guardara la respuesta decodificada en 'utf-8'. A continuacion se crea una nueva variable parsed que toma todo el codigo html y lo transforma notice en un documento especial en el que se puede hacer Xpath. (L 15 - 44)*

Nuevamente se crea un try-except para encapsular el codigo y manejar algun IndexError saliendo de la funcion con return, en try se canalizan mediante variables cada una de las constantes, que en los primeros dos casos (title y summary) se debe seleccionar el primer elemento de la lista que ofrecen, y por ultimo asegurarnos de que llegue sin comillas algun texto en el titulo usando el metodo .replace('\"','') en title ademas de otras limitantes. *(L 21 - 30)*

Usando el manejador contextual with, que permitira que si el script se rompe, los archivos no se corrompan. Administraremos open, el cual se le debe pasar como parametros una ruta, que este caso sera usar la variable que nos ofrece la fecha actual "today" seguido de nombrar el archivo con la variable title, como siguiente parametro permitiremos la escritura de los archivos, y por ultimo parametro nos aseguramos que la codificacion sea utf-8 (f'{today}/{title}.txt', w, encoding='uft-8')*(L 32)*

Para finalizar, hacemos la plantilla del documento usando f.write() dandole como parametro el elemento que queremos que coloque. Algo a resaltar seria que debemos crear un ciclo for que genere por cada p en la constante body un parrafo seguido de un salto de linea.*(L 33 - 39)*

Guardamos todo el trabajo y ejecutamos el scraper.py

### Todo listo ###
