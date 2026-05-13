import requests
import logging

from config import (
    BASE_URL, LATITUDE, LONGITUDE,
    START_DATE, END_DATE, TIMEZONE
)

def get_weather_data():
    url = (
        f"{BASE_URL}"
        f"?latitude={LATITUDE}"
        f"&longitude={LONGITUDE}"
        f"&start_date={START_DATE}"
        f"&end_date={END_DATE}"
        f"&hourly=temperature_2m,precipitation"
        f"&timezone={TIMEZONE}"
    )

    try:
        logging.info("Requesting weather data...")

        response = requests.get(url, timeout=10)
        response.raise_for_status()  # 200 - git, 404 - no page, 500 - błąd serwera, 403 - brak dostępu

        data = response.json()

        if "hourly" not in data:
            logging.error("Invalid API response structure")
            return None

        logging.info("Weather data fetched successfully")
        return data
    
    except requests.exceptions.Timeout:
        logging.error("API request timed out")
        return None

    except requests.exceptions.ConnectionError:
        logging.error("Connection error")
        return None

    except requests.exceptions.HTTPError as e:
        logging.error(f"HTTP error: {e}")
        return None

    except ValueError:
        logging.error("Failed to parse JSON")
        return None

    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        return None