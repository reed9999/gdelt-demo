# Settings pertaining to what's under the analysis directory (regressions,
# classification tasks, etc.)

import os
PATHS = {
    # This is a local database that's too big for me to want to put it on Github (in spite of the
    # large file handling there) but should be in a consistent place. This path was my old place.
    'legacy-local-data': os.path.join('/home', 'philip', 'data-gdelt'),
    'sample-data': os.path.join('data_related', 'sample_data'),
    #underscores when it's referring to a table name
    'country_features':  os.path.join('data_related', 'features',
                            'country_features.csv'),
    'dyad_events_by_year':  os.path.join('data_related', 'features',
                            'dyad_events_by_year.csv'),
}

SCHEMA = {
    'events' : {
        'independent-columns': ['fractiondate','goldsteinscale'],
        # Obviously this is a judgment call and some included (like 14 Protest) or excluded
        # are debatable.
        'aggressive-cameo-families': ['13', '14', '15', '16', '17', '18', '19', '20'],
        'columns-dtypes': {
            'globaleventid': 'int64',
            'day': 'int64',
            'monthyear': 'int64',
            'year': 'int64',
            'fractiondate': 'float64',
            'actor1code': 'object',
            'actor1name': 'object',
            'actor1countrycode': 'object',
            'actor1knowngroupcode': 'object',
            'actor1ethniccode': 'object',
            'actor1religion1code': 'object',
            'actor1religion2code': 'object',
            'actor1type1code': 'object',
            'actor1type2code': 'object',
            'actor1type3code': 'object',
            'actor2code': 'object',
            'actor2name': 'object',
            'actor2countrycode': 'object',
            'actor2knowngroupcode': 'object',
            'actor2ethniccode': 'object',
            'actor2religion1code': 'object',
            'actor2religion2code': 'object',
            'actor2type1code': 'object',
            'actor2type2code': 'object',
            'actor2type3code': 'object',
            'isrootevent': 'bool',
            'eventcode': 'int64',
            'eventbasecode': 'int64',
            'eventrootcode': 'int64',
            'quadclass': 'int64',
            'goldsteinscale': 'float64',
            'nummentions': 'int64',
            'numsources': 'int64',
            'numarticles': 'int64',
            'avgtone': 'float64',
            'actor1geo_type': 'float64',	### Float because NAs preclude Pandas treating it as int64
            'actor1geo_fullname': 'object',
            'actor1geo_countrycode': 'object',
            'actor1geo_adm1code': 'object',
            'actor1geo_lat': 'float64',
            'actor1geo_long': 'float64',
            'actor1geo_featureid': 'object',
            'actor2geo_type': 'float64',
            'actor2geo_fullname': 'object',
            'actor2geo_countrycode': 'object',
            'actor2geo_adm1code': 'object',
            'actor2geo_lat': 'float64',
            'actor2geo_long': 'float64',
            'actor2geo_featureid': 'object',
            'actiongeo_type': 'float64',
            'actiongeo_fullname': 'object',
            'actiongeo_countrycode': 'object',
            'actiongeo_adm1code': 'object',
            'actiongeo_lat': 'float64',
            'actiongeo_long': 'float64',
            'actiongeo_featureid': 'object',	### Seems to be alphanumeri
            'dateadded': 'int64',
            'sourceurl': 'object',
        }
    },

}

MYSQL = {
    'server': '',   #not yet in use
}

MISC = {
    'high-income-threshold': 30000.00,
}