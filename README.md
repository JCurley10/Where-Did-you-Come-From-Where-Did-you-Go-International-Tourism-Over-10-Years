# Where did you Come From, Where did you go? International Tourism Over 10 Years, with a focus on European Countries
## Investigating International Tourism to and from European countries over 2008 - 2018, and the relationship to GDP and world events

## Table of Contents
- [Background](#Background)
- [Motivation](#Motivation)
- [The Questions](#The-Questions)
- [Key Terms](#Key-Terms)
- [The Data](#The-Data)
- [EDA](#EDA)
- [Analysis](#Analysis)
- [Conclusion and Futher Analysis](#Conclusion-and-Further-Analysis)

## Background

With the rise of Instragram and the "wanderlust" hashtag, as well as the availability of cheap flights in the 2010s, it seems like *everyone* was traveling frequently, particularly going abroad to Europe. With headlines like [“Overtourism in Europe’s historic cities sparks backlash”](https://www.theguardian.com/world/2020/jan/25/overtourism-in-europe-historic-cities-sparks-backlash)(The Guardian) and [“Should You Visit These Beautiful European Destinations Suffering From Overtourism?](https://www.forbes.com/sites/ceciliarodriguez/2020/01/30/to-go-or-not-to-go-to-these-beautiful-european-places/#657e49fa29e4)(Forbes), it seems like Europe is crumbling under an unsustainable rise in tourism. 


## Motivation
|<img src="https://github.com/JCurley10/Where-Did-you-Come-From-Where-Did-you-Go-International-Tourism-Over-10-Years/blob/main/images/Paris.JPG" alt="louvre" width="250" height="250"> |
<img src="https://github.com/JCurley10/Where-Did-you-Come-From-Where-Did-you-Go-International-Tourism-Over-10-Years/blob/main/images/Prague.JPG" alt="prague" width="250" height="250"> |
<img src="https://github.com/JCurley10/Where-Did-you-Come-From-Where-Did-you-Go-International-Tourism-Over-10-Years/blob/main/images/slovenia.png" alt="Slovenia" width="250" height="250">  |
<p>(Personal Photos. Location from left to right: The Louvre, Paris; Charles Bridge, Prauge; Ljubliana, Slovenia)
<p>
I became curious about the rise in tourism and if the change is really *that* drastic reading story after story about over-tourism in Europe, and if my experiences of ever-growing tourism to Europe really matched the numbers. (I am so curious, that I had planned to take a group of students on an international educational program to Iceland to learn about the effects of over-tourism, but sadly wasn’t able to go due to the Coronavirus.) So, for selfish purposes, I want to knnow which countries in Europe saw the greatest percent change (both positive and negative) since 2008. (Maybe that’s where I want to travel next!)

But I am also curious about why there may be a change, because as a tourist, I’d want to consider the shape of the country I travel to. I assume that not all European countries are in the fiscal shape to attract more tourists, and not everyone has the means to travel. So, I decided to look into the GDP of a country, specifically the rate of change of GDP, and how that relates to the rate of change of incoming tourists to a country and to outgoing tourists from a country. While I will not be able to make any conclusions about the relationship between GDP and tourist rates-of-change, I am interested in their correlation as a start to a deeper investigation of tourism indicators. 

## The Questions

- Which countries saw the greatest rate of change (positive and negative, if any), and least change, for both incoming and outgoing international travelers between 2008 and 2018?
- How does the rate of change of GDP of a country correlate to both the incoming-tourists to that country, and outgoing-tourist rates from that country?

## Key Terms and Definitions

For this project, I focused on tourism to and from European countries between 2008 and 2009. 
* **European Countries** in this project are defined as the union of countries from the Schengen region and the EU, which are the following 29 countries (in no particular order): ```Austria, Belgium, Czech Republic, Denmark, Finland, France, Germany, Greece, Hungary, Iceland, Ireland, Italy, Luxembourg, Netherlands, Norway, Poland, Portugal, Slovak Republic, Spain, Sweden, Switzerland, Bulgaria, Croatia, Estonia, Latvia, Lithuania, Malta, Romania, and Slovenia.```

The following terms and definitions are taken from the Organisation for Economic Co-Operation and Development (OEC)<sup>1</sup>

- **Tourism** can be regarded as a social, cultural and economic phenomenon related to the movement of people outside their usual place of residence. Tourism refers to the activity of visitors. 
- **A visitor** is a traveller taking a trip to a main destination outside his/her usual environment, for less than a year, for any main purpose (business, leisure or other personal purpose) other than to be employed in the country or place visited. 
- **A tourist** is a visitor if his/her trip includes an overnight stay; otherwise, a visitor is classified as a same-day visitor (or excursionist). 
  - In the purpose of this analysis, 
- **Inbound tourism** comprises the activities of a non-resident visitor within the country of reference. 
  - For the purpose of this analysis, I used the descriptor for "Overnight visitors (tourists)" to define Inbound tourists. These terms may be used interchangeably throughout this file


## The Data
- I pulled data from three sources looking at outgoing and incoming tourists from/to countries, and the GDP of those countries.
- The data for incoming and outgoing tourists numbers I used come from the [Inbound Tourism and Outbound Tourism sets](https://www.kaggle.com/nubatama/tourism-inout-statdata-from-oecd) from Kaggle.com. The [original data](https://stats.oecd.org/Index.aspx?QueryId=95071) come from published queries from their respective datasets from the OECD, which is an international organization that collects and provides data publicly to support evidence-based policy across the globe.

**A brief look at the raw data from the Inbound Tourism Dataset**

|      | COUNTRY | Country |                     VARIABLE |                        Variable | SOURCE |                 Source | YEAR | Year |   Value | Flag Codes | Flags |
|------|--------:|--------:|-----------------------------:|--------------------------------:|-------:|-----------------------:|-----:|-----:|--------:|-----------:|------:|
| 1541 | ISL     | Iceland | INB_ACCOMM_OTHER_COLL_NIGHTS | Other collective establishments | SUPPLY | Tourism supply surveys | 2013 | 2013 | 812325  | NaN        | NaN   |
| 1542 | ISL     | Iceland | INB_ACCOMM_OTHER_COLL_NIGHTS | Other collective establishments | SUPPLY | Tourism supply surveys | 2014 | 2014 | 1106718 | NaN        | NaN   |
| 1543 | ISL     | Iceland | INB_ACCOMM_OTHER_COLL_NIGHTS | Other collective establishments | SUPPLY | Tourism supply surveys | 2015 | 2015 | 1259951 | NaN        | NaN   |

- original "inbound" dataset, showing the first three rows for the Czech Republic, one of the 28 countries I investigated.

**A note on the features** 
- The ```Variable``` column had 87 total indicators such as ```Total International Arrivals```, ```Nights in all types of accommodation```, ```Same-day visitors (excursionists)```, or a country name to indicate where the tourists came from. I only used the information from the ```Overnight visitors (tourists)``` rows as the definition aligned with my research. 
- the ```Value``` represents the total population of the "Variable" indicator. For the purposes of this study, they are the total incoming tourists to the country in the ```Country``` column.
- The ```source``` column represents from which survey the data was collected. Some countries had collected data in both ```Tourism supply surveys``` or ```Tourism demand surveys

- **Notes on the Source data in the "Incoming Tourists" Dataset**:
  - In my analysis, I chose the ```SOURCE``` column as it was less to type.
  - After digging into the type of information collected in the different surveys (Supply or Demand), there was a clear difference in the reported numbers of travelers depending on which survey was used. There is, however, consistency among countries within one type of survey reported. While some countries had reported information from both surveys, others did not. Therefore, I used my discretion and will used the information first from the Supply source. If the country did not report Supply data, I used the Demand source. 
  - For this reason, I will only compare countries against each other as long as they come from the same source:
    - Countries whose data come from the Tourism supply surveys, grouped under ```SUPPLY ```: Austria, Belgium, Czech Republic, Finland, Germany, Greece, Hungary, Italy, Luxembourg, Netherlands, Norway, Poland, Portugal, Slovak Republic, Spain, Switzerland, Bulgaria, Croatia, Estonia, Latvia, Lithuania, Romania, and Slovenia```
    - Countries whose data come from the Tourism demand surveys, grouped under  ```DEMAND```: ```Denmark, France, Iceland, Ireland, Malta, Sweden```
    
#### A look at a cleaned Inbound dataset for inbound tourists to a country, by inbound country and source
**Value** represents total incoming tourists
|      | Country | Variable                      | SOURCE | Year | Value   |
|------|---------|-------------------------------|--------|------|---------|
| 1571 | Iceland | Overnight visitors (tourists) | DEMAND | 2013 |  807349 |
| 1572 | Iceland | Overnight visitors (tourists) | DEMAND | 2014 |  997556 |
| 1573 | Iceland | Overnight visitors (tourists) | DEMAND | 2015 | 1289139 |


A look at a cleaned Outbound dataset for outbound tourists from a country, by origin country**

|     | Country | Variable                      | Year | Outgoing_Tourists |
|-----|---------|-------------------------------|------|-------------------|
| 140 | Iceland | Overnight visitors (tourists) | 2013 |         381675.00 |
| 141 | Iceland | Overnight visitors (tourists) | 2014 |         413291.00 |
| 142 | Iceland | Overnight visitors (tourists) | 2015 |         467437.00 |

**A brief look at the raw data from the GDP dataset**
- The data for the GDP come form the dataset [GDP in Current USD](https://data.worldbank.org/indicator/NY.GDP.MKTP.CD) from the World Bank
- The GDP is in current USD, for the sake of continuity. 

| Country Name | Country Code |   Indicator Name  | Indicator Code |     1960    |     1961    |     1962    |     1963    |     1964    |    1965    |    1966    |    1967    |    1968    |    1969    |    1970    |    1971    |    1972    |    1973    |    1974    |    1975    |    1976    |    1977    |    1978    |    1979    |    1980    |    1981    |    1982    |    1983    |    1984    |    1985    |     1986    |     1987    |     1988    |     1989    |     1990    |     1991    |     1992    |    1993    |    1994    |    1995    |    1996    |    1997    |    1998    |    1999    |    2000    |    2001    |     2002    |     2003    |     2004    |     2005    |     2006    |     2007    |     2008    |     2009    |     2010    |     2011    |     2012    |     2013    |     2014    |     2015    |     2016    |     2017    |     2018    |     2019    |
|:------------:|:------------:|:-----------------:|:--------------:|:-----------:|:-----------:|:-----------:|:-----------:|:-----------:|:----------:|:----------:|:----------:|:----------:|:----------:|:----------:|:----------:|:----------:|:----------:|:----------:|:----------:|:----------:|:----------:|:----------:|:----------:|:----------:|:----------:|:----------:|:----------:|:----------:|:----------:|:-----------:|:-----------:|:-----------:|:-----------:|:-----------:|:-----------:|:-----------:|:----------:|:----------:|:----------:|:----------:|:----------:|:----------:|:----------:|:----------:|:----------:|:-----------:|:-----------:|:-----------:|:-----------:|:-----------:|:-----------:|:-----------:|:-----------:|:-----------:|:-----------:|:-----------:|:-----------:|:-----------:|:-----------:|:-----------:|:-----------:|:-----------:|:-----------:|
| Aruba        | ABW          | GDP (current US$) | NY.GDP.MKTP.CD |             |             |             |             |             |            |            |            |            |            |            |            |            |            |            |            |            |            |            |            |            |            |            |            |            |            | 405463417.1 | 487602457.7 | 596423607.1 | 695304363   | 764887117.2 | 872138715.1 | 958463184.4 | 1082979721 | 1245688268 | 1320474860 | 1379960894 | 1531944134 | 1665100559 | 1722798883 | 1873452514 | 1920111732 | 1941340782  | 2021229050  | 2228491620  | 2330726257  | 2424581006  | 2615083799  | 2745251397  | 2498882682  | 2390502793  | 2549720670  | 2534636872  | 2701675978  | 2765363128  | 2919553073  | 2965921788  | 3056424581  |             |             |
| Afghanistan  | AFG          | GDP (current US$) | NY.GDP.MKTP.CD | 537777811.1 | 548888895.6 | 546666677.8 | 751111191.1 | 800000044.4 | 1006666638 | 1399999967 | 1673333418 | 1373333367 | 1408888922 | 1748886596 | 1831108971 | 1595555476 | 1733333264 | 2155555498 | 2366666616 | 2555555567 | 2953333418 | 3300000109 | 3697940410 | 3641723322 | 3478787909 |            |            |            |            |             |             |             |             |             |             |             |            |            |            |            |            |            |            |            |            | 4055179566  | 4515558808  | 5226778809  | 6209137625  | 6971285595  | 9747879532  | 10109225814 | 12439087077 | 15856574731 | 17804292964 | 20001598506 | 20561069558 | 20484885120 | 19907111419 | 19362642267 | 20191760000 | 19484384937 | 19101353833 |
| Angola       | AGO          | GDP (current US$) | NY.GDP.MKTP.CD |             |             |             |             |             |            |            |            |            |            |            |            |            |            |            |            |            |            |            |            | 5930503401 | 5550483036 | 5550483036 | 5784341596 | 6131475065 | 7553560459 | 7072063345  | 8083872012  | 8769250550  | 10201099040 | 11228764963 | 10603784541 | 8307810974  | 5768720422 | 4438321017 | 5538749260 | 7526446606 | 7648377413 | 6506229607 | 6152922943 | 9129594819 | 8936063723 | 15285594828 | 17812705294 | 23552052408 | 36970918699 | 52381006892 | 65266452081 | 88538611205 | 70307163678 | 83799496611 | 1.12E+11    | 1.28E+11    | 1.37E+11    | 1.46E+11    | 1.16E+11    | 1.01E+11    | 1.22E+11    | 1.01E+11    | 94635415870 |


## EDA 

#### A look at the tourism change overtime, to and from Iceland 



## Analysis 
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

## Conclusion and Further Analysis

There is clearly something different or misleading about where the inbound and outbound tourism data come from. 



----
<sup>1</sup> [stats.oecd.org](https://stats.oecd.org) <p>
<sup>2</sup> [Original datasets found here](https://stats.oecd.org/Index.aspx?QueryId=95071)

