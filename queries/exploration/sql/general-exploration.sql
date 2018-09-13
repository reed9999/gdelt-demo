-- For most of my hunting around, it's fine to consolidate it in this one file
-- As I accumulate useful snippets here I can move them around to better-
-- organized locations.

-- Assumes lookup tables loaded.
SELECT day, actor1code, actor1name, actor2code, actor2name, c1.country, c2.country,
-- but I'm really not clear on the difference between these two
actor1countrycode, actor1geo_countrycode,
actor2countrycode, actor2geo_countrycode,
FROM events AS e 
    LEFT JOIN countries AS c1 ON e.actor1countrycode = c1.code
    LEFT JOIN countries AS c2 ON e.actor2countrycode = c2.code
-- WHERE actor1countrycode != '' 
LIMIT 100;
