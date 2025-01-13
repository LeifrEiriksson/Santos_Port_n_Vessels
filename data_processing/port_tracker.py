import pandas as pd
from datetime import datetime
import requests
from bs4 import BeautifulSoup

def port_calls():

    urls = ('https://www.myshiptracking.com/ports-arrivals-departures/?pid=369','https://www.myshiptracking.com/ports-arrivals-departures/?sort=TIME&page=2&pid=369')
    columns_df = ['ship_name', 'mmsi', 'imo', 'status', 'event', 'port']
    df = pd.DataFrame(columns=columns_df)

    for i in urls:

        data = requests.get(i).text
        soup =  BeautifulSoup(data, 'html.parser')
        table = soup.find_all('tbody')
        op = table[0].find_all('tr')

        for row in op:

            columns = row.find_all('td')

            ship_name = columns[4].find('a').get_text()

            imo_n_mmsi = columns[4].find('a')['href'].split('-')[-4:]
            imo = imo_n_mmsi[-1]
            mmsi = imo_n_mmsi[1]

            status = columns[1].get_text()
            event = columns[2].get_text()
            port = columns[3].get_text().strip()

            tuple_values = (ship_name,mmsi,imo,status,event,port)
            dict_columns = {}

            for j,h in zip(columns_df,tuple_values):

                rows = {j:h}
                dict_columns = {**dict_columns,**rows}

                if len(dict_columns) == 6:

                    df = pd.concat([df, pd.DataFrame([dict_columns])], axis = 0, ignore_index=True) 
    
    return df

def inport():

    urls = ('https://www.myshiptracking.com/inport?sort=TIME&page=1&pid=369','https://www.myshiptracking.com/inport?sort=TIME&page=2&pid=369')
    columns_df = ['ship_name', 'mmsi', 'imo', 'arrived', 'DWT', 'GRT', 'Built', 'Size']
    df = pd.DataFrame(columns=columns_df)

    for i in urls:

        data = requests.get(i).text 
        soup = BeautifulSoup(data, 'html.parser')
        table = soup.find_all('tbody')
        op = table[0].find_all('tr')


        for row in op:

            columns = row.find_all('td')
            ship_name = columns[0].find('a').text.strip()

            mmsi_n_imo = columns[0].find('a')['href'].split('-')[-4:]
            mmsi = mmsi_n_imo[1]
            imo = mmsi_n_imo[-1]

            row_arrived = BeautifulSoup(columns[1].find('span')['title'], 'html.parser').find_all('div')[3].get_text() if columns[1].find('span') != None else None

            DWT = columns[2].get_text()
            GRT = columns[3].get_text()

            Built =  None if columns[4].get_text() == '---' else int(columns[4].get_text())
            Size = None if int(columns[5].get_text()[:-2]) == 0 else int(columns[5].get_text()[:-2])

            tuple_values = (ship_name, mmsi, imo, row_arrived, DWT, GRT, Built, Size)
            dict_columns = {}

            for j,h in zip(columns_df,tuple_values):

                rows = {j:h}
                dict_columns = {**dict_columns,**rows}

                if len(dict_columns) == 8:

                    df = pd.concat([df, pd.DataFrame([dict_columns])], axis = 0, ignore_index=True) 
    
    return df