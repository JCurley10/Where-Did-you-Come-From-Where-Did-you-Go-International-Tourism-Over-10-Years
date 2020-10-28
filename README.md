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

```
['Austria', 'Belgium', 'Czech Republic', 
'Denmark', 'Finland', 'France', 'Germany', 
'Greece', 'Hungary', 'Iceland', 'Ireland', 
'Italy', 'Luxembourg', 'Netherlands', 'Norway', 
'Poland', 'Portugal', 'Slovak Republic', 'Spain', 
'Sweden', 'Switzerland', 'Bulgaria', 'Croatia', 
'Estonia', 'Latvia', 'Lithuania', 'Malta', 
'Romania', 'Slovenia']
These countries are, from the Inbound Dataset:  not every country is affected by tourism the same way, and truly not everyone is able to travel as much as it may seem.  
```

## Motivation

I became curious about the rise in tourism and if the change is really *that* drastic reading story after story about over-tourism in Europe, and if my experiences of ever-growing tourism to Europe really matched the numbers. (I am so curious, that I had planned to take a group of students on an international educational program to Iceland to learn about the effects of over-tourism, but sadly wasn’t able to go due to the Coronavirus.) So, for selfish purposes, I want to knnow which countries in Europe saw the greatest percent change (both positive and negative) since 2008. (Maybe that’s where I want to travel next!)

But I am also curious about why there may be a change, because as a tourist, I’d want to consider the shape of the country I travel to. I assume that not all European countries are in the fiscal shape to attract more tourists, and not everyone has the means to travel. So, I decided to look into the GDP of a country, specifically the rate of change of GDP, and how that relates to the rate of change of incoming tourists to a country and to outgoing tourists from a country. While I will not be able to make any conclusions about the relationship between GDP and tourist rates-of-change, I am interested in their correlation as a start to a deeper investigation of tourism indicators. 

## The Questions

• Which countries saw the greatest rate of change (positive and negative, if any), and least change, for both incoming and outgoing international travelers between 2008 and 2018?
• How does the rate of change of GDP of a country correlate to both the incoming-tourists to that country, and outgoing-tourist rates from that country?

## Key Terms and Definitions

For this project, I focused on tourism to and from European countries between 2008 and 2009. 
* **European Countries** in this project are defined as the union of countries from the Schengen region and the EU, which are the following 29 countries (in no particular order): ```Austria, Belgium, Czech Republic, Denmark, Finland, France, Germany, Greece, Hungary, Iceland, Ireland, Italy, Luxembourg, Netherlands, Norway, Poland, Portugal, Slovak Republic, Spain, Sweden, Switzerland, Bulgaria, Croatia, Estonia, Latvia, Lithuania, Malta, Romania, and Slovenia.```

#### Key Terms
The following terms and definitions are taken from the Organisation for Economic Co-Operation and Development (OEC)[^1] 

- **Tourism** can be regarded as a social, cultural and economic phenomenon related to the movement of people outside their usual place of residence. Tourism refers to the activity of visitors. 
- **A visitor** is a traveller taking a trip to a main destination outside his/her usual environment, for less than a year, for any main purpose (business, leisure or other personal purpose) other than to be employed in the country or place visited. 
- **A tourist** is a visitor if his/her trip includes an overnight stay; otherwise, a visitor is classified as a same-day visitor (or excursionist). 
- **Inbound tourism** comprises the activities of a non-resident visitor within the country of reference. 
  - In the datasets, I used the descriptor for "Overnight visitors (tourists)" to define Inbound tourists. These terms may be used interchangeably throughout this file


## The Data
The Datasets used for this project were taken from the 
## EDA 

## Analysis 

## Conclusion and Further Analysis




**Notes to self**: 

Notebooks folder for jupyter notebook 

src folder - put python scripts (code in jupyter and copy into script, or write in python and import into a script)

----
[^1]: [stats.oecd.org](https://stats.oecd.org)
[^2]: [Original datasets found here](https://stats.oecd.org/Index.aspx?QueryId=95071)

