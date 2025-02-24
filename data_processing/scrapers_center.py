import data_processing.port_n_vessels as port
import data_processing.weather as weather
import data_processing.port_tracker as tracker

def crawler_check():
    try:
        return port.crawler()

    except Exception as err:
        return err

def weather_check():
    try:
        return weather.openmeteo_hourly()

    except Exception as err:
        return err

def port_calls_check():
    try:
        return tracker.port_calls()

    except Exception as err:
        return err
        
def berthed_v1_check():
    try:
        return tracker.inport() 

    except Exception as err:
        return err


