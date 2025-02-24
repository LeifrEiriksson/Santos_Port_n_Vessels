import sys
import os
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from data_processing.scrapers_center import weather_check
import sqlite3
from prefect import task, flow, get_run_logger
from datetime import timedelta


@task
def fetch_weather_data():
    logger = get_run_logger()
    logger.info("Starting to collect weather data...")
    
    try:
        weather_data = weather_check()
        logger.info("Weather data collected successfully!")
        return weather_data

    except Exception as e:
        logger.error(f"Failed to collect weather data: {e}")
        raise


@task
def save_to_sqlite(weather_data):
    logger = get_run_logger()
    logger.info("Saving weather data to SQLite...")
    
    try:
        db_path = Path(__file__).parent.parent / 'data' / 'raw_pvs.db'
        conn = sqlite3.connect(db_path)
        weather_data.to_sql('weather_data', conn, if_exists='append', index=False)
        conn.commit()
        conn.close()
        logger.info("Weather data saved successfully!")

    except Exception as e:
        logger.error(f"Failed to save weather data to SQLite: {e}")
        raise


@flow(name="Hourly Weather Data Pipeline")
def weather_data_pipeline():

    logger = get_run_logger()
    logger.info("Starting weather data pipeline...")

    weather_data = fetch_weather_data()
    save_to_sqlite(weather_data)

    logger.info("Weather data pipeline completed successfully!")


if __name__ == "__main__":

    weather_data_pipeline().serve(name='Weather_Hourly', cron = '0 * * * *')
