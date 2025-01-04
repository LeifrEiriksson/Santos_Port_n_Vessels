import openmeteo_requests
import requests_cache
import pandas as pd
from retry_requests import retry

def openmeteo_hourly():

	# Setup the Open-Meteo API client with cache and retry on error
	cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
	retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
	openmeteo = openmeteo_requests.Client(session = retry_session)

	# Make sure all required weather variables are listed here
	# The order of variables in hourly or daily is important to assign them correctly below
	url = "https://api.open-meteo.com/v1/forecast"
	params = {
		"latitude": -23.9608,
		"longitude": -46.3336,
		"hourly": ["temperature_2m", "relative_humidity_2m", "dew_point_2m", "precipitation_probability", "precipitation", "rain", "pressure_msl", "surface_pressure", "visibility", "evapotranspiration", "wind_speed_80m", "wind_speed_120m", "wind_direction_80m", "wind_direction_120m"],
		"daily": ["sunrise", "sunset", "uv_index_max"],
		"timezone": "America/Sao_Paulo",
		"past_days": 2
	}
	responses = openmeteo.weather_api(url, params=params)

	# Process first location. Add a for-loop for multiple locations or weather models
	response = responses[0]

	# Process hourly data. The order of variables needs to be the same as requested.
	hourly = response.Hourly()
	hourly_temperature_2m = hourly.Variables(0).ValuesAsNumpy()
	hourly_relative_humidity_2m = hourly.Variables(1).ValuesAsNumpy()
	hourly_dew_point_2m = hourly.Variables(2).ValuesAsNumpy()
	hourly_precipitation_probability = hourly.Variables(3).ValuesAsNumpy()
	hourly_precipitation = hourly.Variables(4).ValuesAsNumpy()
	hourly_rain = hourly.Variables(5).ValuesAsNumpy()
	hourly_pressure_msl = hourly.Variables(6).ValuesAsNumpy()
	hourly_surface_pressure = hourly.Variables(7).ValuesAsNumpy()
	hourly_visibility = hourly.Variables(8).ValuesAsNumpy()
	hourly_evapotranspiration = hourly.Variables(9).ValuesAsNumpy()
	hourly_wind_speed_80m = hourly.Variables(10).ValuesAsNumpy()
	hourly_wind_speed_120m = hourly.Variables(11).ValuesAsNumpy()
	hourly_wind_direction_80m = hourly.Variables(12).ValuesAsNumpy()
	hourly_wind_direction_120m = hourly.Variables(13).ValuesAsNumpy()

	hourly_data = {"date": pd.date_range(
		start = pd.to_datetime(hourly.Time(), unit = "s", utc = True),
		end = pd.to_datetime(hourly.TimeEnd(), unit = "s", utc = True),
		freq = pd.Timedelta(seconds = hourly.Interval()),
		inclusive = "left"
	)}
	hourly_data["temperature_2m"] = hourly_temperature_2m
	hourly_data["relative_humidity_2m"] = hourly_relative_humidity_2m
	hourly_data["dew_point_2m"] = hourly_dew_point_2m
	hourly_data["precipitation_probability"] = hourly_precipitation_probability
	hourly_data["precipitation"] = hourly_precipitation
	hourly_data["rain"] = hourly_rain
	hourly_data["pressure_msl"] = hourly_pressure_msl
	hourly_data["surface_pressure"] = hourly_surface_pressure
	hourly_data["visibility"] = hourly_visibility
	hourly_data["evapotranspiration"] = hourly_evapotranspiration
	hourly_data["wind_speed_80m"] = hourly_wind_speed_80m
	hourly_data["wind_speed_120m"] = hourly_wind_speed_120m
	hourly_data["wind_direction_80m"] = hourly_wind_direction_80m
	hourly_data["wind_direction_120m"] = hourly_wind_direction_120m

	hourly_dataframe = pd.DataFrame(data = hourly_data)

	return hourly_dataframe