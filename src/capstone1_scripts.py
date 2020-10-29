import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


'''
Inbound Data
'''

inbound = pd.read_csv('../data/TOURISM_INBOUND_29032020041047359.csv')

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

#All possibile "Variables", total = 87
inbound_df.Variable.unique()

#DataFrame that includes just the countries from the union of the Schegen Region and EU
schen_eu_df = inbound_df[inbound_df['Country'].isin(schen_eu_countries)]

#DataFrame that includes only data from Overnight visitors (tourists) variable
all_inbound_tourists_df = schen_eu_df[schen_eu_df['Variable']=='Overnight visitors (tourists)']
# array of all countries in the dataframe, to check membership against
all_countries = all_inbound_tourists_df['Country'].unique()



# Make the DataFrames to display the countries with SOURCE = SUPPLY and SOURCE = DEMAND, separately

#lists of countries per source
countries_in_supply = list(all_inbound_tourists_df[all_inbound_tourists_df["SOURCE"]=='SUPPLY']['Country'].unique())
countries_in_demand =  list(all_inbound_tourists_df[all_inbound_tourists_df["SOURCE"]=='DEMAND']['Country'].unique())
countries_in_demand_only = list(set(countries_in_demand).difference(set(countries_in_supply)))

#all years to consider
all_years = list(range(2008, 2019))   


# Function to Make Relevant DataFrames
def make_inbound_dataframe(source, countries_list, df = all_inbound_tourists_df):
    '''
    Returns a dataframe that only includes the information from the
    desired SOURCE column from the input dataframe
    
    Parameters:
        
        source (lst of str): the source from which to collect the data.
            choices are "SUPPLY" or "DEMAND"

        countries_list (lst): the list of countries to consider 

        df (pandas DataFrame): the dataframe from which we are getting the values.
            Default to all_inbound_tourists_df

    Returns:
        a pandas Dataframe that includes the information from the DEMAND column 
    '''

    return df[(df['SOURCE']==source) & (df['Year'].isin(all_years)) & df['Country'].isin(countries_list)]

# set two dataframes to have the inbound data relevent to the survey 
inbound_supply_df = make_inbound_dataframe('SUPPLY', countries_in_supply)
inbound_demand_df = make_inbound_dataframe('DEMAND', countries_in_demand_only)


####### CHECK THIS AGAIN #####
##### dataframes where countries are indices 
inbound_supply_to_graph = inbound_supply_df.groupby(['Country', 'Year']).sum()
inbound_demand_to_graph = inbound_demand_df.groupby(['Country', 'Year']).sum()

##merge the inbound supply and demand dfs


'''---------------------------------------------------------------'''

'''
Outbound Data
'''

# read in the outbound dataset and rename the value to be outgoing tourists

outbound = pd.read_csv('../data/TOURISM_OUTBOUND_29032020041014703.csv')
outbound_df = outbound[['Country', 'Variable', 'Year', 'Value']]
outbound_df = outbound_df.rename(columns = {"Value": "Outgoing_Tourists"})
pd.options.display.float_format = '{:.2f}'.format

#make the DF with just the important information, where Variable = Overnight visitors (tourists) 
all_outbound_tourists_df = outbound_df[(outbound_df['Country'].isin(schen_eu_countries) 
                        & (outbound_df['Variable']=='Overnight visitors (tourists)'))]

#Make a df with indices == countries 
outbound_to_graph = all_outbound_tourists_df.groupby(['Country', 'Year']).sum()

#make DF to graph outbounds
merged_inbound = pd.merge(inbound_supply_df, inbound_demand_df, on=['Year', 'Variable', 'Country'], 
         suffixes = ['.supply', '.demand'], how = 'outer').sort_values(['Country', 'Year'])

##MAYBE NOT NECESSARY
# Merge the inbound and outbound datasets

merged_inbound_and_outbound_tourists_df = pd.merge(merged_inbound, all_outbound_tourists_df, on=['Year', 'Variable', 'Country'], 
         suffixes = ['.inbound', '.outbound'], how = 'outer').sort_values(['Country', 'Year'])


def get_country_over_time(country, indicator):

    '''
    Returns a dataframe that only includes the information from the
    apropriate column from the input dataframe, given a country name 
    and input dataframe indictaor 

    Parameters:
    
        country (str): which country to look at over time

        df (pandas DataFrame): the dataframe from which we are getting the Values.
            
        indicator (str): indicate which value we are looking at; 
            choices are inbound or outbound
            
    Returns:
    
        a pandas Dataframe that includes the information that 
        country's tourism information, and the SOURCE field
        if indicator == 'inbound'

    '''
    if indicator == 'inbound':
        if country in countries_in_supply:
            df = inbound_supply_df
        elif country in countries_in_demand_only:
            df = inbound_demand_df 
    
    elif indicator == 'outbound':
        df = all_outbound_tourists_df
        
    else:
        return ("Please enter an appropriate Country and/or indicator(inbound or outbound)")
        
    return df[df['Country']==country]


#Make individual dataframes by country to then graph
def make_df_to_graph(country, indicator):

    return get_country_over_time(country, indicator).groupby(['Country', 'Year']).sum()


#Find the Percent Changes of the Tourism graphs

def find_percent_change(indicator, change_type):
    
    '''
    Returns a series of dictionaries whose keys are countries
    and values are the percent change over time of the population
    
    Parameters:
        indicator (str): "inbound" or "outbound" 
                depending on the data we want to observe
        
        change_type (str): "cumulative" or "regular" type 
                of percent change wanted 
    
    Returns:
        percent_dictionary (dict): keys are countries,
            values are the cumulative or noncumulative percent change over time
    '''
    
    percent_dictionary = dict()
        
    if indicator == "inbound":
        for country in all_countries:

            if country in countries_in_supply:
                if change_type == "cumulative":
                    percent_dictionary[country] = inbound_supply_to_graph.loc[country].reset_index()['Value'].pct_change().cumsum()
                elif change_type == "regular":
                    percent_dictionary[country] = inbound_supply_to_graph.loc[country].reset_index()['Value'].pct_change()

            elif country in countries_in_demand_only:
                if change_type == "cumulative":
                    percent_dictionary[country] = inbound_demand_to_graph.loc[country].reset_index()['Value'].pct_change().cumsum()
                elif change_type == "regular":
                    percent_dictionary[country] = inbound_demand_to_graph.loc[country].reset_index()['Value'].pct_change()
        
    elif indicator == "outbound":
        for country in list(all_outbound_tourists_df['Country'].unique()):
            if change_type == "cumulative":
                percent_dictionary[country] = outbound_to_graph.loc[country].reset_index()['Outgoing_Tourists'].pct_change().cumsum()
            elif change_type == "regular":
                percent_dictionary[country] = outbound_to_graph.loc[country].reset_index()['Outgoing_Tourists'].pct_change()
    return percent_dictionary


# To CHECK Print out the dictionary that shows the cumulative percent change of 
# inbound and outbound tourists with country as the key, and percent change
pct_dictionary_in = find_percent_change("inbound", "regular")
# for k, v in dictionary_in.items():
#     print (f'{k}, {v}')
        
pct_dictionary_out = find_percent_change("outbound", "regular")
# for k, v in dictionary_out.items():
#     print (f'{k}, {v}')


## TO DO: Write a function that takes indicator and change_type, and makes the dataframe with the given percent change dictionaries


# Find the country with the highest cumulative percent change inbound and outbound 
# Use these lists to decide who I am going to highlight
#  
#Cumulative inbound df
cumpct_dictionary_in = find_percent_change("inbound", "cumulative")
cum_pct_change_in = pd.DataFrame(cumpct_dictionary_in)
cum_pct_change_in = cum_pct_change_in.rename(index = {0:2008, 1: 2009, 2: 2010, 3:2011, 4:2012, 5:2013, 6:2014, 7:2015, 8:2016, 9:2017, 10:2018})
cum_pct_change_in = cum_pct_change_in.T

#cumulative outbound df
cumpct_dictionary_out = find_percent_change("outbound", "cumulative")
cum_pct_change_out = pd.DataFrame(cumpct_dictionary_out)
cum_pct_change_out = cum_pct_change_out.rename(index = {0:2008, 1: 2009, 2: 2010, 3:2011, 4:2012, 5:2013, 6:2014, 7:2015, 8:2016, 9:2017, 10:2018})
cum_pct_change_out = cum_pct_change_out.T 

# Make dataframes of the percent changes to graph later 
pct_change_in = pd.DataFrame(pct_dictionary_in).rename(index = {0:2008, 1: 2009, 2: 2010, 3:2011, 4:2012, 5:2013, 6:2014, 7:2015, 8:2016, 9:2017, 10:2018}).T
pct_change_out = pct_change_in = pd.DataFrame(pct_dictionary_out).rename(index = {0:2008, 1: 2009, 2: 2010, 3:2011, 4:2012, 5:2013, 6:2014, 7:2015, 8:2016, 9:2017, 10:2018}).T

'''
GDP DATA
'''
#Read in the gdp file 
gdp = pd.read_csv('../data/GDP_Current.csv')

# make a DF with only the necessary rows and columns 
gdp_by_years = gdp.loc[:, ['Country Name','2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018']] 
gdp_by_years = gdp_by_years[gdp_by_years['Country Name'].isin(schen_eu_countries)]

if __name__ == '__main__':

    # print (inbound_df.head())
    # print (all_inbound_tourists_df.columns)
    # print (inbound_supply_df.head())
    # print (inbound_demand_df.head())

    czech_rep_in = make_df_to_graph('Czech Republic', 'inbound').reset_index()
    # print (czech_rep_in)
    czech_rep_out = make_df_to_graph('Czech Republic', 'outbound').reset_index()
    #print (czech_rep_out)
    czech_rep = get_country_over_time('Czech Republic', 'inbound')
    # print (czech_rep)

    # print (outbound_df.head())
    # print (all_outbound_tourists_df.head())
    # print (all_outbound_tourists_df[all_outbound_tourists_df['Country']=='Germany'])
    # print (merged_inbound_and_outbound_tourists_df.columns)

    ## Find the top countries with most percent change of in and outbound tourists
    print ("list of cumulative percent change for incoming tourists:", cum_pct_change_in.max(axis = 1).sort_values(ascending = False))
    # print ("list of cumulative percent change for outgoing tourists", cum_pct_change_out.max(axis = 1).sort_values(ascending = False))

    #print (gdp.head())
    print (gdp_by_years.head())
    
    pass