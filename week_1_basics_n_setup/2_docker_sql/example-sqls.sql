
--Q3
SELECT 
	COUNT(1) as "trip_count"
FROM 
	public.green_taxi_trips t
WHERE CAST(lpep_pickup_datetime AS DATE)='2019-01-15' AND
	CAST(lpep_dropoff_datetime AS DATE)='2019-01-15';
---
SELECT lpep_pickup_datetime, lpep_dropoff_datetime, total_amount, 
		CONCAT(lpu."Borough", ' / ' , lpu."Zone") AS "pickup_loc",
		CONCAT(ldo."Borough", ' / ' , ldo."Zone") AS "dropoff_loc"

FROM public.green_taxi_trips t,
		public.zones lpu,
		public.zones ldo
where 
	t."PULocationID" = lpu."LocationID" AND
	t."DOLocationID" = ldo."LocationID"
	LIMIT 100;

SELECT lpep_pickup_datetime, lpep_dropoff_datetime, total_amount, 
		CONCAT(lpu."Borough", ' / ' , lpu."Zone") AS "pickup_loc",
		CONCAT(ldo."Borough", ' / ' , ldo."Zone") AS "dropoff_loc"
FROM 
	public.green_taxi_trips t JOIN zones lpu 
		ON t."PULocationID" = lpu."LocationID"
	JOIN zones ldo
		ON t."DOLocationID" = ldo."LocationID"
	LIMIT 100;
--LEFT JOIN means Show all rows on the left even there's no record on the right on the joining condition
-- If there was no matching record on the zones, with LEFT JOIN we can still see all rows of the trips table.
-- Only JOIN wouldn't return non matching records.	

--Q4:
SELECT 
	CAST(lpep_pickup_datetime AS DATE) as "day", 
-- 	COUNT(1) as "trip_count",
	MAX(trip_distance)
-- 	MAX(passenger_count)
FROM 
	public.green_taxi_trips t
GROUP BY
	1
ORDER BY 2 DESC;

--Q5:
SELECT 
	CAST(lpep_pickup_datetime AS DATE) as "day", 
	COUNT(1) as "trip_count"
FROM 
	public.green_taxi_trips t
WHERE 
	CAST(lpep_pickup_datetime AS DATE) = '2019-01-01' AND
	passenger_count='3' -- OR '2'
GROUP BY 1;

--Q6:
SELECT  lpu."Zone" AS "pickup_loc",
		ldo."Zone" AS "dropoff_loc",
		MAX(tip_amount)
FROM 
	public.green_taxi_trips t 
	JOIN zones lpu 
		ON t."PULocationID" = lpu."LocationID"
	JOIN zones ldo
		ON t."DOLocationID" = ldo."LocationID"
WHERE lpu."Zone" = 'Astoria'
GROUP BY 1, 2
ORDER BY 3 DESC;