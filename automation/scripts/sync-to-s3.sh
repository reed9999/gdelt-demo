S3_BUCKET=s3://reed9999
SCRIPTS_DIR=$S3_BUCKET/scripts
QUERIES_DIR=$S3_BUCKET/queries
aws s3 sync ~/aws/gdelt-demo/scripts/ $SCRIPTS_DIR
aws s3 sync ~/aws/gdelt-demo/queries/ $QUERIES_DIR
