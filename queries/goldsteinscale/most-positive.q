-- The point of this directory is for exploratory queries to get to learn the
-- goldsteinscale column. Since this column is the positive/negative metric for
-- events influencing stability of societies, it could be a key one for my research
-- here.

-- Unsurprisingly the kind of event matters a lot.
-- 190: Use of conventional military force, very destabilizing
-- 0847: Retreat or surrender militarily, very stabilizing

-- This seems to be perfectly correlated--i.e. the Goldstein number is derived
-- directly from the kind of event.
SELECT
  goldsteinscale, eventcode, eventrootcode, count(*)
FROM gdelt.events
GROUP BY goldsteinscale, eventcode, eventrootcode
  ORDER BY goldsteinscale;
