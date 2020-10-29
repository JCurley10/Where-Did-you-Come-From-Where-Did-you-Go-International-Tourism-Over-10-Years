import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from capstone1_scripts import *

## EDA

#Find the countries with the most, ever, incoming and outgoing tourists to look at their spread 
most_outbound_tourists = merged_inbound_and_outbound_tourists_df.groupby('Country').max('Outgoing_Tourists').sort_values('Outgoing_Tourists', ascending = False).reset_index()
most_out = most_outbound_tourists.head()

most_inbound_tourists_supply = merged_inbound_and_outbound_tourists_df.groupby('Country').max('Value.Ssupply').sort_values('Value.supply', ascending = False).reset_index()
most_inb_supply = most_inbound_tourists_supply.head()

most_inbound_tourists_demand = merged_inbound_and_outbound_tourists_df.groupby('Country').max('Value.demand').sort_values('Value.demand', ascending = False).reset_index()
most_inb_demand = most_inbound_tourists_demand.head()


## Bar graph 5 countries with most outbounds of all time

sns.set_style('whitegrid')

fig, ax = plt.subplots(1, 1, figsize = (18, 8), dpi = 256)

ax.bar(most_out['Country'], most_out['Outgoing_Tourists'], color = 'indianred')
ax.tick_params(axis='both', which='major', labelsize=18)
# ax.set_xlabel('Countries', fontsize = 20)
ax.set_ylabel('Number of Outbound Tourists In 1 Year (in millions)',  fontsize = 20)
ax.set_title('Countries with Most Outbound Tourists in 2018', size = 30)

for idx, data in enumerate(most_out['Outgoing_Tourists']):
    plt.text(x=idx, y = data , s = f"{data: ,.0f}", ha = 'center', fontsize = 20, color = 'black')
plt.tight_layout()
# plt.show()


#Graph these top 5 outbound countries
germany_out = make_df_to_graph('Germany', 'outbound').reset_index()
italy_out =  make_df_to_graph('Italy', 'outbound').reset_index()
france_out =  make_df_to_graph('France', 'outbound').reset_index()
netherlands_out =  make_df_to_graph('Netherlands', 'outbound').reset_index()
sweden_out =  make_df_to_graph('Sweden', 'outbound').reset_index()

sns.set_style('whitegrid')
fig, ax = plt.subplots(1, 1, figsize=(20, 8), dpi = 256)

ax.tick_params(axis='both', which='major', labelsize=16)
ax.set_ylabel('Number of Outgoing Tourists, (in millions)', fontsize = 16 )
# Choose to look at the graph with and without germany 
# ax.plot(germany_out['Year'], germany_out['Outgoing_Tourists'], color = 'indianred', lw = 3, label = 'Germany')
ax.plot(italy_out['Year'], italy_out['Outgoing_Tourists'], color = 'firebrick', ls = 'dashdot',lw = 2, label = 'Italy')
ax.plot(france_out['Year'], france_out['Outgoing_Tourists'], color = 'orangered', ls = 'solid', lw = 2, label = 'France')
ax.plot(netherlands_out['Year'],netherlands_out['Outgoing_Tourists'], color = 'crimson', ls = ":", lw = 3, label = 'Netherlands')
ax.plot(sweden_out['Year'], sweden_out['Outgoing_Tourists'], color = "mediumvioletred", ls = 'dashed', lw = 2, label = 'Sweden')

ax.set_title('Outgoing Tourists Over Time, \n for Countries with the Most Outgoing Tourists in 2018', fontsize = 20)
plt.legend(fontsize = 16)
# plt.savefig('most_outgoing.png')
# plt.show()

# Plot countries with top most inbound of all time 
# the year this occured = 2018

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


# Incoming Tourists Over Time for Countries with the Most Outgoing Tourists in one Year
fig, ax = plt.subplots(1, 1, figsize=(20, 8), dpi = 256)

spain_in = make_df_to_graph('Spain', 'inbound').reset_index()
italy_in = make_df_to_graph('Italy', 'inbound').reset_index()
germany_in = make_df_to_graph('Germany', 'inbound').reset_index()
austria_in = make_df_to_graph('Austria', 'inbound').reset_index()
greece_in = make_df_to_graph('Greece', 'inbound').reset_index()

ax.plot(spain_in['Year'],spain_in['Value'] , color = 'navy', ls = 'dashed', label = 'Spain', marker ='o')
ax.plot(italy_in['Year'], italy_in['Value'], color = 'deepskyblue', ls = 'solid',  label = 'Italy', marker = 'o')
ax.plot(germany_in['Year'], germany_in['Value'], color = 'steelblue', ls = ":", lw = 2, label = 'Germany', marker = 'o')
ax.plot(austria_in['Year'], austria_in['Value'], color = "cadetblue", ls = 'dashdot', label = 'Austria', marker = 'o')
ax.set_title('Incoming Tourists Over Time, \n for Countries with the Most Outgoing Tourists in one Year', fontsize = 20)
plt.legend(fontsize = 14, numpoints = 1);

# Plot 

if __name__ == '__main__':
    # print (countries_with_most_outbound_tourists)
    # print (most_out)
    # print (most_inb_supply)
    # print (most_ind_demand)
    pass

