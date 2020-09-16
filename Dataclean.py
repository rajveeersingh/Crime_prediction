import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from datetime import datetime as dt

class Dataclean:
    # load data
    df = pd.read_csv('/home/superadmin/DBDA/project/chicago/2003_Ward_Dataset_CSV_Crimes_-_2001_to_present/Crimes_-_2001_to_present.csv',index_col='ID',parse_dates=['Date'])

    #change the colome name
    df.rename(columns={'Primary Type':'crime_type',
                   'Location Description':'Area_name',
                   'Community Area':'Area'},inplace=True)
	
    # checking missing na values from dataframe 
    print("crime",sum(df['crime_type'].isna()))
    print("location",sum(df['Area_name'].isna()))
    print("arrest",sum(df['Arrest'].isna()))
    print("ward",sum(df['Ward'].isna()))
    print("year",sum(df["Year"].isna()))

    #removing the Na/Null values from dataframe and replacing with mode
    df['Area_name'] = df['Area_name'].fillna(df['Area_name'].mode()[0])
    df['Ward'] = df['Ward'].fillna(df['Ward'].mode()[0])


    #selecting the colomn are to be used in newdata set for the model
    xf = ['Case Number','Date','crime_type','Description','Area_name','Arrest','Domestic','District','Ward','Year']
    pf = df[xf]

    # Writing new Clean dataset file
    pf.to_csv('/home/superadmin/DBDA/project/My_Project/Crime_new.csv',index=False)



    
# load_data()
