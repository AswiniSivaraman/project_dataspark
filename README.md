Project Name:
DataSpark – Illuminating Insights for Global Electronics
Introduction:

Global Electronics, a leading retailer of consumer electronics, is striving to leverage its vast data to enhance customer satisfaction, optimize operations, and drive overall business growth. This project, titled "DataSpark: Illuminating Insights for Global Electronics," aims to conduct a comprehensive Exploratory Data Analysis (EDA) on their data to uncover valuable insights and actionable recommendations.
Problem Statement:

As part of Global Electronics' data analytics team, you are tasked with conducting a comprehensive Exploratory Data Analysis (EDA) to uncover valuable insights from the company’s data. Your goal is to provide actionable recommendations that can enhance customer satisfaction, optimize operations, and drive overall business growth.
Global Electronics, a leading retailer of consumer electronics, has provided you with several datasets containing information about their customers, products, sales, stores, and currency exchange rates.
The company seeks to leverage this data to better understand their business and identify areas for improvement.
Packages Used:

•	Pandas:
Pandas is a powerful and open-source Python library. The Pandas library is used for data manipulation and analysis. Pandas consist of data structures and functions to perform efficient operations on data.
To know more about Pandas. Click here  https://pandas.pydata.org/docs/index.html

•	MySQL:
MySQL is an open-source relational database management system (RDBMS) that's used to store and manage data
To know more about MySQL. Click here  https://dev.mysql.com/doc/

Install Packages:

•	Pandas – pip install pandas
•	MySQL Connector– pip install mysql-connector-python
 
Software Used:

•	Visual Studio Code:
Visual Studio Code, also commonly referred to as VS Code, is a source-code editor developed by Microsoft for Windows, Linux, macOS and web browsers. Features include support for debugging, syntax highlighting, intelligent code completion, snippets, code refactoring, and embedded version control with Git. Users can change the theme, keyboard shortcuts, preferences, and install extensions that add functionality.
Performed EDA in visual studio code.


To know more about visual studio code. Click here  https://code.visualstudio.com/docs

•	MySQL Workbench:
MySQL Workbench is a visual tool that helps database architects, developers, and DBAs work with MySQL servers and databases. It's a cross-platform, open-source tool that combines SQL development, database design, and administration into a single environment. Stores the data and have written queries for insight

To know more about MySQL workbench. Click here 
https://dev.mysql.com/doc/workbench/en/


•	Power Bi:
Power BI, or Power Business Intelligence, is a Microsoft platform that helps users analyse, visualize, and share data for business intelligence (BI) purposes. It's a collection of software services, apps, and connectors that can turn data from different sources into interactive insights. Power BI can connect to data from Excel spreadsheets, cloud-based data warehouses, and on-premises hybrid data warehouses. It can then help users build charts, graphs, and dashboards to visualize the data.
Created dashboard in Power Bi


To know more about Power Bi. Click here  https://learn.microsoft.com/en-us/power-bi/


•	PowerPoint:
It is a presentation-based program that uses graphics, videos, etc. to make a presentation more interactive and interesting
Created report for the project
To know more about PowerPoint. Click here  https://support.microsoft.com/en- us/powerpoint
 
Project files:

•	datacleaning.py:
1)	This file will manage the data cleaning process and saving the data in the mysql database.
•	project_dataspark_dataspark.sql:
1) This file contains MySQL queries to extract key insights from the data. These queries will address important business questions.
•	dataspark_dashboard.pbix:
1) This file contains interactive power bi dashboard which helps to understand business insights related to sales, customer, store, product, exchange rates.
•	Report.pptx:
1) This file contains the key insights of the global electronics with problem and solution statement
Project Workflow:

1)	Run the dalacleaning.py file in vs code using ‘python datacleaning.py’ command
2)	Execute MySQL queries in MySQL Workbench
3)	Open dataspark_dashboard.pbix to go through the customer, sales, stores, product, exchange rate insight of the global electronics.
4)	Open the Report.pptx file to understand the key insights and problem and solution statement of the insights.

Learnt things from this project:
•	Gained a deep understanding of how to clean and prepare data for analysis, ensuring accuracy and reliability
•	Improved proficiency in Exploratory Data Analysis (EDA), uncovering insights and patterns in data
•	Strengthened expertise in MySQL, particularly in data storage, retrieval, and management.
•	Developed advanced skills in Power BI, enabling the creation of impactful visualizations and dashboards.
•	Improved the ability to craft compelling narratives around data, effectively communicating insights and recommendations.

Power Bi Dashboard:
 
         

 
CUSTOMER INSIGHTS
 
Overivew
 
Insights
 
Q&A's
 

 

Interested Category Of Product By Age Group
Product category
Audio

4K	Cameras and camcorders
Cell phones Computers
Games and Toys
2K
Home Appliances
Music, Movies and Audio Books TV and Video
0K
 

Interested Subcategory of Product By Age Group

Age Group	18-24	25-34	35-44	45-54	55-64	65-84	85+


Air Conditioners Bluetooth Headphones
Boxed Games Camcorders
Cameras & Camcorders Access…
Car Video
 
18-24	25-34	35-44	45-54	55-64	65-84	85+
Age Group
 
0K	5K	10K
Interested People Count
 


 
Product Sold Count By Category

Audio	Cameras and …	Cell phones	Computers	Games and …
 
Category Interested Breakdown By Gender
 
Profit By State
 

 
Music, Movies and …
 
Audio 23K
 
29K	Cameras and …
18K

 
Home App…  	
18K
 



Cell phones 31K
 

 
Games and Toys
23K
 


Computers 44K
 



© 2024 Miiccrrossofftt Corrporrattiion
 

         

SALES INSIGHTS


 


country	Canada	Online	United States
 


country	Australia	France	Germany	Italy
 
Total Profit Across All Stores In A Country

Legend	Count of store_key	Sum of total_sales_usd
 

Connecticut

Kansas Nebraska Nevada
Newfoundland and…
 

1.08M

1.06	M

1.07	M

1.06M

1.26M
 


0.2M


0.1M


0.0M
 



0.13	M
 



0.14	M
0.11	M
 





0.08M
 


0.15M 0.13M
 




0.12	M
 



0.15M



0.01M
 
0.21M	20
10
0
 

20M


10M


0M
 

 
0M	5M	10M
Sum of total_sales_usd
 

state
 

country
 


Overall Profit By Category	Stores across the Country

category	Audio	Cameras a…	Cell phones	Computers	Games and…	Home Appli…	Music, Movi…	store_key	0	1	2	4	5	6	8	9	10	12	13	14	15	16	17	18	19	20	21	22	23	24	26	27      28      29      30      31      32

 

Music, Movies and Audio Books
 
Audio 3.17M
 


Home Appliances
5.89M

Games and Toys
0.72M
 
3.13M	Cameras and camcorders
5.29M




Cell phones 6.18M
 



 
Computers 16.08M
 

© 2024 Miiccrrossofftt Corrporrattiion
 

 
         

 
STORE INSIGHTS
 

Overview
 

Insights
 

Q&A's
 


Store's Sales Details

country	Sum of customer_count		Sum of sales_per_store	Sum of store_count		Sum of total_sales_volume
Australia	2941	1,534.83	6	9209
Canada	5415	3,358.60	5	16793
France	1730	769.29	7	5385
Germany	5956	2,104.78	9	18943
Italy	2685	2,823.33	3	8470
Netherlands	2250	1,450.40	5	7252
United Kingdom	8140	3,614.00	7	25298
United States	33767	4,433.63	24	106407


 
Least 10 Stores by Sales
 


store_key
 
Top 10 Stores by Sales
65	store_key
 
Sales By Store Age in a State

Alaska	Arkansas	Armagh	Australian Ca…	Ayrshire	Basse-Norm…	Belfast
 
28 156.52K

18 171.98K




17
137.52K


16 149.79K
 
1 174.14K	1
2 9.38K	2
12	12
152.76K	13
14
13	15
122.83K
16
14 91.65K	17

15 168.47K
 
61 1M 1.02M
59 0.98M

57 0.97M

55 1.06M

54 1.07M

50 1.06M
45 1.08M
9 1.06M
 
0

9

45

50
0 8.94M	54
55

57

59
 

20






10



0M	5M	10M	15M	20M
Sum of total_sales
 
         

 
PRODUCT INSIGHTS
 
Overview
 
Insights
 
Q&A's
 


Total Sales By Category And Year	Popular Product In A Country

year	2016	2017	2018	2019	2020	2021	product_name	Adventure Wor…	Adventure W…	Adventure W…	Adventure …	Contoso DVD …	SV DVD 14-I…	SV DVD Rec…	WWI Deskto…	WWI Deskto…


5M





0M



 
Category
 
© 2024 Miiccrrossofftt Corrporrattiion
 


 
Category Sold In Years
 
Profit By Brand
 
Top 10 Products By Sales Volume
 

 
year	2016	2017	2018	2019	2020	2021
 
Brand Name	A. Datum	Adventure Works	Contoso	Fabrikam	Litware
 

Adventure Works …
 

521
 

5M





0M




Category
 
Wide World Im… 32.13K The Phone Company
24.71K
Southridge Video
17.48K
Proseware  	
36.66K
Northwind Traders
10.15K

Litware 47.2K
 
A. Datum 20.75K
Adventure Works 42.75K



Contoso 87.24K




Fabrikam 63.12K
 

Adventure Works … Adventure Works … Adventure Works … Adventure Works … WWI Desktop PC1… WWI Desktop PC1…
 











0	200	400
Sales Volume
 
505
520
514
521
509
507
 
         

 
EXCHANGE RATES INSIGHTS
 

Insights
 

Q&A's
 

 

Profitable Currency Type
 

Distribution of Sales By Currency Code
 

Exchange Rate Fluctuate on Different Year
 

 


AUD CAD
 


0.6M

1.0M
 



20M
 
23M


8
 
2016	2017	2018	2019	2020	2021
 
EUR
GBP USD
 


0.9M
 
1.5M
 





4.6M
 
10M	9M	7
6M
4M
2M
 


0M	2M	4M
Profit
 

0M
AUD	CAD	EUR	GBP	USD
Currency Code
 


Month
 


country	product_name	unit_cost_usd	unit_price_usd	exchange_rate	local_cost	local_price	profit_margin
Australia	A. Datum Advanced Digital Camera M300 Azure	$86.68	$188.50	1.3898	120.46785988330842	261.9772910475731	141.50943116426467
Australia	A. Datum All in One Digital Camera M200 Azure	$86.45	$188.00	1.2787	110.5436144888401	240.39559888839722	129.85198439955713
Australia	A. Datum All in One Digital Camera M200 Grey	$86.45	$188.00	1.3728	118.67855935692788	258.086398601532	139.4078392446041
Australia	A. Datum All in One Digital Camera M200 Silver	$86.45	$188.00	1.4188	122.65525968670845	266.73439931869507	144.0791396319866
Australia	A. Datum Bridge Digital Camera M300 Green	$85.95	$186.90	1.4226	122.27247265577317	265.88394577503203	143.61147311925885
Australia	A. Datum Bridge Digital Camera M300 Grey	$85.95	$186.90	1.2846	110.41137167215348	240.0917436361313	129.68037196397782
Australia	A. Datum Bridge Digital Camera M300 Grey	$85.95	$186.90	1.2974	111.51152980327606	242.48405957221985	130.9725297689438
Australia	A. Datum Bridge Digital Camera M300 Pink	$85.95	$186.90	1.4498	124.61031124591828	270.9676227092743	146.35731146335598
Australia	A. Datum Compact Digital Camera M200 Green	$59.32	$129.00	1.2769	75.745711145401	164.72010684013367	88.97439569473266
Australia	A. Datum Compact Digital Camera M200 Silver	$59.32	$129.00	1.3879	82.33022769451141	179.03909933567047	96.70887164115906
Australia	A Datum Compact Digital Camera M200 Silver	$59 32	$129 00	1 4777	87 65716370582581	190 62329936027527	102 96613565444946


