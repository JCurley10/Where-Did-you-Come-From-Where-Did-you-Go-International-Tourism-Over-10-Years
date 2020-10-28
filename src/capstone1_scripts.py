import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

inbound = pd.read_csv('data/TOURISM_INBOUND_29032020041047359.csv')

#Only relevant columns to be included 
inbound_df = inbound[['Country', 'Variable', 'SOURCE', 'Year', 'Value']]

#List of the union of the countries in the Schengen Region and EU
schen_eu_countries = ['Austria', 'Belgium', 'Czech Republic', 
                    'Denmark', 'Finland', 'France', 'Germany', 
                    'Greece', 'Hungary', 'Iceland', 'Ireland', 
                    'Italy', 'Luxembourg', 'Netherlands', 'Norway', 
                    'Poland', 'Portugal', 'Slovak Republic', 'Spain', 
                    'Sweden', 'Switzerland', 'Bulgaria', 'Croatia', 
                    'Estonia', 'Latvia', 'Lithuania', 'Malta', 
                    'Romania', 'Slovenia']

#DataFrame that includes just the countries from the union of the Schegen Region and EU
schen_eu = inbound_df[inbound_df['Country'].isin(schen_eu_countries)]

#29 countries in total
num_countries = len(schen_eu['Country'].unique())
# Check are the countries from the schen_eu_countries above
countries = schen_eu['Country'].unique() 


def get_tourists_from_source(source, year, variable = 'Overnight visitors (tourists)' , df = schen_eu):
    '''
    Returns a dataframe that only includes the information from the
    SOURCE = 'DEMAND' column from the input dataframe

    Parameters:
        
        source (str): the source from which to collect the data.
            choices are "SUPPLY" or "DEMAND"

        year (int): the year to collect the information from

        variable (str): the description of the tourism data (aka, 'From where) to collect. 
            Default to 'Overnight visitors (tourists)' to represent all  
            overnight travelers, defined here as 'tourists'

        df (pandas DataFrame): the dataframe from which we are getting the values.
            Default to schen_eu

    Returns:
        a pandas Dataframe that includes the information from the DEMAND column 

    '''
    return schen_eu[(schen_eu['SOURCE']==source) & (schen_eu['Year']== year) & (schen_eu['Variable']== variable)].sort_values('Country') 
     
#get 'Overnight visitors (tourists)' from both the supply and demand sources in 2008
tot_tourists_from_supply_08 = get_tourists_from_source('SUPPLY', 2008, variable = 'Overnight visitors (tourists)' , df = schen_eu)

tot_tourists_from_demand_08 = get_tourists_from_source('DEMAND', 2008, variable = 'Overnight visitors (tourists)' , df = schen_eu)

#merge the two sources to see which datasets come from SUPPLY or DEMAND surveys 

overnight_visitors = pd.merge(tot_tourists_from_supply_08, tot_tourists_from_demand_08, on=['Year', 'Variable', 'Country'], 
         suffixes = ['.supply', '.demand'], how = 'outer').sort_values('Country')

#Check that all 29 countries 'Overnight visitors (tourists)' variable as an idicator
overnight_visitors_countries = schen_eu[schen_eu['Variable']=='Overnight visitors (tourists)']['Country'].unique()

''' >> prints ['Austria' 'Belgium' 'Czech Republic' 'Denmark' 'Finland' 'France'
 'Germany' 'Greece' 'Hungary' 'Iceland' 'Ireland' 'Italy' 'Luxembourg'
 'Netherlands' 'Norway' 'Poland' 'Portugal' 'Slovak Republic' 'Spain'
 'Sweden' 'Switzerland' 'Croatia' 'Estonia' 'Latvia' 'Lithuania' 'Malta'
 'Romania' 'Slovenia'] ''' #Missing Bulgaria -- > use the "Total international arrival" from DEMAND as this measure?

#Identify which countires report information from supply and demand surveys 

'''
insert work  here
'''
supply_countries = 
demand_only_countries = 

def get_country_over_time(source, country, variable = 'Overnight visitors (tourists)' , df = schen_eu):

    '''
    Returns a dataframe that only includes the information from the
    SOURCE = 'DEMAND' column from the input dataframe

    Parameters:
        
        source (str): the source from which to collect the data.
            choices are "SUPPLY" or "DEMAND"

        country (str): which country to look at over time

        variable (str): the description of the tourism data (aka, 'From where) to collect. 
            Default to 'Overnight visitors (tourists)' to represent all  
            overnight travelers, defined here as 'tourists'

        df (pandas DataFrame): the dataframe from which we are getting the values.
            Default to schen_eu

    Returns:
        a pandas Dataframe that includes the information from the SOURCE column 

    '''
    return schen_eu[(schen_eu['SOURCE']==source) & (schen_eu['Country']== country) & (schen_eu['Variable']== variable)].sort_values('Year') 


#print the datasets

# for country in schen_eu_countries:
#     if country in supply_countries:
#         for country in supply_countries:
#             print (get_country_over_time('SUPPLY', country, variable = 'Overnight visitors (tourists)' , df = schen_eu))
#             print ('\n')
            
#     elif country in demand_countries:
#         for country in demand_countries:
#             print (get_country_over_time('DEMAND', country, variable = 'Overnight visitors (tourists)' , df = schen_eu))
