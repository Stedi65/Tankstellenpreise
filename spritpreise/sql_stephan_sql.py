
import pandas as pd

import sqlite3
from sqlite3 import Error

def hole_daten():
    # Daten holen
    dat_name = 'spritpreise.db'
    con = sqlite3.connect(dat_name)
    df = pd.read_sql("SELECT * FROM daten", con)
    return df

def sort_id(df):
    '''
    sortieren nach ID und wirft doppelte raus (Tanksellen ID)
    '''
    print('-20- df1', df)
    df1 = pd.DataFrame()
    df2 = pd.DataFrame()
    df1 = df['id']
    df2 = df1.sort_values(ascending=True)
    df2.drop_duplicates(inplace=True)
    return df2


def sort_zeit(df):
    '''
    sortieren nach Zeit und wirft doppelte raus
    '''
    df1 = pd.DataFrame()
    df2 = pd.DataFrame()
    df1 = df['datetime']
    df2 = df1.sort_values(ascending=True)
    df2.drop_duplicates(inplace=True)
    return df2




def table_sprit_E10(df):
    '''
    # Tabelle Sprint E10
    # erstellt nach Spaltennamen ID
    # erstellt nach Zeilennamen Zeit
    # deshalb vorher die doppelten aussortiert
    '''
    df = pd.DataFrame()
    mask = df['id'].duplicated(keep=False)
    # index der ID nummern
    df[df['id'] == True].index.tolist()


def table_sprit_E5(df):
    pass


def table_sprit_Diesel(df):
    pass
    
    
    
def zusammen_tabellen():
    '''
    die Tabellen E5 / E10 / Disel ... und Id zu Tankstellen Name/Adresse
    in eine neue SQL abspeichern
    '''
    pass

if __name__ == '__main__':
    data = hole_daten()
    data_id = sort_id(data)
    data_zeit = sort_zeit(data)
    id_list(data_id)
    
   


