S3_BUCKET=s3://reed9999
SCRIPTS_DIR=$S3_BUCKET/scripts
QUERIES_DIR=$S3_BUCKET/queries
aws s3 sync ~/aws/gdelt-demo/automation/scripts/ $SCRIPTS_DIR
# aws s3 sync ~/aws/gdelt-demo/queries/ $QUERIES_DIR
aws s3 sync ~/aws/gdelt-demo/queries/data-engineering $QUERIES_DIR/data-engineering
aws s3 sync ~/aws/gdelt-demo/queries/data-engineering/hive $QUERIES_DIR/data-engineering/hive
