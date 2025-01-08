# Santos Port and Vessels
## Collecting data about the Port of Santos and vessels, with a simple data engineering project

# Introduction

The objective of this project is to collect and store data on ship movements at the Port of Santos and weather forecasts for the region. The data collection is performed using two main sources:

Ship Movements: Web scraping is used to extract detailed information from the official Port of Santos website. This data includes information about ship arrivals, their status (docked, anchored, etc.), and other operational details. The extraction is performed using the BeautifulSoup library.

Weather Data: Weather forecasts are collected through the OpenMeteo API, with the code provided directly by the platform. The API offers forecasts for the upcoming days, providing information about expected weather conditions, such as temperature, precipitation, and other relevant data.

## Data Storage

For storing the collected data, two database solutions have been chosen:

* SQLite: Used for the bronze layer, which stores raw data. This layer acts as a repository for unprocessed data, ensuring simplicity and efficiency for initial storage.

* DuckDB: Designed for the silver and gold layers, which handle processed and refined data. DuckDB's focus on OLAP workloads makes it ideal for supporting the analytical needs of the project. Its versatility, simplicity, and high efficiency make it an excellent choice for data science and analytics teams.

Although the current data volume is manageable with these solutions, the project is structured with scalability in mind. If the data volume grows significantly, the infrastructure can be adapted to more robust databases, such as PostgreSQL.