##############################################################################
# pandas_gdelt_helper.py
# Helper module to facilitate the data manipulation involved in this project.

import glob
import logging
import os
import pandas as pd

THIS_FILE_DIR = os.path.dirname(__file__)
INDEPENDENT_COLUMNS = ['fractiondate','goldsteinscale']
LOCAL_DATA_DIR = "/home/philip/aws/data/original/events" #HARDCODED

#HARDCODED for now, but could make sense to externalize them as with events
# In which case DRY
def get_country_features_column_dtypes():
    return {
        #THIS WAY IT WORKS BUT IS MISALIGNED
        'name': 'object',
        # 'actual_name': 'object',
        'code': 'object',
        'actor1_relationships': 'object', #'int64',
        'actor2_relationships': 'int64',

        #ORIGINAL
        # 'code': 'object',
        # 'actor1_relationships': 'int64',
        # 'actor2_relationships': 'int64',

    }

#Misnomer - rename to events column names!
#It's also really redundant to return this tuple. Not sure what I was
# thinking. Just return the names as keys to the dict.
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
    names = [x['name'] for x in pairs]
    dtypes = {x['name']: x['dtype'] for x in pairs}
    return names, dtypes

def get_event_column_names():
    COLUMN_NAMES_FILE = os.path.normpath(
        os.path.join(THIS_FILE_DIR, "..", "data_related",
                    "events_column_names.csv")
    )
    with open(COLUMN_NAMES_FILE, 'r') as f:
        column_names = str(f.readline()).split('\t')
    return column_names

def get_events_local_medium():
    filenames = glob.glob(os.path.join(LOCAL_DATA_DIR, "????.csv"))
    filenames += glob.glob(os.path.join(LOCAL_DATA_DIR, "????????.export.csv"))
    # But not e.g., 20150219114500.export.csv, which I think is v 2.0
    assert len(filenames) > 0, "There should be at least one data file."

    return get_events_common(filenames)

def get_events_sample_tiny():
    TINY_DATA_DIR = os.path.join(THIS_FILE_DIR, "..", "data_related",
                                "sample_data")

    filenames = glob.glob(os.path.join(TINY_DATA_DIR, "events.csv"))
    return get_events_common(filenames)

def get_events_common(filenames):

    column_names, dtypes = get_event_column_names_dtypes()
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
        events_data = get_events_local_medium()
    except AssertionError as e:
        events_data = get_events_sample_tiny()
    report_on_nulls(events_data)
    events_data = events_data.dropna(subset=INDEPENDENT_COLUMNS)
    return events_data

def get_country_features():
    dtypes = get_country_features_column_dtypes()
    column_names = dtypes.keys()
    filename = os.path.join(THIS_FILE_DIR, '..', 'data_related', 'features',
                            'country_features.csv')
    # The following fails with the error
    # backtrace reproduced at the end of the file.
    # On Travis-CI it appeared to be Python 3.5 only (not 3.6 or 3.4)
    # but now it fails locally on 3.6 as well; don't know about 3.4

    country_features_data = pd.read_csv(filename, delimiter="\t",
                names=column_names, dtype=dtypes, index_col=['code'])
    return country_features_data
    # for column in [...]:
    #     events_data[column] = pd.to_numeric(events_data[column])

def get_country_external():
    filename = os.path.join(THIS_FILE_DIR, '..', 'data_related', 'external',
                            'API_NY.GDP.PCAP.CD_DS2_en_csv_v2_10181232.csv')
    data = pd.read_csv(filename, header=4)
    return data


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



#
# ~/code/gdelt-demo/analysis/pandas_gdelt_helper.py in get_country_features()
#     114                             'country_features.csv')
#     115     country_features_data = pd.read_csv(filename, delimiter="\t",
# --> 116                 names=column_names, dtype=dtypes, index_col=['code'])
#     117     return country_features_data
#     118     # for column in [...]:
#
# ~/.local/lib/python3.5/site-packages/pandas/io/parsers.py in parser_f(filepath_or_buffer, sep, delimiter, header, names, index_col, usecols, squeeze, prefix, mangle_dupe_cols, dtype, engine, converters, true_values, false_values, skipinitialspace, skiprows, nrows, na_values, keep_default_na, na_filter, verbose, skip_blank_lines, parse_dates, infer_datetime_format, keep_date_col, date_parser, dayfirst, iterator, chunksize, compression, thousands, decimal, lineterminator, quotechar, quoting, escapechar, comment, encoding, dialect, tupleize_cols, error_bad_lines, warn_bad_lines, skipfooter, doublequote, delim_whitespace, low_memory, memory_map, float_precision)
#     676                     skip_blank_lines=skip_blank_lines)
#     677
# --> 678         return _read(filepath_or_buffer, kwds)
#     679
#     680     parser_f.__name__ = name
#
# ~/.local/lib/python3.5/site-packages/pandas/io/parsers.py in _read(filepath_or_buffer, kwds)
#     444
#     445     try:
# --> 446         data = parser.read(nrows)
#     447     finally:
#     448         parser.close()
#
# ~/.local/lib/python3.5/site-packages/pandas/io/parsers.py in read(self, nrows)
#    1034                 raise ValueError('skipfooter not supported for iteration')
#    1035
# -> 1036         ret = self._engine.read(nrows)
#    1037
#    1038         # May alter columns / col_dict
#
# ~/.local/lib/python3.5/site-packages/pandas/io/parsers.py in read(self, nrows)
#    1846     def read(self, nrows=None):
#    1847         try:
# -> 1848             data = self._reader.read(nrows)
#    1849         except StopIteration:
#    1850             if self._first_chunk:
#
# pandas/_libs/parsers.pyx in pandas._libs.parsers.TextReader.read()
#
# pandas/_libs/parsers.pyx in pandas._libs.parsers.TextReader._read_low_memory()
#
# pandas/_libs/parsers.pyx in pandas._libs.parsers.TextReader._read_rows()
#
# pandas/_libs/parsers.pyx in pandas._libs.parsers.TextReader._convert_column_data()
#
# pandas/_libs/parsers.pyx in pandas._libs.parsers.TextReader._convert_tokens()
#
# ValueError: invalid literal for int() with base 10: 'BOL'
# ValueError: invalid literal for int() with base 10: 'BOL'
