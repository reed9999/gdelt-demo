## There may be more efficient ways to just create Hive tables off of selected
# data files that I don't know about yet. 
# My kludge is to copy only about 10% or less of the files to my own s3, hoping
# that's little enough not to incur huge s3 charges.

# However this still fills up more s3 space than I want to, so I'll selectively 
# pare it down too. 
S3_BUCKET=s3://reed9999
SRC=s3://gdelt-open-data/events
DST=$S3_BUCKET/data/events/
#already have 1979 thru 1982
aws s3 cp $SRC/1990.csv $DST
aws s3 cp $SRC/1992.csv $DST
aws s3 cp $SRC/1997.csv $DST
aws s3 cp $SRC/1999.csv $DST
aws s3 cp $SRC/2000.csv $DST
aws s3 cp $SRC/2005.csv $DST
aws s3 cp $SRC/200609.csv $DST
aws s3 cp $SRC/200612.csv $DST
aws s3 cp $SRC/200705.csv $DST
aws s3 cp $SRC/200904.csv $DST
aws s3 cp $SRC/20130401.export.csv $DST
aws s3 cp $SRC/20130830.export.csv $DST
aws s3 cp $SRC/20130831.export.csv $DST
aws s3 cp $SRC/20140411.export.csv $DST
aws s3 cp $SRC/20140430.export.csv $DST
aws s3 cp $SRC/20150430.export.csv $DST
