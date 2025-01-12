import requests
import pandas as pd
import httpx
from bs4 import BeautifulSoup

infos = {
'scheduled' : {
'url': "https://www.portodesantos.com.br/informacoes-operacionais/operacoes-portuarias/navegacao-e-movimento-de-navios/atracacoes-programadas/",
'columns':['Date','Hour','ETA','Place','Ship','IMO','Cargo','Event','Voyage','DUV'],
'df' : None
},

'foreseen_cargo' : {
'url':"https://www.portodesantos.com.br/informacoes-operacionais/operacoes-portuarias/navegacao-e-movimento-de-navios/navios-esperados-carga/",
'columns':['Ship','Flag','Draft','Nav','Arrival','Notice','Office','Operation','Goods','Weight','Voyage','DUV','P','Terminal','IMO'],
'df' : None
},

'foreseen_cruise' : {
'url':"https://www.portodesantos.com.br/informacoes-operacionais/operacoes-portuarias/navegacao-e-movimento-de-navios/navios-esperados-passageiros/",
'columns':['Ship','Flag','Draft','Nav','Arrival','Notice','Office','Voyage','DUV','P','Terminal'],
'df' : None
},

'berthage_ships' : {
'url':"https://www.portodesantos.com.br/informacoes-operacionais/operacoes-portuarias/navegacao-e-movimento-de-navios/navios-fundeados/",
'columns':['Ship','Flag','Draft','Nav','Arrival','Notice','Office','Operat','Type','Weight','Voyage','P','Terminal'],
'df' : None
},

'berthed_ships' : {
'url':"https://www.portodesantos.com.br/informacoes-operacionais/operacoes-portuarias/navegacao-e-movimento-de-navios/atracados-porto-terminais/",
'columns':['Place','Ship','Cargo','Unload','Load'],
'df' : None
},
}

def crawler():

    infos_dict = dict(infos)

    for key, value in infos_dict.items():

        table = None
        op = None

        url = value['url']
        columns_df = value['columns']

        data = requests.get(url, verify=False).text
        soup = BeautifulSoup(data, 'html.parser')

        if key != 'berthed_ships':
            table = soup.find_all('tbody')

        else:
            table = soup.find('table', {'id':'atracados'})

        df = pd.DataFrame(columns = columns_df)

        for i in range(len(table)):

            if key != 'berthed_ships':
                op = table[i].find_all('tr')

            else:
                op = table.tbody.find_all('tr')

            for row in op:

                columns = row.find_all('td')

                if(columns != []):

                    dict_merge = {}

                    for j in range(len(columns_df)):

                        if key != 'berthed_ships':

                            row = {
                                columns_df[j]: columns[j].text.strip()
                            }

                        else:

                            columns_index = (0,1,6,7,8)

                            index_column = columns_index[j]

                            row = {
                                columns_df[j]: columns[index_column].text.strip()
                            }

                        dict_merge = {**dict_merge, **row}

                    df = pd.concat([df, pd.DataFrame([dict_merge])], axis = 0, ignore_index=True) 

        value['df'] = df 

    return infos_dict