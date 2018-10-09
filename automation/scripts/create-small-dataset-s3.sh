## There may be more efficient ways to just create Hive tables off of selected
# data files that I don't know about yet. 
# Indeed, I'm pushing the bounds of what I want to keep in my S3 at the moment so haven't run this yet.

S3_BUCKET=s3://reed9999
SRC=$S3_BUCKET/data/events
DST=$S3_BUCKET/data/_small
#This is the entire list from the create-reed9999 file.
# aws s3 cp $SRC/1992.csv $DST
# aws s3 cp $SRC/1997.csv $DST
# aws s3 cp $SRC/1999.csv $DST
# aws s3 cp $SRC/2000.csv $DST
# aws s3 cp $SRC/2005.csv $DST
# aws s3 cp $SRC/200609.csv $DST
# aws s3 cp $SRC/200612.csv $DST
# aws s3 cp $SRC/200705.csv $DST
# aws s3 cp $SRC/200904.csv $DST
# aws s3 cp $SRC/20130401.export.csv $DST
# aws s3 cp $SRC/20130830.export.csv $DST
# aws s3 cp $SRC/20130831.export.csv $DST
# aws s3 cp $SRC/20140411.export.csv $DST
# aws s3 cp $SRC/20140430.export.csv $DST
# aws s3 cp $SRC/20150430.export.csv $DST
