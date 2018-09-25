-- Copying the goldsteinscale "most positive" stuff doesn't make sense because
--  we can't group by avgtone.
-- Also we should examine negative events.

SELECT *
FROM gdelt.events
ORDER BY avgtone DESC
LIMIT 50;

--I don't understand why two stories with actor "GUNMAN" are so high in the 
-- positive events. 043 is "Host a visit". 

-- What about negative tone of events?
SELECT *
FROM gdelt.events
ORDER BY avgtone ASC
LIMIT 50;

-- The "top four" (really all zero) are two military actions, an unspecified
-- announcement, and an unspecified rejection.
