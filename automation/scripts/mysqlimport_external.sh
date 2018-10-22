# To get this to work, I had to whitelist the relevant directories in AppArmor
# https://stackoverflow.com/q/2783313/

echo "Remember to run from project root."
DATA_DIR=~/demo/data-related/external
# I hate using VARCHAR(16) but easiest way to deal with empty string for 
# the moment.
mysql -uroot -p -e "USE gdelt; 
DROP TABLE IF EXISTS gdp; 
CREATE TABLE IF NOT EXISTS gdp (
    country_name VARCHAR(999), country_code VARCHAR(3),
    indicator_name VARCHAR(64), indicator_code VARCHAR(16),
    gdp1960 VARCHAR(16), gdp1961 VARCHAR(16), gdp1962 VARCHAR(16), 
    gdp1963 VARCHAR(16), gdp1964 VARCHAR(16), 
    gdp1965 VARCHAR(16), gdp1966 VARCHAR(16), gdp1967 VARCHAR(16), 
    gdp1968 VARCHAR(16), gdp1969 VARCHAR(16), 
    gdp1970 VARCHAR(16), gdp1971 VARCHAR(16), gdp1972 VARCHAR(16), 
    gdp1973 VARCHAR(16), gdp1974 VARCHAR(16), 
    gdp1975 VARCHAR(16), gdp1976 VARCHAR(16), gdp1977 VARCHAR(16), 
    gdp1978 VARCHAR(16), gdp1979 VARCHAR(16), 
    gdp1980 VARCHAR(16), gdp1981 VARCHAR(16), gdp1982 VARCHAR(16), 
    gdp1983 VARCHAR(16), gdp1984 VARCHAR(16), 
    gdp1985 VARCHAR(16), gdp1986 VARCHAR(16), gdp1987 VARCHAR(16), 
    gdp1988 VARCHAR(16), gdp1989 VARCHAR(16), 
    gdp1990 VARCHAR(16), gdp1991 VARCHAR(16), gdp1992 VARCHAR(16), 
    gdp1993 VARCHAR(16), gdp1994 VARCHAR(16), 
    gdp1995 VARCHAR(16), gdp1996 VARCHAR(16), gdp1997 VARCHAR(16), 
    gdp1998 VARCHAR(16), gdp1999 VARCHAR(16), 
    gdp2000 VARCHAR(16), gdp2001 VARCHAR(16), gdp2002 VARCHAR(16), 
    gdp2003 VARCHAR(16), gdp2004 VARCHAR(16), 
    gdp2005 VARCHAR(16), gdp2006 VARCHAR(16), gdp2007 VARCHAR(16), 
    gdp2008 VARCHAR(16), gdp2009 VARCHAR(16), 
    gdp2010 VARCHAR(16), gdp2011 VARCHAR(16), gdp2012 VARCHAR(16), 
    gdp2013 VARCHAR(16), gdp2014 VARCHAR(16), 
    gdp2015 VARCHAR(16), gdp2016 VARCHAR(16), gdp2017 VARCHAR(16),
    dummy VARCHAR(16)
)"
# TEMPFILENAME=gdp.__temp.csv
CURRENT_FILE=$DATA_DIR/API_NY.GDP.PCAP.CD_DS2_en_csv_v2_10181232.csv
mysql -uroot -p gdelt -e "LOAD DATA INFILE '$CURRENT_FILE' INTO TABLE gdp 
FIELDS TERMINATED BY ','
    ENCLOSED BY '\"' 
IGNORE 5 LINES;" 

# Do nothing with these two for the moment because we may not need this metadata...
CURRENT_FILE=$DATA_DIR/Metadata_Country_API_NY.GDP.PCAP.CD_DS2_en_csv_v2_10181232.csv
CURRENT_FILE=$DATA_DIR/Metadata_Indicator_API_NY.GDP.PCAP.CD_DS2_en_csv_v2_10181232.csv
