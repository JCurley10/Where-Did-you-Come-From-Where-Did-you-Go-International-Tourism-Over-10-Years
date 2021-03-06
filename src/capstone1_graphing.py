import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import matplotlib.ticker as ticker
from capstone1_scripts import *

## EDA

'''
# GDP 
'''

#Graph at the total EU GDP over time 
sns.set_style("whitegrid")
total_eu_gdp = gdp_by_years.set_index('Country Name').sum()

fix, ax = plt.subplots(1, 1, figsize =(18, 8), dpi = 256)
ax.plot(total_eu_gdp, color = "green")
ax.tick_params(axis='both', which='major', labelsize=16)
ax.set_ylabel("GDP in Current UDS (in Trillions)", fontsize = 18)
ax.set_title("Total GDP for European Countries Over Time \n in current USD", fontsize = 24)
plt.tight_layout()
# plt.show
plt.savefig('../images/gdp.png')

'''
# TOURISM 
'''

#Find the countries with the most, ever, incoming and outgoing tourists to look at their spread 
most_outbound_tourists = merged_inbound_and_outbound_tourists_df.groupby('Country').max('Outgoing_Tourists').sort_values('Outgoing_Tourists', ascending = False).reset_index()
most_out = most_outbound_tourists.head()

#Find the countries with the most, ever, incoming tourists, coming from the SUPPLY survey to look at their spread
most_inbound_tourists_supply = merged_inbound_and_outbound_tourists_df.groupby('Country').max('Value.Supply').sort_values('Value.supply', ascending = False).reset_index()
most_inb_supply = most_inbound_tourists_supply.head()

#Find the countries with the most, ever, incoming tourists form the DEMAND survey
# I want to include Iceland, which came in 6th
most_inbound_tourists_demand = merged_inbound_and_outbound_tourists_df.groupby('Country').max('Value.demand').sort_values('Value.demand', ascending = False).reset_index()
most_inb_demand = most_inbound_tourists_demand.head(6)


## TO DO: Make the following three graphs into functions to make bar graphs when called 
#for all inbound or outbound, using the above variable dataframes

# ## This makes a Bar graph 5 countries with most outbounds of all time
# (Year occurred in 2018)
sns.set_style('whitegrid')

fig, ax = plt.subplots(1, 1, figsize = (18, 8), dpi = 256)
ax.bar(most_out['Country'], most_out['Outgoing_Tourists'], color = 'indianred')
ax.tick_params(axis='both', which='major', labelsize=18)
# ax.set_xlabel('Countries', fontsize = 20) #probably don't ened this, is self explanatory in the tick labels
ax.set_ylabel('Number of Outbound Tourists In 1 Year (in millions)',  fontsize = 20)
ax.set_title('Countries with Most Outbound Tourists in 2018', size = 30)

for idx, data in enumerate(most_out['Outgoing_Tourists']):
    plt.text(x=idx, y = data , s = f"{data: ,.0f}", ha = 'center', fontsize = 20, color = 'black')
plt.tight_layout()
# plt.show()

## This makes a Bar graph 5 countries with most inbounds of all time
#  coming from the SUPPLY survey (the year this occured = 2018)

sns.set_style('whitegrid')
fig, ax = plt.subplots(1, 1, figsize = (18, 8), dpi = 256)
ax.bar(most_inb_supply['Country'], most_inb_supply['Value.supply'], color = 'cornflowerblue')

ax.tick_params(axis='both', which='major', labelsize=18)
# ax.set_xlabel('Countries', fontsize = 20)
ax.set_ylabel('Number of Inbound Tourists In 1 Year (in millions)',  fontsize = 20)
ax.set_title('Countries with Most Inbound Tourists in 2018', size = 30)

for idx, data in enumerate(most_inb_supply['Value.supply']):
    plt.text(x=idx, y = data , s = f"{data: ,.0f}", ha = 'center', fontsize = 20, color = 'black')
plt.tight_layout()
# plt.show()

''''''
# # ## This makes a Bar graph the countries with most inbounds of all time i
# coming from the DEMAND survey (the year this occured = 2018)

sns.set_style('whitegrid')
fig, ax = plt.subplots(1, 1, figsize = (18, 8), dpi = 256)
ax.bar(most_inb_demand['Country'], most_inb_demand['Value.demand'], color = 'royalblue')

ax.tick_params(axis='both', which='major', labelsize=18)
# ax.set_xlabel('Countries', fontsize = 20)
ax.set_ylabel('Number of Inbound Tourists In 1 Year (in millions)',  fontsize = 20)
ax.set_title('Countries with Most Inbound Tourists in 2018  \n from the Demand survey', size = 30)

for idx, data in enumerate(most_inb_demand['Value.demand']):
    plt.text(x=idx, y = data , s = f"{data: ,.0f}", ha = 'center', fontsize = 20, color = 'black')
plt.tight_layout()
#plt.show()


''''''
## TO DO: Make functions for these plots to graph ANY countries 
## Currently they are set to only take in these partciular countries. 

#Graph these top 3 countries with most outbound percent change, and least outbound cumulative percent change
# Make outbound 
# iceland_out = make_df_to_graph('Sweden', 'outbound').reset_index()
# malta_out = make_df_to_graph ("Malta", 'outbound').reset_index()
# finland_out = make_df_to_graph("Finland", 'outbound').reset_index()

# latvia_out = make_df_to_graph("Latvia", "outbound").reset_index()
# romania_out = make_df_to_graph("Romania", "outbound").reset_index()
# slovak_out = make_df_to_graph("Slovak Republic", "outbound").reset_index()

def graph_tourists_over_time_graph(country_list, indicator, color_list, show = False, save = False):
    '''
    takes in a list of countries and an indicator to 
    plot a graph showing trend over time. 
    It shows or saves the graph depending on the action
    passed in as an argument

    Parameters:
        country_list (lst of str): list of countries to plot 

        indicator (str) : choice are "Inbound" or "Outbound" to search. 

        show (bool): default to False. Change to True
             to show the graph

        save (bool) : default to False. Change to True
            to save the graph 

    Returns:
            None
    '''
    
    sns.set_style('whitegrid')
    fig, ax = plt.subplots(1, 1, figsize=(14, 6), dpi = 256)
    
    ax.tick_params(axis='both', which='major', labelsize=16)
    ax.set_ylabel('Number of Outgoing Tourists, (in millions)', fontsize = 16)


    for country, color in zip(country_list, color_list):
        df = make_df_to_graph(country, indicator).reset_index()
        if indicator == "Outbound":
            ax.plot(df['Year'], df['Outgoing_Tourists'], color = color, lw = 1, label = country)
        elif indicator == "Inbound":
            ax.make_df['Year'], df['Value'], color = color, lw = 1, label = country):

    ax.set_title(f'{} Tourists Over Time', fontsize = 24)
    plt.legend(loc = "best", fontsize = 14)

    if show:
        plt.show()

    elif save:
        plt.savefig(f'../images/{indicator}.png')

''''''




# Analysis

# Functions that make comparison graphs with simple arguments 

# Compare GDP and Country with regplot
def regplot_comparison_graph(country, indicator, color, y_lim = (-.2, 0.5), show = True, save = False):

    '''
    Mkes a scatter plot with linear regression line and confidence interval 
    that compares the GDP and the incoming or outgoing tourists 

    Parameters:

        country (str) : which country to get the comparison of 

        indicator (str) : "inbound" or "outbound". This determines which 
                    percent change DataFrame to pull from
        
        y_lim (tuple of floats) : the y-limit of the window view, 
                    Default to (-.2, 0.5),
        
        color (str) : the color you want to make your country plot

        show (bool) : default to True. Change if you want to show the figure

        save (bool) : default to False. Change if you want to save the figure

     '''
    sns.set_style('whitegrid')
    fig, ax = plt.subplots(1, 1, figsize=(11, 8), dpi = 256)
    ax.tick_params(axis='both', which='major', labelsize=16)
    ax.set_ylim(y_lim)
    ax.axhline(y=0, color = 'grey')

    sns.regplot(x= list(range(2008, 2019)), y = gdp_pct_change.loc[country], ci = None, data = gdp_pct_change, color = "green", label = "percent change of GDP")
    if indicator == "inbound":
        sns.regplot(x = list(range(2008, 2019)), y = pct_change_in.loc[country], ci = None, data = pct_change_in, color = color, label = f"percent change of {indicator} tourists to {country}")
    elif indicator == "outbound":
        sns.regplot(x = list(range(2008, 2019)), y = pct_change_out.loc[country], ci = None, data = pct_change_out, color = color, label = f"percent change of {indicator} tourists from {country}")
    

    # plt.annotate("Potential GDP reporting issue, 2015", xy = (6, -0.02), xytext = (6, -0.08), fontsize = 12, arrowprops =dict(facecolor ='green'))
    ax.set_title(f"Percent Change of GDP Vs. Percent Change of \n {indicator} Tourists - {country}", fontsize = 24)
    ax.set_ylabel("Percent Change, as a decimal, (non-cumulative)", fontsize = 16)
    ax.legend(loc = "upper left", fontsize = 16)
    plt.tight_layout()

    if show: 
        plt.show()
    if save:
        plt.savefig(f"../images/{country}_gdp_{indicator}_reg.png")


# Compare GDP and Country with line graph 

def line_comparison_graph(country, indicator, color, y_lim = (-.2, 0.5), show = True, save = False):

    '''
    Makes two line graphs that compare
    the GDP and the incoming or outgoing tourists 

    Parameters:

        country (str) : which country to get the comparison of 

        indicator (str) : "inbound" or "outbound". This determines which 
                    percent change DataFrame to pull from
        
        y_lim (tuple of floats) : the y-limit of the window view, 
                    Default to (-.2, 0.5),
        
        color (str) : the color you want to make your country plot

        show (bool) : default to True. Change if you want to show the figure

        save (bool) : default to False. Change if you want to save the figure

     '''
    sns.set_style('whitegrid')
    fig, ax = plt.subplots(1, 1, figsize=(18, 8), dpi = 256)
    ax.tick_params(axis='both', which='major', labelsize=16)
    ax.set_ylim(y_lim)
    ax.axhline(y=0, color = 'grey')

    ax.plot(gdp_pct_change.columns, gdp_pct_change.loc[country], color = "green", label = "percent change of GDP")
    
    if indicator == "inbound":
        ax.plot(gdp_pct_change.columns, pct_change_in.loc[country], color = color, label = f"percent change of inbound tourists to {country}")
    
    elif indicator == "outbound":
         ax.plot(gdp_pct_change.columns, pct_change_out.loc[country], color = color, label = f"percent change of outbound tourists from {country}")
        
    
    ax.set_title(f"Percent Change of GDP Vs. Percent Change of \n {indicator} Tourists - {country}", fontsize = 24)
    ax.set_ylabel("Percent Change, as a decimal, (non-cumulative)", fontsize = 16)
    ax.legend(loc = "best" , fontsize = 16)
    
    ## Optional annotate for the 2015 dip
    #plt.annotate("Global GDP dip, 2015", xy = (7, -0.02), xytext = (7, -0.08), fontsize = 12, arrowprops =dict(facecolor ='green'))
    
    plt.tight_layout()
    
    if show: 
        plt.show()
    if save:
        plt.savefig(f"../images/{country}_gdp_{indicator}_line")





''''''




if __name__ == '__main__':
    # print (most_out)
    # print (most_inb_supply)
    # print (most_inb_demand)
    # print (tourists_in_from_demand_graph(show=False, save = True))
    # print (tourists_in_from_supply_graph(show = False, save = True))

    # print (regplot_comparison_graph('Iceland', 'inbound', 'midnightblue', y_lim=(-.2, 0.5), show = False, save = True))
    # print (regplot_comparison_graph('Slovenia', 'inbound', 'indigo', y_lim=(-.2, 0.3), show = False, save = True))
    
    # print (regplot_comparison_graph('France', 'inbound', 'purple', y_lim=(-.2, 0.3), show = False, save = True))
    # print (regplot_comparison_graph('Estonia', 'inbound', 'black', y_lim=(-.2, 0.3), show = False, save = True))
    # print (regplot_comparison_graph('Sweden', 'inbound', 'black', y_lim=(-.2, 0.3), show = False, save = True))
    # print (regplot_comparison_graph('Luxembourg', 'inbound', 'slateblue', y_lim=(-.2, 0.3), show = False, save = True))

    # print (regplot_comparison_graph('Iceland', 'outbound', 'orangered', y_lim=(-.2, 0.3), show = False, save = True))
    # print (regplot_comparison_graph('Malta', 'outbound', 'tomato', y_lim=(-.2, 0.3), show = False, save = True))
    # print (regplot_comparison_graph('Latvia', 'outbound', 'coral', y_lim=(-.2, 0.3), show = False, save = True))
    # print (regplot_comparison_graph('Romania', 'outbound', 'crimson', y_lim=(-.2, 0.3), show = False, save = True))

    # print (line_comparison_graph('France', 'inbound', 'purple', y_lim=(-.2, 0.3), show = False, save = True))
    # print (line_comparison_graph('Slovenia', 'inbound', 'indigo', y_lim=(-.2, 0.3), show = False, save = True))
    # print (line_comparison_graph('Iceland', 'inbound', 'midnightblue', y_lim=(-.2, 0.5), show = False, save = True))
    # print (line_comparison_graph('Iceland', 'outbound', 'orangered', y_lim=(-.2, 0.5), show = False, save = True))
    # print (line_comparison_graph('Malta', 'outbound', 'tomato', y_lim=(-.2, 0.3), show = False, save = True))
    # print (line_comparison_graph('Romania', 'outbound', 'crimson', y_lim=(-.2, 0.3), show = False, save = True))
    
    pass