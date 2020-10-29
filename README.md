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

| COUNTRY | Country | VARIABLE | Variable | SOURCE | Source | YEAR | Year | Value |
|---------|---------|----------|----------|--------|--------|------|------|-------|
| CZE | Czech Republic | INB_ARRIVALS_OVERNIGHT | Overnight visitors (tourists) | SUPPLY | Tourism supply surveys | 2008 | 2008 | 6649410 |  |  |
| CZE | Czech Republic | INB_ARRIVALS_OVERNIGHT | Overnight visitors (tourists) | SUPPLY | Tourism supply surveys | 2009 | 2009 | 6032370 |  |  |
| CZE | Czech Republic | INB_ARRIVALS_OVERNIGHT | Overnight visitors (tourists) | SUPPLY | Tourism supply surveys | 2010 | 2010 | 6333996 |  |  |

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
    
**A look at a cleaned Inbound dataset for inbound tourists to a country, by inbound country and source**
Value represents total incoming tourists
|     | Country        | Variable                      | SOURCE | Year | Value   |
|-----|----------------|-------------------------------|--------|------|---------|
| 440 | Czech Republic | Overnight visitors (tourists) | SUPPLY | 2008 | 6649410 |
| 441 | Czech Republic | Overnight visitors (tourists) | SUPPLY | 2009 | 6032370 |
| 442 | Czech Republic | Overnight visitors (tourists) | SUPPLY | 2010 | 6333996 |


**A look at a cleaned Outbound dataset for outbound tourists from a country, by origin country**

|    | Country        | Variable                      | Year | Outgoing_Tourists |
|----|----------------|-------------------------------|------|-------------------|
| 74 | Czech Republic | Overnight visitors (tourists) | 2008 | 9665239           |
| 75 | Czech Republic | Overnight visitors (tourists) | 2009 | 8904347           |
| 76 | Czech Republic | Overnight visitors (tourists) | 2010 | 8672554           |

**A brief look at the raw data from the GDP dataset**
- The data for the GDP come form the dataset [GDP in Current USD](https://data.worldbank.org/indicator/NY.GDP.MKTP.CD) from the World Bank
- The GDP is in current USD, for the sake of continuity. 

| Country Name | Country Code | Indicator Name    | Indicator Code | 1960        | 1961        | 1962        | 1963        | 1964        | 1965       | 1966       | 1967       | 1968       | 1969       | 1970       | 1971       | 1972       | 1973       | 1974       | 1975       | 1976       | 1977       | 1978       | 1979       | 1980       | 1981       | 1982       | 1983       | 1984       | 1985       | 1986        | 1987        | 1988        | 1989        | 1990        | 1991        | 1992        | 1993       | 1994       | 1995       | 1996       | 1997       | 1998       | 1999       | 2000       | 2001       | 2002        | 2003        | 2004        | 2005        | 2006        | 2007        | 2008        | 2009        | 2010        | 2011        | 2012        | 2013        | 2014        | 2015        | 2016        | 2017        | 2018        | 2019        |
|--------------|--------------|-------------------|----------------|-------------|-------------|-------------|-------------|-------------|------------|------------|------------|------------|------------|------------|------------|------------|------------|------------|------------|------------|------------|------------|------------|------------|------------|------------|------------|------------|------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|------------|------------|------------|------------|------------|------------|------------|------------|------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|
| Aruba        | ABW          | GDP (current US$) | NY.GDP.MKTP.CD |             |             |             |             |             |            |            |            |            |            |            |            |            |            |            |            |            |            |            |            |            |            |            |            |            |            | 405463417.1 | 487602457.7 | 596423607.1 | 695304363   | 764887117.2 | 872138715.1 | 958463184.4 | 1082979721 | 1245688268 | 1320474860 | 1379960894 | 1531944134 | 1665100559 | 1722798883 | 1873452514 | 1920111732 | 1941340782  | 2021229050  | 2228491620  | 2330726257  | 2424581006  | 2615083799  | 2745251397  | 2498882682  | 2390502793  | 2549720670  | 2534636872  | 2701675978  | 2765363128  | 2919553073  | 2965921788  | 3056424581  |             |             |
| Afghanistan  | AFG          | GDP (current US$) | NY.GDP.MKTP.CD | 537777811.1 | 548888895.6 | 546666677.8 | 751111191.1 | 800000044.4 | 1006666638 | 1399999967 | 1673333418 | 1373333367 | 1408888922 | 1748886596 | 1831108971 | 1595555476 | 1733333264 | 2155555498 | 2366666616 | 2555555567 | 2953333418 | 3300000109 | 3697940410 | 3641723322 | 3478787909 |            |            |            |            |             |             |             |             |             |             |             |            |            |            |            |            |            |            |            |            | 4055179566  | 4515558808  | 5226778809  | 6209137625  | 6971285595  | 9747879532  | 10109225814 | 12439087077 | 15856574731 | 17804292964 | 20001598506 | 20561069558 | 20484885120 | 19907111419 | 19362642267 | 20191760000 | 19484384937 | 19101353833 |
| Angola       | AGO          | GDP (current US$) | NY.GDP.MKTP.CD |             |             |             |             |             |            |            |            |            |            |            |            |            |            |            |            |            |            |            |            | 5930503401 | 5550483036 | 5550483036 | 5784341596 | 6131475065 | 7553560459 | 7072063345  | 8083872012  | 8769250550  | 10201099040 | 11228764963 | 10603784541 | 8307810974  | 5768720422 | 4438321017 | 5538749260 | 7526446606 | 7648377413 | 6506229607 | 6152922943 | 9129594819 | 8936063723 | 15285594828 | 17812705294 | 23552052408 | 36970918699 | 52381006892 | 65266452081 | 88538611205 | 70307163678 | 83799496611 | 1.12E+11    | 1.28E+11    | 1.37E+11    | 1.46E+11    | 1.16E+11    | 1.01E+11    | 1.22E+11    | 1.01E+11    | 94635415870 |

**A look at a cleaned GDP dataset, only looking at the Schengen Zone and EU countries**

|    | Country Name | 2008            | 2009            | 2010            | 2011            | 2012            | 2013            | 2014            | 2015            | 2016            | 2017            | 2018            |
|----|-------------|-----------------|-----------------|-----------------|-----------------|-----------------|-----------------|-----------------|-----------------|-----------------|-----------------|-----------------|
| 12 | Austria     | 430000000000.00 | 400000000000.00 | 392000000000.00 | 431000000000.00 | 409000000000.00 | 430000000000.00 | 442000000000.00 | 382000000000.00 | 395000000000.00 | 418000000000.00 | 456000000000.00 |
| 15 | Belgium     | 515000000000.00 | 481000000000.00 | 481000000000.00 | 523000000000.00 | 496000000000.00 | 522000000000.00 | 535000000000.00 | 462000000000.00 | 476000000000.00 | 504000000000.00 | 543000000000.00 |
| 19 | Bulgaria    | 54438966420.00  | 51999181062.00  | 50363282117.00  | 57363610380.00  | 54013812089.00  | 55591336862.00  | 56883172568.00  | 50630703922.00  | 53785050339.00  | 58950125036.00  | 66200847918.00  |

## EDA 
#### A look at the outgoing tourism from the Czech Republic over time
![Outgoing from Czech-Rep](https://github.com/JCurley10/Where-Did-you-Come-From-Where-Did-you-Go-International-Tourism-Over-10-Years/blob/main/images/outgoing_czech.png)

#### A look at the five countries who reported the top 5 most incoming tourists over time. 

#### A look at the 5 countries who reported the top 5 more outgoing tourists over time. It happens that each of these was reported in 2018

## Analysis 




## Conclusion and Further Analysis

There is clearly something different or misleading about where the inbound and outbound tourism data come from. 


**Notes to self**: 

----
<sup>1</sup> [stats.oecd.org](https://stats.oecd.org) <p>
<sup>2</sup> [Original datasets found here](https://stats.oecd.org/Index.aspx?QueryId=95071)

