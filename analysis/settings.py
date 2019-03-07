# Settings pertaining to what's under the analysis directory (regressions,
# classification tasks, etc.)

PATHS = {
    'legacy-local-data': '/home/philip/data-gdelt',
}

SCHEMA = {
    'events' : {
        'independent-columns': ['fractiondate','goldsteinscale'],
        'aggressive-cameo-families': ['13', '14', '15', '16', '17', '18', '19', '20'],

    },

}

MYSQL = {
    'server': '',   #not yet in use
}

MISC = {
    'high-income-threshold': 30000.00,
}