Scraper de Noticias de E-Periodico La Republica:

Preparar el proyecto

Inicializamos proyecto en git
Y luego agregamos el modulo de desarrollo de python
<> py -m venv venv </>
Lo siguiente que se realiza es iniciar un entorno virtual
En windows = venv/Scripts/activate
En windows con terminal Unix = source venv/Scripts/activate
En linux y en mac = source venv/bin/activate

(opcional) crear un workspace para llevar un historial de trabajo

Luego se ha de instalar las dependencias a utilizar: Request, LXML y autopep8
<> pip install requests lxml autopep8 </>

//py -m pip install --upgrade pip <- comando para actualizar pip si se necesitara