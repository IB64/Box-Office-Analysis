# Box-Office-Analysis Project by Gian-Marco Caramelli & Angelo Beleno
## Objectives:
- Showcase the performance of the Domestic box office over the last 24 years
- Successfully create a web scraping script 
- Highlight the best performing seasons on average and the best performing release dates on average based on seasonality 
- Highlight the avg box office per month and day over the last 24 years to shed visibility on commercial trends.
- Provide commercial insights surrounding the domestic movie industry.

The project involved Domestic Box Office data extracted from Box Office Mojo from the 01/01/00 to 31/12/23.  The extraction resulted in over 355,000 rows of data and 6832 movies. Highlighting some key insights surrounding the domestic box office.

The project contains a pipeline that uses the box_office api Python library to web scrape data from Box Office Mojo. The extracted data is cleaned, formatted and uploaded to a csv file.

Our code:  src

Once our extraction was completed and the clean data was onto a CSV file we uploaded it onto BigQuery for Data Analysis.

Our Queries and results: src/sql

The data analysed in BigQuery was uploaded onto Tableau and we displayed the results in a dashboard:

Domestic Box Office Analysis V1: https://public.tableau.com/app/profile/gian.marco.caramelli/viz/DomesticBoxOfficeAnalysis2000-2023/Dashboard1 

Domestic Box Office Analysis V3: https://public.tableau.com/app/profile/gian.marco.caramelli/viz/DomesticBoxOfficeAnalysis2000-2023V3/Dashboard2 


Overall the project successfully completed all objectives and delivered insightful visualisation from our data extraction and analysis. 

Our full Documentation on the project: 
https://docs.google.com/document/d/1uUFjNye__e3ooKvdr2xNcIaMau0f9EFgnvk2WZr_3D0/edit 
## Key Commercial Insights
- Historically, Autumn has seen the lowest box office. This could be because it is cold and nobody wants to go outside. In contrast, summer has seen a more consistently high box office, where the weather is nice.
- The best performing dates for the highest average box office revenue fall on specific days in Winter (December 25), Summer (July 3), Fall (November 23), and Spring (March 27). These dates align with major holidays and school breaks.
- Summer is the best performing season for box office revenue, followed by Winter, Spring, and Fall. This could be due to summer blockbusters and holiday season releases drawing larger audiences.
- Walt Disney Studios Motion Pictures (26.34%):
Dominance likely due to major franchises like Marvel, Star Wars, and Pixar.
- Warner Bros. (23.67%):
Success with franchises such as Harry Potter, DC Universe, and various high-performing standalone movies.
- Universal Pictures (20.09%):
Strong performance with franchises like Fast & Furious, Jurassic World, and Despicable Me/Minions.
- Autumn ranks as the lowest performing season in terms of average daily box office revenue, with September being the least lucrative month, particularly on September 19th. Notably, the 31st of any month typically registers the lowest average daily box office figures. Conversely, the 25th and 26th of the month consistently emerge as the top-performing days.
