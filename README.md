# gdelt-demo


For the main showcase, [start 
here](https://github.com/reed9999/gdelt-demo/blob/master/Start_here.ipynb). 
If you have Jupyter Notebook installed (automatic if you follow the pip3 
instructions below), run `jupyter notebook Start_here.ipynb` or simply
`jupyter notebook` and navigate in the Web GUI. 

This is an early-stage demo project to showcase my autodidactic process and my
acquired skills. Broadly speaking the goal is to continuing building on my 
competency in Python including data science libraries, regression analysis, 
and other data science fundamentals while building skills in Spark, AWS and 
exploring real world questions with DS methodologies that I'd like to continue
enhancing.

For [other projects in my showcase](https://github.com/reed9999/gdelt-demo/blob/master/readme_more.md#rest-of-showcase), a task list for this project, and other info, see readme_more.md.
 
## Setup
Most of this code is Python 3 (3.5 or 3.6). To run the analysis code in Python,
you'll likely want to do the standard routine of `pip3 install -r requirements.txt`. 

## Skills demonstrated and other accomplishments


* **Ideation / asking good questions**: See research questions under Start_here.ipynb.

* **Regression analysis** (Scikit-learn LinearRegression class): Findings in Start_here.ipynb. See [analysis](https://github.com/reed9999/gdelt-demo/tree/master/queries/analysis) for code. 

* **SQL and HiveQL**: The most complex examples are my first cuts at feature 
extraction; see [queries/feature_extrac](https://github.com/reed9999/gdelt-demo/tree/master/queries/exploration). See [queries/exploration](https://github.com/reed9999/gdelt-demo/tree/master/queries/exploration). The SQL ones should run against a local MySQL. Many of the Hive ones will run against MySQL with minimal modification.
  
* **Spark** (via PySpark): See [queries/spark_sql](https://github.com/reed9999/gdelt-demo/tree/master/queries/spark_sql). 

* **AWS setup** (S3, EMR cluster creation): These are some data engineering skills to complement the purely data science skills.
  * **via CLI**: See [automation/scripts](https://github.com/reed9999/gdelt-demo/tree/master/automation/scripts).
  * **via boto3**: See [automation](https://github.com/reed9999/gdelt-demo/tree/master/automation).
  * **Hadoop and Spark on Elastic MapReduce**: Hadoop has worked fine with HiveQL, but 
  so far, my Spark apps hang when run as steps. Learning what's going on here will be helpful 
  to my overall understanding.

### Other accomplishments
I've created several toy examples which can form the basis of my more serious work here. See `queries/hive` directory (to be converted to Spark SQL):

* `load_gdelt_events.q` is just a hacked example to create and populate our gdelt_events table.
* `first_demo_shorter.q` and `demo_*.q` from 003 to 010 are just simple queries to get familiar with this table.6


