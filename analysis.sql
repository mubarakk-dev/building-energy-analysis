
-- Building Energy Consumption Analysis
-- Dataset: Simulated office building electricity usage
-- Database: SQLite

-- Query 1: Daily electricity consumption

SELECT
    date,
    SUM(energy_kwh) AS total_energy_kwh
FROM energy_readings
GROUP BY date
ORDER BY date;


-- Query 2: Average electricity consumption by hour

SELECT
    hour,
    AVG(energy_kwh) AS avg_energy_kwh
FROM energy_readings
GROUP BY hour
ORDER BY avg_energy_kwh DESC;


-- Query 3: Daily consumption and percentage change

WITH daily_energy AS (
    SELECT
        date,
        SUM(energy_kwh) AS total_energy_kwh
    FROM energy_readings
    GROUP BY date
),
daily_comparison AS (
    SELECT
        date,
        total_energy_kwh,
        LAG(total_energy_kwh) OVER (
            ORDER BY date
        ) AS previous_day_kwh
    FROM daily_energy
)

SELECT
    date,
    total_energy_kwh,
    previous_day_kwh,
    ROUND(
        (total_energy_kwh - previous_day_kwh)
        * 100.0 / NULLIF(previous_day_kwh, 0),
        2
    ) AS percentage_change
FROM daily_comparison
ORDER BY date;
