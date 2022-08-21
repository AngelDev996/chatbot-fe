# Proyecto de la clase Teoría de la simulación.
## Chatbot para consulta de servicios financieros


## Deployment

### Para hacer uso de este chatbot, se necesitan herramientas previas instaladas, las cuales son:

- Python en su version 3
- Gestor de paquetes para python como Pip o Anaconda (preferiblemente anaconda)
- Editor de codigo o IDE (preferiblemente Visual Studio Code o Pycharm)

### Se recomienda la creacion de un entorno (venv) para hacer uso de este chatbot

#### Clonar repositorio:
```
git clone https://github.com/AngelDev996/chatbot-fe.git
```

#### Creacion y activacion de entorno con anaconda en Linux:
```
conda create --name proyecto-ts
conda activate proyecto-ts
```

### Instalacion de las dependencias necesarias en el entorno para levantar server e interactuar con el chatbot:

```
conda install pytorch torchvision torchaudio cudatoolkit=10.2 -c pytorch flask nltk

```

### Iniciar el chatbot:
#### Para iniciar el chatbot, entrar a la carpeta chatbot-fe con:
`cd chatbot-fe`
#### El archivo `app.py` es la aplicacion la cual inicia el servidor el cual nos permite interactuar con el chatbot
#### Ejecutar el archivo `app.py` en linux
```
python app.py
```

### Listo! ahora puedes interactuar con el chatbot abriendo en el navegador la direccion [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

### Nota: Si existe un conflicto porque el puerto 5000 ya esta utilizado, cambiar el puerto en la funcion `fetch` del archivo `static/app.js`