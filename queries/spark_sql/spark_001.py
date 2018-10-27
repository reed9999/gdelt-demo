###############################################################################
# First demo script for spark_sql to explore the spark-submit workflow that
# I'll be using in production.


# Neither one of these works as a standalone Python script unless PySpark is
# installed separately. I think my original intent was to have a script I could
# paste in at the command prompt. At any rate, this minimal case is *too*
# minimal to still be useful for troubleshoot.

# Before I had
import spark.sql.HiveContext
# In other contexts I have
#import pyspark.sql.HiveContext
