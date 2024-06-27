import pandas as pd
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, DateTime, Float
from sqlalchemy.exc import SQLAlchemyError

def create_dataframe ():
    df = pd.read_csv('Online_Sales_Data.csv')
    return df

def transform_dataframe(df):

    df['Date'] = pd.to_datetime(df['Date'])
    df['average_revenue_per_unit'] = df['Total Revenue'] / df['Units Sold'] 

    new_columns_names ={
        'Transaction ID' : 'transaction_id',
        'Date' : 'date',
        'Product Category' : 'product_category',
        'Product Name' : 'product_name',
        'Units Sold' : 'units_sold',
        'Unit Price' : 'unit_price',
        'Total Revenue' : 'total_revenue',
        'Region' : 'region',
        'Payment Method' : 'payment_method'
            }
    df = df.rename(columns=new_columns_names) 

    return df

def upload_table(df):

    DATABASE = 'postgresql+psycopg2://postgres:password@localhost:5432/DB_VivVidero'

    try:
        engine = create_engine(DATABASE, echo = True)

        metadata = MetaData()

        sales = Table('sales', metadata,
            Column('transaction_id', Integer, primary_key = True),
            Column('date', DateTime),
            Column('product_category', String (length = 80)),
            Column('product_name', String (length = 80)),
            Column('units_sold', Integer),
            Column('unit_price', Float),
            Column('total_revenue', Float),
            Column('region', String (length = 80)),
            Column('payment_method', String (length = 80)),
            Column('average_revenue_per_unit', Float)
        )

        metadata.create_all(engine)

        df.to_sql('sales', engine, if_exists='append', index = False)
        print('Dataframe subido correctamente')
    except SQLAlchemyError as e:
        print(f'Error al subir el Dataframe: {e}')

def main():
    df_initial = create_dataframe()
    df_transformed = transform_dataframe(df_initial)
    upload_table(df_transformed)

if __name__ == "__main__":
    main()