# Santos Port and Vessels
## Collecting data about the Port of Santos and vessels, with a simple data engineering project

# Introduction

The objective of this project is to collect and store data on ship movements at the Port of Santos and weather forecasts for the region. The data collection is done through two main sources:

Ship Movements: Web scraping is used to extract detailed information from the official Port of Santos website. This data includes information about ship arrivals, their status (docked, anchored, etc.), and other operational details. The extraction is performed using the BeautifulSoup library.

Weather Data: Weather forecasts are collected through the OpenMeteo API, with the code provided directly by the platform. The API offers forecasts for the upcoming days, providing information about expected weather conditions, such as temperature, precipitation, and other relevant data.

## Data Storage

For storing the collected data, DuckDB has been chosen. DuckDB is a database solution that, while more geared towards OLAP projects, offers good performance for the current data volume and allows efficient processing of the **raw** data layer. The choice of DuckDB is motivated by its versatility, efficiency, and high availability for data science and analytics teams.

Although the data volume is not large at the moment, the project is structured to allow future scalability if the data processing needs grow significantly. If necessary, the infrastructure can be scaled to more robust databases like PostgreSQL.