##############################################################################
# pandas_gdelt_helper.py
# Helper module to facilitate the data manipulation involved in this project.
# See readme_data.md for details on the different data sources. I've created a few too many
# different ones and need to consolidate.
# For CAMEO codes see http://eventdata.parusanalytics.com/data.dir/cameo.html
# (latest: http://eventdata.parusanalytics.com/cameo.dir/CAMEO.Manual.1.1b3.pdf )

# I would like to get rid of the get_ prefix in function names below. This is more of a Ruby
# tendency, but it makes the code read more like plain English and the get_ adds little value.
import glob
import logging
import os
import pandas as pd

THIS_FILE_DIR = os.path.dirname(__file__)
INDEPENDENT_COLUMNS = ['fractiondate','goldsteinscale']
LOCAL_DATA_DIR = "/home/philip/data-gdelt" #HARDCODED
HIGH_INCOME_THRESHOLD = 30000.00
# Also worth considering: We could calculate a threshold using mean, stdev, etc.
# or just search for an international standard for "high income"

# DRY -- there should be one canonical place where we maintain the fields list for all
# our data tables, be they flat files, MySQL, Hive, etc.
# It might be worth looking at something like Django migrations just to standardize.
COUNTRY_FEATURES_COLUMN_DTYPES = {
    #At one point these were coming out misaligned, but that doesn't appear to be a problem now.
        'name': 'object',
        'code': 'object',
        'actor1_relationships': 'int64',
        'actor2_relationships': 'int64',
    }
DYAD_EVENTS_BY_YEAR_DTYPES= {
    #At one point these were coming out misaligned, but that doesn't appear to be a problem now.
    # CREATE TABLE IF NOT EXISTS dyad_events_by_year AS
    # SELECT year, actor1code, actor2code, eventcode,
    # -- I don't see why I can't join on a group field but for for now this throws an error.
    # -- eventcodes.description,
    # eventbasecode,  eventrootcode, goldsteinscale, count(*) as count_events
    # FROM events LEFT JOIN eventcodes
    #   ON eventcodes.code = events.eventcode
    # GROUP BY year, actor1code, actor2code, eventcode,
        'year': 'int64',
        'actor1code': 'object',
        'actor2code': 'object',
        'eventcode': 'object',
        'eventbasecode': 'object',
        'eventrootcode': 'object',
        'goldsteinscale': 'float64',
        'count_events': 'int64',
    }

# Obviously this is a judgment call and some included (like 14 Protest) or excluded are debatable.
AGGRESSIVE_CAMEO_FAMILIES = ['13', '14', '15', '16', '17', '18', '19', '20']

# TODO REFACTOR the others -- soon.
FILENAMES = {
    # not yet in use
    'country_features':  os.path.join(THIS_FILE_DIR, '..', 'data_related', 'features',
                            'country_features.csv'),
    'dyad_events_by_year':  os.path.join(THIS_FILE_DIR, '..', 'data_related', 'features',
                            'dyad_events_by_year.csv'),
}
class PandasGdeltHelper():
    pass

def get_event_column_names_dtypes():
    COLUMN_NAMES_DTYPES_FILE = os.path.normpath(
        os.path.join(THIS_FILE_DIR, "..", "data_related",
                    "events_column_names_dtypes.csv")
    )
    with open(COLUMN_NAMES_DTYPES_FILE, 'r') as f:
        lines = f.readlines()
        pairs = [{'name': x.split('\t')[0], 'dtype': x.split('\t')[1].rstrip()}
            for x in lines]
        # pairs = str(f.readline()).split('\t')
    dtypes = {x['name']: x['dtype'] for x in pairs}
    return dtypes

def get_event_column_names():
    COLUMN_NAMES_FILE = os.path.normpath(
        os.path.join(THIS_FILE_DIR, "..", "data_related",
                    "events_column_names.csv")
    )
    with open(COLUMN_NAMES_FILE, 'r') as f:
        column_names = str(f.readline()).split('\t')
    return column_names

def get_events_from_local_medium_sized():
    filenames = glob.glob(os.path.join(LOCAL_DATA_DIR, "????.csv"))
    filenames += glob.glob(os.path.join(LOCAL_DATA_DIR, "????????.export.csv"))
    # But not e.g., 20150219114500.export.csv, which I think is v 2.0
    if len(filenames) > 0:
        raise FileNotFoundError("There should be at least one data file. Is the medium-sized CSV db set up here?")
    return get_events_common(filenames)

def get_events_from_sample_data():
    TINY_DATA_DIR = os.path.join(THIS_FILE_DIR, "..", "data_related",
                                "sample_data")

    filenames = glob.glob(os.path.join(TINY_DATA_DIR, "events.csv"))
    return get_events_common(filenames)

def get_events_common(filenames):
    """Common refactored functionality to get the events files whether in the sample data or
    in my s3 downloads"""
    dtypes = get_event_column_names_dtypes()
    column_names = dtypes.keys()
    events_data = pd.DataFrame(columns=column_names, dtype=None)
    # This didn't work later in the execution but maybe with the empty
    # DataFrame
    for column in ['nummentions', 'numsources', 'numarticles']:
        events_data[column] = pd.to_numeric(events_data[column])

    for filename in filenames:
        try:
            new_df = pd.read_csv(filename, delimiter="\t", names=column_names,
                                dtype=dtypes, index_col=['globaleventid'])
        except Exception:
            logging.info("""Fell through to non-dtype (i.e. slow) handling 
                on filename: {}""".format(filename))
            new_df = pd.read_csv(filename, delimiter="\t", names=column_names,
                                dtype=None, index_col=['globaleventid'])
        try:
            events_data = pd.concat([new_df, events_data], sort=False)
        except TypeError:
            logging.info("""Version compatibility. Jupyter runs an older
                version of pandas.""")
            events_data = pd.concat([events_data, new_df], )
    return events_data

def get_events():
    try:
        events_data = get_events_from_local_medium_sized()
    except AssertionError as e:
        events_data = get_events_from_sample_data()
    report_on_nulls(events_data)
    events_data = events_data.dropna(subset=INDEPENDENT_COLUMNS)
    return events_data

def clean_up_external_country_columns(dataframe):
    """Delete unhelpful columns from 1960 to 2016, inclusive"""
    labels = [str(i) for i in range(1960, 2017)]
    dataframe.drop(axis='columns', columns=labels, inplace=True)
    return dataframe


def get_external_country_data():
    filename = os.path.join(THIS_FILE_DIR, '..', 'data_related', 'external',
                            'API_NY.GDP.PCAP.CD_DS2_en_csv_v2_10181232.csv')
    column_criterion = lambda x: x[0:7] != "Unnamed"
    dataframe = pd.read_csv(filename, delimiter=",", skiprows=4, dtype=None,
                            index_col='Country Code', usecols=column_criterion,
                            )
    tweak_external_data_country_codes(dataframe)
    clean_up_external_country_columns(dataframe)
    dataframe['is_high_income'] = dataframe['2017'] >= HIGH_INCOME_THRESHOLD
    return dataframe


def get_country_features():
    dtypes = COUNTRY_FEATURES_COLUMN_DTYPES
    column_names = dtypes.keys()
    filename = os.path.join(THIS_FILE_DIR, '..', 'data_related', 'features',
                            'country_features.csv')
    country_features_data = pd.read_csv(filename, delimiter="\t",
                names=column_names, dtype=dtypes, index_col=['code'])
    external_data = get_external_country_data()
    return country_features_data.join(other=external_data, how='inner')
    # for column in [...]:
    #     events_data[column] = pd.to_numeric(events_data[column])


def tweak_external_data_country_codes(ext_data):
    """For those cases where an external data source uses different country codes for what is
    obviously the same country as GDELT, convert them all to the GDELT name.
    It turns out there are only two obvious cases where the same country has different codes.

    Returns: The input data frame.
    Side effects: Changes the data frame in place rather than cloning.
    """
    TWEAKS = {
        'ROU': 'ROM',   #Romania
        'TLS': 'TMP',   #Timor-Leste
    }
    #https://stackoverflow.com/a/40428133
    as_list = ext_data.index.tolist()
    for ext_code, feature_code in TWEAKS.items():
        index = as_list.index(ext_code)
        as_list[index] = feature_code
    ext_data.index = as_list
    return ext_data

# The next functions are utilities that probably don't need to be preserved here.
# TODO maybe offload util functions to a separate file?

def report_on_nulls(events_data):
    count_null = events_data.isna().sum().sum()
    count_goldstein_null = events_data.goldsteinscale.isna().sum()
    count_avgtone_null = events_data.avgtone.isna().sum()
    if count_goldstein_null > 0:
        logging.warning(
            "{} rows have NA in goldsteinscale out of {} total nulls".format(
                count_goldstein_null, count_null
            ))
    if count_avgtone_null > 0:
        logging.warning(
            "{} rows have NA in avgtone out of {} total nulls".format(
                count_avgtone_null, count_null
            ))

def util_report_on_country_mismatches():
    """This utility function made sense to help me discover what tweaks were necessary.
    To return everything to the original state (in a messy hacky way), remove the tweak call from
    get_external_country_data()
    """
    assert False, """This is now broken: 
    ValueError: columns overlap but no suffix specified"""
    feat = get_country_features()
    ext = get_external_country_data()
    joined = feat.join(ext, how='outer')
    print(joined.columns)

    external_nans = joined['2017'].isna()
    feature_nans = joined['name'].isna()
    print("Here are the countries in GDELT features but not GDP data:\n")
    print(joined[external_nans]['name'])
    print("Here are the countries in GDP data but not GDELT features:\n")
    print(joined[feature_nans]['Country Name'])

# REFACTORING attempt but not yet turned on.
def open_csv_for_table(table, dtypes=None,):
    # I should refactor so the optional param is not needed.
    filename = FILENAMES[table]
    column_names = list(dtypes.keys()) #DRY, copied from country_features
    n = len(column_names)
    df = pd.read_csv(filename, delimiter="\t",
                names=column_names, dtype=dtypes,
                error_bad_lines=False,
                # usecols=range(0, n),
                           ) # also tried: .dropna() #index_col=['code'])
    return df

def dyad_events_by_year():
    dtypes = DYAD_EVENTS_BY_YEAR_DTYPES
    df = open_csv_for_table('dyad_events_by_year')
    assert df is not None
    return df


def dyad_aggression_by_year():
    dtypes = DYAD_EVENTS_BY_YEAR_DTYPES
    column_names = list(dtypes.keys()) #DRY, copied from country_features
    n = len(column_names)
    filename = FILENAMES['dyad_events_by_year']
    dyad_events_by_year = pd.read_csv(filename, delimiter="\t",
                names=column_names, dtype=dtypes,
                error_bad_lines=False,
                usecols=range(0, n), #without this I get cannot convert float NaN to integer
                           ) # also tried: .dropna() #index_col=['code'])

    # dyad_events_by_year = pd.read_csv(FILENAMES['dyad_events_by_year'], delimiter="\t",
    #                                   names=DYAD_EVENTS_BY_YEAR_DTYPES.keys(),
    #                                   # dtype=None,
    #                                   # index_col=['...???...'],
    #                                   )
    assert dyad_events_by_year is not None
    data = dyad_events_by_year
    data['eventfamily'] = list(map(lambda x: x[:2], data['eventbasecode']))
    criterion = data['eventfamily'].isin(AGGRESSIVE_CAMEO_FAMILIES)

    #The following is patently not the way to do this. Indexing on a Boolean list
    # selects the rows for True leading to a shape mismatch.
    data['is_aggressive'] = data['eventrootcode'].isin(AGGRESSIVE_CAMEO_FAMILIES)
    foo = data.groupby([
        'actor1code',
        'actor2code',
        'year',
        'is_aggressive',
    ])
    rv = data.groupby([
        'actor1code',
        'actor2code',
        'year',
        'is_aggressive',
    ])['count_events'].sum()
    return rv

def country_aggression_by_year():
    country_df = get_country_features()
    assert country_df is not None

    raise NotImplementedError


if __name__ == "__main__":
    #simple test of new functionality
    features = get_country_features()
    is_high_income = features['is_high_income']
    pass
