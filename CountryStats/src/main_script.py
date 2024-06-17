# src/main_script.py

import pandas as pd
import requests
import hashlib
import time
import sqlite3
import json
from typing import Dict, List, Tuple
import logging

# Configurar logging
logging.basicConfig(level=logging.INFO)

def fetch_country_data(url: str) -> List[Dict]:
    """Obtiene datos de países desde la API."""
    try:
        response = requests.get(url)
        response.raise_for_status()  # Lanza una excepción si la respuesta contiene un error
        return response.json()
    except requests.RequestException as e:
        logging.error(f"Error fetching data: {e}")
        return []

def process_country_data(data: List[Dict]) -> Tuple[List[str], List[str], List[str], List[float]]:
    """Procesa datos de países y retorna listas para DataFrame."""
    countries, languages, hashes, times = [], [], [], []
    
    for country in data:
        country_name = country.get('name', {}).get('common', 'Unknown')
        language = next(iter(country.get('languages', {}).values()), 'Unknown')

        start_time = time.time()
        language_hash = hashlib.sha1(language.encode()).hexdigest()
        end_time = time.time()

        processing_time = end_time - start_time

        countries.append(country_name)
        languages.append(language)
        hashes.append(language_hash)
        times.append(processing_time)
    
    return countries, languages, hashes, times

def create_dataframe(countries: List[str], languages: List[str], hashes: List[str], times: List[float]) -> pd.DataFrame:
    """Crea un DataFrame con los datos procesados."""
    return pd.DataFrame({
        'Country': countries,
        'Language': languages,
        'Language_Hash': hashes,
        'Time': times
    })

def save_to_sqlite(df: pd.DataFrame, db_name: str, table_name: str):
    """Guarda el DataFrame en una base de datos SQLite."""
    with sqlite3.connect(db_name) as conn:
        df.to_sql(table_name, conn, if_exists='replace', index=False)
    logging.info(f"Data saved to {db_name} in table {table_name}.")

def save_to_json(df: pd.DataFrame, file_name: str):
    """Guarda el DataFrame en un archivo JSON."""
    df.to_json(file_name, orient='records', lines=True)
    logging.info(f"Data saved to {file_name}.")

def main():
    url = "https://restcountries.com/v3.1/all"
    data = fetch_country_data(url)

    if not data:
        logging.error("No data fetched. Exiting program.")
        return

    countries, languages, hashes, times = process_country_data(data)

    df = create_dataframe(countries, languages, hashes, times)

    total_time = df['Time'].sum()
    average_time = df['Time'].mean()
    min_time = df['Time'].min()
    max_time = df['Time'].max()

    logging.info(f"Tiempo total: {total_time} segundos")
    logging.info(f"Tiempo promedio: {average_time} segundos")
    logging.info(f"Tiempo mínimo: {min_time} segundos")
    logging.info(f"Tiempo máximo: {max_time} segundos")

    save_to_sqlite(df, 'countries.db', 'countries')
    save_to_json(df, 'data.json')

    logging.info("Datos procesados y guardados correctamente.")

if __name__ == "__main__":
    main()
