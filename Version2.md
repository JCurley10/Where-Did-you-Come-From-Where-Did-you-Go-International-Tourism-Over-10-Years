# Where did you Come From, Where did you go? 
## Investigating International Tourism and GDP to and from European countries from 2008 to 2018


## Table of Contents
- [Background and Motivation](#Background-and-Motivation)
- [Motivation](#Motivation)
- [The Questions](#The-Questions)
- [Key Terms](#Key-Terms)
- [The Data](#The-Data)
- [EDA](#EDA)
- [Analysis](#Analysis)
- [Conclusion and Futher Analysis](#Conclusion-and-Further-Analysis)

## Background and Motivation

<img src="https://github.com/JCurley10/Where-Did-you-Come-From-Where-Did-you-Go-International-Tourism-Over-10-Years/blob/main/images/Paris.JPG" alt="louvre" width="300" height="300"> |
<img src="https://github.com/JCurley10/Where-Did-you-Come-From-Where-Did-you-Go-International-Tourism-Over-10-Years/blob/main/images/Prague.JPG" alt="prague" width="300" height="300"> |
<img src="https://github.com/JCurley10/Where-Did-you-Come-From-Where-Did-you-Go-International-Tourism-Over-10-Years/blob/main/images/slovenia.png" alt="Slovenia" width="300" height="300">  |
<p>(Personal Photos. Location from left to right: The Louvre, Paris; Charles Bridge, Prauge; Ljubliana, Slovenia)
<p>
  
It seems like *everyone* has been traveling to Europe a lot in the past decade. With headlines like [“Overtourism in Europe’s historic cities sparks backlash”](https://www.theguardian.com/world/2020/jan/25/overtourism-in-europe-historic-cities-sparks-backlash)(The Guardian) and [“Should You Visit These Beautiful European Destinations Suffering From Overtourism?](https://www.forbes.com/sites/ceciliarodriguez/2020/01/30/to-go-or-not-to-go-to-these-beautiful-european-places/#657e49fa29e4)(Forbes), it seems like Europe is crumbling under an unsustainable rise in tourism. But, is it true?
It also seems like the econonmic health of Europe has never been better. But is *that* true? And are these two phenonemna related?

I decided to look into the GDP of a country, specifically the rate of change of GDP, and how that relates to the rate of change of incoming tourists to a country, as well as outgoing tourists from a country.


## The Questions

- Which countries saw the greatest rate of change (positive and negative, if any), and least change, for both incoming and outgoing international travelers between 2008 and 2018?

- How does the rate of change of GDP of a country correlate to both the incoming-tourists rates to that country, and outgoing-tourist rates from that country?

While I will not be able to make any conclusions about the relationship between GDP and tourist rates-of-change, I am interested in their correlation as a start to a deeper investigation of tourism indicators. 

## Key Terms and Definitions

- **European Countries**: Throughout this project are defined as the union of countries from the Schengen region and the EU, which are the following 28 countries<sup>1</sup> (in no particular order): ```Austria, Belgium, Czech Republic, Denmark, Finland, France, Germany, Greece, Hungary, Iceland, Ireland, Italy, Luxembourg, Netherlands, Norway, Poland, Portugal, Slovak Republic, Spain, Sweden, Switzerland, Croatia, Estonia, Latvia, Lithuania, Malta, Romania, and Slovenia.``` 
- **Tourism** can be regarded as a social, cultural and economic phenomenon related to the movement of people outside their usual place of residence. Tourism refers to the activity of visitors. 
- **A visitor** is a traveller taking a trip to a main destination outside his/her usual environment, for less than a year, for any main purpose (business, leisure or other personal purpose) other than to be employed in the country or place visited. 
- **A tourist** is a visitor if his/her trip includes an overnight stay; otherwise, a visitor is classified as a same-day visitor (or excursionist). 
- **Inbound tourism** comprises the activities of a non-resident visitor within the country of reference. <sup>2</sup>
- For the purpose of this analysis, I looked at the number of tourists ("Value") described by the variable **"Overnight visitors (tourists)"**  in the Inbound Tourism and Outbound Tourism datasets.
 

## The Data

### The data I used come from three separate datasets: Inbound Tourists, Outbound Tourists, and GDP (Current USD)

### Inbound and Outbound Tourists: 
The datasets I used come from the [Inbound Tourism and Outbound Tourism sets](https://www.kaggle.com/nubatama/tourism-inout-statdata-from-oecd) from Kaggle.com. The [original data](https://stats.oecd.org/Index.aspx?QueryId=95071) come from published queries from their respective datasets from the OECD, the Organisation for Economic Co-operation and Development which is an international organization that collects and provides data publicly to support evidence-based policy across the globe.

#### Important Features of the Data Sets 
- The ```Variable``` column had 87 total indicators such as ```Total International Arrivals```, ```Nights in all types of accommodation```, ```Same-day visitors (excursionists)```, or a country name to indicate where the tourists came from. I only used the information from the ```Overnight visitors (tourists)``` rows as the definition aligned with my research. 
- the ```Value``` represents the total population of the "Variable" indicator. For the purposes of this study, they are the total incoming tourists to the country in the ```Country``` column.
- The ```source```column represents from which survey the data was collected. Some countries had collected data in both ```Tourism supply surveys``` or ```Tourism demand surveys```. I looked at tourism data from one survey per country depending on availability, and only compared incoming tourists in countries grouped by source survey.<sup>3</sup>. 
    
    
**A brief look at the raw data from the Inbound Tourism Dataset**

|      | COUNTRY | Country |                     VARIABLE |                        Variable | SOURCE |                 Source | YEAR | Year |   Value | Flag Codes | Flags |
|------|--------:|--------:|-----------------------------:|--------------------------------:|-------:|-----------------------:|-----:|-----:|--------:|-----------:|------:|
| 1541 | ISL     | Iceland | INB_ACCOMM_OTHER_COLL_NIGHTS | Other collective establishments | SUPPLY | Tourism supply surveys | 2013 | 2013 | 812325  | NaN        | NaN   |
| 1542 | ISL     | Iceland | INB_ACCOMM_OTHER_COLL_NIGHTS | Other collective establishments | SUPPLY | Tourism supply surveys | 2014 | 2014 | 1106718 | NaN        | NaN   |
| 1543 | ISL     | Iceland | INB_ACCOMM_OTHER_COLL_NIGHTS | Other collective establishments | SUPPLY | Tourism supply surveys | 2015 | 2015 | 1259951 | NaN        | NaN   |


#### A look at a cleaned Inbound dataset for inbound tourists to Iceland, by inbound country and source

|      | Country | Variable                      | SOURCE | Year | Value   |
|------|---------|-------------------------------|--------|------|---------|
| 1571 | Iceland | Overnight visitors (tourists) | DEMAND | 2013 |  807349 |
| 1572 | Iceland | Overnight visitors (tourists) | DEMAND | 2014 |  997556 |
| 1573 | Iceland | Overnight visitors (tourists) | DEMAND | 2015 | 1289139 |

* **Value** represents total incoming tourists

#### A look at a cleaned Outbound dataset for outbound tourists from Iceland<sup>*</sup>, by origin country

|     | Country | Variable                      | Year | Outgoing_Tourists |
|-----|---------|-------------------------------|------|-------------------|
| 140 | Iceland | Overnight visitors (tourists) | 2013 |         381675.00 |
| 141 | Iceland | Overnight visitors (tourists) | 2014 |         413291.00 |
| 142 | Iceland | Overnight visitors (tourists) | 2015 |         467437.00 |
- <sup>*</sup> *Interesting, these numbers are greater than the total population of Iceland. Hmm...*

### GDP
- The data for the GDP come form the dataset [GDP in Current USD](https://data.worldbank.org/indicator/NY.GDP.MKTP.CD) from the World Bank
- The GDP is in current USD, for the purpose of consistency


#### A brief look at the cleaned GDP Dataset with only the relevant countries and years 

|      | Country | 2008            | 2009            | 2010            | 2011            | 2012            | 2013            | 2014            | 2015            | 2016            | 2017            | 2018            |
|------|---------|-----------------|-----------------|-----------------|-----------------|-----------------|-----------------|-----------------|-----------------|-----------------|-----------------|-----------------|
| 1220 | Austria | 430000000000.00 | 400000000000.00 | 392000000000.00 | 431000000000.00 | 409000000000.00 | 430000000000.00 | 442000000000.00 | 382000000000.00 | 395000000000.00 | 418000000000.00 | 456000000000.00 |
|   15 | Belgium | 515000000000.00 | 481000000000.00 | 481000000000.00 | 523000000000.00 | 496000000000.00 | 522000000000.00 | 535000000000.00 | 462000000000.00 | 476000000000.00 | 504000000000.00 | 543000000000.00 |


## EDA 

### General Trends of Inbound and Outbound data

#### Looking at the the trend of the countries that reported the most inbound or outbound tourist numbers ever reported. (It turned out, all the highest inbound tourism numbers came from 2018!)

<img src="https://github.com/JCurley10/Where-Did-you-Come-From-Where-Did-you-Go-International-Tourism-Over-10-Years/blob/main/images/most_incoming_supply.png" alt="most_incoming_supply" >

<img src = "https://github.com/JCurley10/Where-Did-you-Come-From-Where-Did-you-Go-International-Tourism-Over-10-Years/blob/main/images/most_incoming_demand.png" alt = "incoming_no_france">

#### France is a major outlier. Let's see these values without France.

<img src = "https://github.com/JCurley10/Where-Did-you-Come-From-Where-Did-you-Go-International-Tourism-Over-10-Years/blob/main/images/most_incoming_demand_no_france.png" alt = "most_incoming_demand">

<img src = "https://github.com/JCurley10/Where-Did-you-Come-From-Where-Did-you-Go-International-Tourism-Over-10-Years/blob/main/images/most_outgoing.png" alt = "most_outgoing">

#### Germany is a major outlier. Let's see these values without Germany

<img src = "https://github.com/JCurley10/Where-Did-you-Come-From-Where-Did-you-Go-International-Tourism-Over-10-Years/blob/main/images/most_outgoing_no_germany.png" alt = "outgoing_no_germany">

### GDP over time
#### The cumulative GDP for the 28 European countries examined in this study 
<img src = "https://github.com/JCurley10/Where-Did-you-Come-From-Where-Did-you-Go-International-Tourism-Over-10-Years/blob/main/images/gdp.png" alt = "GDP">

## Analysis 

### Percent Change
- Because of population difference, I chose to look at relative changes (percent change) over time to compare a country's tourism rates and GDP. Particularly at yearly percent change. 
- Most economic measures are reported in percent change, so this analysis aligns with how tourism and GDP are often reported. 
- The information in the tables below show **Cumululative Percent Change**, of outbound and inbound tourism and GDP, ordered from positive to negative
- Two countries form the top and bottom of the tables reflecting tourism change were selected for furhter analysis. 

<table>
  
<tr><th>Percent Change of Outbound Tourists</th><th>Percent Change of Inbound Tourists</th><th>Percent Change of GDP</th></tr>

<tr><td>
  
| Country         | Cum. Pct. Change |
|-----------------|------------------|
| Iceland         | 1.00             |
| Malta           | 0.99             |
| Finland         | 0.91             |
| Luxembourg      | 0.68             |
| Poland          | 0.64             |
| Belgium         | 0.45             |
| Switzerland     | 0.45             |
| Spain           | 0.41             |
| Sweden          | 0.41             |
| Hungary         | 0.39             |
| Portugal        | 0.34             |
| Lithuania       | 0.31             |
| Germany         | 0.29             |
| Slovenia        | 0.28             |
| Italy           | 0.24             |
| Ireland         | 0.22             |
| Austria         | 0.22             |
| Netherlands     | 0.21             |
| Estonia         | 0.20             |
| Denmark         | 0.19             |
| Croatia         | 0.13             |
| Norway          | 0.10             |
| France          | 0.07             |
| Czech Republic  | 0.02             |
| Bulgaria        | 0.01             |
| Slovak Republic | -0.08            |
| Romania         | -0.13            |
| Latvia          | -0.23            |

</td><td>

| Country         | Cum. Pct. Change |
|-----------------|------------------|
| Iceland         | 1.75             |
| Slovenia        | 0.87             |
| Latvia          | 0.80             |
| Malta           | 0.75             |
| Romania         | 0.69             |
| Croatia         | 0.68             |
| Greece          | 0.66             |
| Netherlands     | 0.65             |
| Portugal        | 0.61             |
| Poland          | 0.59             |
| Czech Republic  | 0.49             |
| Germany         | 0.46             |
| Denmark         | 0.44             |
| Lithuania       | 0.44             |
| Italy           | 0.43             |
| Hungary         | 0.37             |
| Austria         | 0.35             |
| Slovak Republic | 0.33             |
| Spain           | 0.32             |
| Switzerland     | 0.32             |
| Finland         | 0.29             |
| Ireland         | 0.28             |
| Belgium         | 0.17             |
| Luxembourg      | 0.17             |
| Norway          | 0.15             |
| Estonia         | 0.14             |
| France          | 0.12             |
| Sweden          | -0.06            |

</td><td>
  
| Country Name    | Cum. Pct. Change |
|-----------------|------------------|
| Malta           | 0.15             |
| Estonia         | 0.14             |
| Romania         | 0.14             |
| Ireland         | 0.14             |
| Czech Republic  | 0.13             |
| Latvia          | 0.13             |
| Lithuania       | 0.12             |
| Poland          | 0.12             |
| Slovenia        | 0.11             |
| Hungary         | 0.11             |
| Slovak Republic | 0.11             |
| Luxembourg      | 0.10             |
| Croatia         | 0.10             |
| Netherlands     | 0.10             |
| Austria         | 0.09             |
| Portugal        | 0.09             |
| Norway          | 0.09             |
| Spain           | 0.08             |
| Finland         | 0.08             |
| Denmark         | 0.08             |
| Belgium         | 0.08             |
| Germany         | 0.08             |
| France          | 0.07             |
| Greece          | 0.07             |
| Italy           | 0.07             |
| Iceland         | 0.05             |
| Switzerland     | 0.04             |
| Sweden          | 0.03             |  
</td></tr> </table>

### Tourism Vs. GDP

### Outbound Tourism vs. GDP 
- The following eight graphs show the **percent change** of outbound or inbound tourism and percent change of GDP, both being relative to the previous year. <p>
- This means that any point above the zero represents growth in that year compared to the previous year.

#### Iceland and Malta had high cumulative percent change over time in outbound tourists
<img src = "https://github.com/JCurley10/Where-Did-you-Come-From-Where-Did-you-Go-International-Tourism-Over-10-Years/blob/main/images/Iceland_gdp_outbound_reg.png" alt = "iceland_out_gdp">

<img src = "https://github.com/JCurley10/Where-Did-you-Come-From-Where-Did-you-Go-International-Tourism-Over-10-Years/blob/main/images/Malta_gdp_outbound_reg.png" alt = "malta_out">

#### Romania and Latvia had negative cumulative percent change in outgoing tourists

<img src = "https://github.com/JCurley10/Where-Did-you-Come-From-Where-Did-you-Go-International-Tourism-Over-10-Years/blob/main/images/Romania_gdp_outbound_reg.png" alt = "romania_out">

<img src = "https://github.com/JCurley10/Where-Did-you-Come-From-Where-Did-you-Go-International-Tourism-Over-10-Years/blob/main/images/Romania_gdp_outbound_line.png" alt = "romania_line">

<img src = "https://github.com/JCurley10/Where-Did-you-Come-From-Where-Did-you-Go-International-Tourism-Over-10-Years/blob/main/images/Latvia_gdp_outbound_reg.png" alt = "latvia_out">

### Inbound Tourism Vs. GDP

#### Iceland and Slovenia had a high cumulative percent change over time in inbound tourist counts

<img src = "https://github.com/JCurley10/Where-Did-you-Come-From-Where-Did-you-Go-International-Tourism-Over-10-Years/blob/main/images/Iceland_gdp_inbound_reg.png" alt = "iceland_in_gdp">

<img src = "https://github.com/JCurley10/Where-Did-you-Come-From-Where-Did-you-Go-International-Tourism-Over-10-Years/blob/main/images/Slovenia_gdp_inbound_reg.png" alt = "slovenia_in">

#### France and Luxembourg had a very low cumulative percent change over time in inbound tourist counts
(Sweden, Estonia, Norway did not have enough data reported to compare to GDP)
<img src = "https://github.com/JCurley10/Where-Did-you-Come-From-Where-Did-you-Go-International-Tourism-Over-10-Years/blob/main/images/France_gdp_inbound_reg.png" alt = "france_in">

<img src =https://github.com/JCurley10/Where-Did-you-Come-From-Where-Did-you-Go-International-Tourism-Over-10-Years/blob/main/images/Luxembourg_gdp_inbound_reg.png alt = "lux_in">

Another look at Iceland, both inbound and outbound 
<img src = "https://github.com/JCurley10/Where-Did-you-Come-From-Where-Did-you-Go-International-Tourism-Over-10-Years/blob/main/images/iceland_gdp_inbound_line.png" alt = "iceland_in_line" >

<img src = "https://github.com/JCurley10/Where-Did-you-Come-From-Where-Did-you-Go-International-Tourism-Over-10-Years/blob/main/images/Iceland_gdp_outbound_line.png" alt = "iceland_out_line"  >

## Conclusion and Further Analysis

### Conclusions
- In the seven countries investigated above, there appears to be a relationship between the rate of change of GDP and Inbound tourism:
  - The countries that had the most positive cumulative percent change in outbound or inbound tourists saw similar trends between percent change in tourism and precent change in GDP.
  - Countries with a smaller cumulative percent change in tourism over time also saw a consistently flat year-on-year percent change in GDP (percent change that hover around 0)
- Iceland, whose tourism increased the most (both inbound and outbound), did not have a very high cumulative GDP percent change. Iceland is a unique country for other reasons including having a very small population, and a boom in popularity after the 2011 volcano erpution. 
- The source data  was difficult to manage, as each country may report toursim information differently, and there is no perfect way to count *real* tourists entering or leaving a country. I  would like to get more information on exactly how the inbound and outbound data were collected beyond the brief descriptions on the OECD website.

### Further Analysis:
* It would be interesting to compare the actual tourism and GDP percent growth correlations of all countries investigated in the percent change. 
* It would be valuable to compare the change in per-capita GDP to tourist rates by population in the future
* It would be interesting to look at more than just GDP as a comparitive measure against tourism numbers (See Iceland!) 

----

<sup>1</sup> Bulgaria would technically fit this description, but there was limited data on incoming tourists from Bulgaria in the data <p>
<sup>2</sup> Defintions taken from [stats.oecd.org](https://stats.oecd.org) <p>
 <sup>3</sup> Notes on the Source data in the "Incoming Tourists" Dataset: 
  - In my analysis, I chose the ```SOURCE``` column as it was less to type.
  - After digging into the type of information collected in the different surveys (Supply or Demand), there was a clear difference in the reported numbers of travelers depending on which survey was used. There is, however, consistency among countries within one type of survey reported. While some countries had reported information from both surveys, others did not. Therefore, I used my discretion and will used the information first from the Supply source. If the country did not report Supply data, I used the Demand source. 
    - Countries whose data come from the Tourism SUPPLY surveys, grouped under ```SUPPLY ```: Austria, Belgium, Czech Republic, Finland, Germany, Greece, Hungary, Italy, Luxembourg, Netherlands, Norway, Poland, Portugal, Slovak Republic, Spain, Switzerland, Bulgaria, Croatia, Estonia, Latvia, Lithuania, Romania, and Slovenia```
    - Countries whose data come from the Tourism DEMAND surveys, grouped under  ```DEMAND```: ```Denmark, France, Iceland, Ireland, Malta, Sweden```