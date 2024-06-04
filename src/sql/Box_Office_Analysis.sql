#total Domestic BO per Year
SELECT
EXTRACT(ISOYEAR FROM date) AS isoyear,
Sum(daily) as total_Box_Office
FROM `chrome-folio-405910.Box_Office_Analysis_Project.Clean_Data_Box_Office`
group by isoyear
order by isoyear


#top 10 studios in the last 24 years domestically
SELECT
distinct(Distributor),
sum(Daily) as total_box_office
from `chrome-folio-405910.Box_Office_Analysis_Project.Clean_Data_Box_Office`
where distributor != 'NA'
group by Distributor
order by total_box_office desc
limit 10


# Total BO for seasons over the last 24 years
SELECT
  sum(daily) AS total,
  EXTRACT(ISOYEAR FROM date) AS isoyear,
  CASE
    WHEN EXTRACT(MONTH FROM date) IN (12, 1, 2) THEN 'Winter'
    WHEN EXTRACT(MONTH FROM date) IN (3, 4, 5) THEN 'Spring'
    WHEN EXTRACT(MONTH FROM date) IN (6, 7, 8) THEN 'Summer'
    WHEN EXTRACT(MONTH FROM date) IN (9, 10, 11) THEN 'Fall'
    ELSE 'Unknown'
  END AS Seasons
FROM `chrome-folio-405910.Box_Office_Analysis_Project.Clean_Data_Box_Office`
GROUP BY Seasons, isoyear
order by 2 desc


# avg BO for seasons over the last 24 years
select
seasons,
round(avg(total),0) as Avg_BO
From(
SELECT
  sum(daily) AS total,
  EXTRACT(ISOYEAR FROM date) AS isoyear,
  CASE
    WHEN EXTRACT(MONTH FROM date) IN (12, 1, 2) THEN 'Winter'
    WHEN EXTRACT(MONTH FROM date) IN (3, 4, 5) THEN 'Spring'
    WHEN EXTRACT(MONTH FROM date) IN (6, 7, 8) THEN 'Summer'
    WHEN EXTRACT(MONTH FROM date) IN (9, 10, 11) THEN 'Fall'
    ELSE 'Unknown'
  END AS Seasons
FROM `chrome-folio-405910.Box_Office_Analysis_Project.Clean_Data_Box_Office`
GROUP BY Seasons, isoyear
order by 2 desc)
group by seasons


#top 10 best performing dates on avg in the last 24 years
select
Seasons,
avg(total) as avg_bo,
date
From(
SELECT
  sum(daily) AS total,
  EXTRACT(ISOYEAR FROM date) AS isoyear,
  date,
  CASE
    WHEN EXTRACT(MONTH FROM date) IN (12, 1, 2) THEN 'Winter'
    WHEN EXTRACT(MONTH FROM date) IN (3, 4, 5) THEN 'Spring'
    WHEN EXTRACT(MONTH FROM date) IN (6, 7, 8) THEN 'Summer'
    WHEN EXTRACT(MONTH FROM date) IN (9, 10, 11) THEN 'Fall'
    ELSE 'Unknown'
  END AS Seasons
FROM `chrome-folio-405910.Box_Office_Analysis_Project.Clean_Data_Box_Office`
GROUP BY Seasons, isoyear, date
order by 3,2 desc)
group by 1, 3
order by 2 desc
limit 15


#best performing day and month based on sesonality


WITH DailyTotals AS (
  SELECT
    SUM(daily) AS total,
    date,
    EXTRACT(DAY FROM date) AS day,
    EXTRACT(MONTH FROM date) AS month,
    CASE
      WHEN EXTRACT(MONTH FROM date) IN (12, 1, 2) THEN 'Winter'
      WHEN EXTRACT(MONTH FROM date) IN (3, 4, 5) THEN 'Spring'
      WHEN EXTRACT(MONTH FROM date) IN (6, 7, 8) THEN 'Summer'
      WHEN EXTRACT(MONTH FROM date) IN (9, 10, 11) THEN 'Fall'
      ELSE 'Unknown'
    END AS season
  FROM `chrome-folio-405910.Box_Office_Analysis_Project.Clean_Data_Box_Office`
  GROUP BY date, day, month, season
),
AveragePerDay AS (
  SELECT
    day,
    month,
    season,
    AVG(total) AS avg_bo
  FROM DailyTotals
  GROUP BY day, month, season
),
BestDay AS (
  SELECT
    day,
    month,
    season,
    avg_bo,
    ROW_NUMBER() OVER (PARTITION BY season ORDER BY avg_bo DESC) AS row_num
  FROM AveragePerDay
)
SELECT
  day,
  month,
  season,
  round(avg_bo,1)
FROM BestDay
WHERE row_num = 1
ORDER BY season;


#avg daily bo for the last 24 years
EXTRACT(MONTH FROM date) as month,
EXTRACT(DAY FROM date) as day,
round(avg(daily),1) as avg_daily_BO
from `chrome-folio-405910.Box_Office_Analysis_Project.Clean_Data_Box_Office`
group by 1,2
order by 1, 2


#film drops in BO bsed on week
SELECT
  Release,
  SUM(daily) AS total_daily_box_office,
  round(SUM(____LW),1) AS total_weekly_change,
  EXTRACT(WEEK FROM date) AS week_number,
  EXTRACT(YEAR FROM date) AS year
FROM
  `chrome-folio-405910.Box_Office_Analysis_Project.Clean_Data_Box_Office`
  where release = 'Five Nights at Freddy\'s'
GROUP BY
  Release,
  year,
  week_number
ORDER BY
  year,
  week_number;


