# ChatGPT Chat Link

<https://chat.openai.com/share/7fdd6ff8-6015-4192-8439-a41cd0e0833a>

Para convertir este script en un servicio de Windows que se ejecute periódicamente en segundo plano y guarde los resultados en un archivo `CSV`, puedes seguir estos pasos:

1. Modifica el Script de Python: Modifica el script para que se ejecute en un bucle y escriba los resultados en un archivo `CSV`.
2. Convierte el Script en un Ejecutable: Utiliza una herramienta como `pyinstaller` para convertir tu script de Python en un ejecutable.
3. Crea un Servicio de Windows: Usa una herramienta como `NSSM` (Non-Sucking Service Manager) para instalar tu ejecutable como un servicio de Windows.
4. Configura el Servicio para que se Ejecute Regularmente: Configura el servicio para que se inicie automáticamente cuando Windows se inicie y para que se ejecute a intervalos regulares.

Para convertir este script en un ejecutable y configurarlo como un servicio, sigue estos pasos adicionales:

1. Instala PyInstaller: Usa `pip install pyinstaller` para instalar PyInstaller.
2. Crea un Ejecutable: Ejecuta `pyinstaller --onefile tu_script.py` en la línea de comandos para crear un ejecutable.
3. Descarga e Instala NSSM: Descarga NSSM desde su sitio web oficial y sigue las instrucciones para instalar tu ejecutable como un servicio.
4. Configura el Servicio: Durante la configuración con `NSSM`, establece el camino al ejecutable y configura el servicio para que se inicie automáticamente.

Ten en cuenta que manejar servicios de Windows y tareas en segundo plano puede requerir derechos de administrador y conocimientos avanzados en administración de sistemas. Además, este enfoque es bastante básico y podría no ser adecuado para entornos de producción o para sistemas críticos.

Primero, para obtener el nombre de la interfaz de red o el `SSID` de la red WiFi, puedes usar la biblioteca `psutil` para conexiones Ethernet y wifi para conexiones WiFi. Instala estas bibliotecas con `pip` si aún no las tienes

## TODO

1. Mejorar documentacion
2. Usar `tqdm` u otra librería para mostar que hay una acción en proceso
3. Filtrar por red a la que está conectada y graficar los datos de las dos redes por separado
4. Validar que no haya internet y decidir si guardar ese registro o no, o inferir la causa por la que no hay internet
