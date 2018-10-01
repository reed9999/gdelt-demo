# gdelt-demo


<!--div class="w3-container w3-pale-blue w3-leftbar w3-border-blue reed9999-note">-->
For the main showcase, <a href="https://github.com/reed9999/gdelt-demo/blob/master/Start-here.ipynb">start here</a>. If you have Jupyter Notebook installed, run `jupyter notebook` and then via the Web GUI access `Start-here.ipynb`. 
<!--/div-->

Demonstration project--Learning to do interesting stuff with AWS and the GDELT dataset

This is an early-stage demo project to showcase my autodidactic process and my acquired skills. Broadly speaking the goal is to get better at ''doing data science'' (whatever that ends up meaning to me) while enhancing skills in Spark, AWS, Hadoop, and Python along the way.

For [other projects I want to showcase](https://github.com/reed9999/gdelt-demo/blob/master/readme-more.md#rest-of-showcase), a task list for this project, and other info, see readme-more.md.

## Setup
To run the analysis code in Python, you'll likely want to do the standard routine of `pip install -r requirements.txt`. 
I'm working on getting it to run on a small subset of GDELT data that this repo has installed in db-related/sample-db.

## Accomplishments
### Skills demonstrated

* **Ideation / asking good questions**: See research questions under Start-here.ipynb.

* **Regression analysis** (Scikit-learn LinearRegression class): Findings in Start-here.ipynb. See [analysis](https://github.com/reed9999/gdelt-demo/tree/master/queries/analysis) for code. 

* **Hive QL and SQL**: Exploratory queries for now. See [queries/exploration](https://github.com/reed9999/gdelt-demo/tree/master/queries/exploration). The SQL ones should run against a local MySQL. Many of the Hive ones will run against MySQL with minimal modification.
  
* **Spark** (via PySpark): See [queries/spark_sql](https://github.com/reed9999/gdelt-demo/tree/master/queries/spark-sql). 

* **AWS setup** (S3, EMR cluster creation): These are some data engineering skills to complement the purely data science skills.
  * **via CLI**: See [automation/scripts](https://github.com/reed9999/gdelt-demo/tree/master/automation/scripts).
  * **via boto3**: See [automation](https://github.com/reed9999/gdelt-demo/tree/master/automation).
  * **Hadoop and Spark on Elastic MapReduce**: Hadoop has worked fine with HiveQL, but 
  so far, my Spark apps hang when run as steps. Learning what's going on here will be helpful 
  to my overall understanding.

### Other accomplishments
I've created several toy examples which can form the basis of my more serious work here. See `queries/hive` directory (to be converted to Spark SQL):

* `load-gdelt-events.q` is just a hacked example to create and populate our gdelt_events table.
* `first-demo-shorter.q` and `demo-*.q` from 003 to 010 are just simple queries to get familiar with this table.6



<!--borrowed shamelessly from https://www.w3schools.com/css/css_border.asp-->
<!--but GitHub doesn't deal well with this sort of markup. -->
<!-- 
<style>
.w3-container:after,.w3-container:before,.w3-panel:after,.w3-panel:before,.w3-row:after,.w3-row:before,.w3-row-padding:after,.w3-row-padding:before,
.w3-cell-row:before,.w3-cell-row:after,.w3-clear:after,.w3-clear:before,.w3-bar:before,.w3-bar:after{content:"";display:table;clear:both}
.w3-pale-blue,.w3-hover-pale-blue:hover{color:#000!important;background-color:#ddffff!important}
.w3-purple,.w3-hover-purple:hover{color:#fff!important;background-color:#9c27b0!important}
.w3-leftbar{border-left:6px solid #ccc!important}.w3-rightbar{border-right:6px solid #ccc!important}
.w3-border-blue,.w3-hover-border-blue:hover{border-color:#2196F3!important}
.w3-border-purple,.w3-hover-border-purple:hover{border-color:#9c27b0!important}
.w3-border-deep-purple,.w3-hover-border-deep-purple:hover{border-color:#673ab7!important}
.reed9999-note {padding:10px; font-size: medium; font-weight:bold;}
p.reed9999-note{font-weight:bold;}
</style>
-->
