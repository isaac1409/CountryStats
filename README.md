# CountryStats

## Descripción
**CountryStats** es una aplicación en Python que obtiene datos de países desde la API [REST Countries](https://restcountries.com/), encripta los nombres de los idiomas con SHA1 y genera estadísticas sobre el tiempo de procesamiento. Los datos procesados se almacenan en una base de datos SQLite y en un archivo JSON.

## Características
- Obtención de datos de países y sus idiomas.
- Encriptado de nombres de idiomas utilizando SHA1.
- Cálculo de estadísticas de tiempo de procesamiento.
- Almacenamiento de datos en SQLite.
- Exportación de datos a JSON.
- Test unitarios para validar la funcionalidad.

## Instalación
1. Clonar el repositorio:
    ```bash
    git clone https://github.com/tuusuario/CountryStats.git
    cd CountryStats
    ```

2. Instalar las dependencias:
    ```bash
    pip install -r requirements.txt
    ```

## Uso
Ejecutar el script principal:
```bash
python src/main_script.py
