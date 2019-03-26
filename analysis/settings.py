# Settings pertaining to what's under the analysis directory (regressions,
# classification tasks, etc.)

import os
PATHS = {
    # This is a local database that's too big for me to want to put it on Github (in spite of the
    # large file handling there) but should be in a consistent place. This path was my old place.
    'legacy-local-data': os.path.join('/home', 'philip', 'data-gdelt'),
    'sample-data': os.path.join('..', 'data_related', 'sample_data'),
    #underscores when it's referring to a table name
    'country_features':  os.path.join('..', 'data_related', 'features',
                            'country_features.csv'),
    'dyad_events_by_year':  os.path.join('..', 'data_related', 'features',
                            'dyad_events_by_year.csv'),
}

SCHEMA = {
    'events' : {
        'independent-columns': ['fractiondate','goldsteinscale'],
        # Obviously this is a judgment call and some included (like 14 Protest) or excluded
        # are debatable.
        'aggressive-cameo-families': ['13', '14', '15', '16', '17', '18', '19', '20'],
    },

}

MYSQL = {
    'server': '',   #not yet in use
}

MISC = {
    'high-income-threshold': 30000.00,
}