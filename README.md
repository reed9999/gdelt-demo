# gdelt-demo


For the main showcase, [start 
here](https://github.com/reed9999/gdelt-demo/blob/master/Start_here.ipynb). You can view it in Jupyter Notebook or at that link.

This is an early-stage demo project to showcase my competency in Python and in data science; at the same time it has been a platform to build skills in AWS (and soon, Google Query as needed for real-time GDELT v.2), including Hadoop and to an extent Spark.
So far I have examples of analytics involving classification, using decision trees, *k* nearest neighbors, simple vector machines, and random forests.
I also have an example of linear regression.
As this project progresses, it will more extensively showcase a full data science life-cycle, but the pieces are already there in some form: exploratory analysis, hypothesis testing, data wrangling/data munging, modeling, and drawing conclusions.

GDELT is a multi-terabyte dataset of world events that, in its latest versions, 
is updated often and to a high granularity.
This project is exploratory, in the sense that I'm still getting a feel for the capabilities of 
the GDELT data.
In general, I'm interested in predicting precursors of violence, in media coverage of world events, and in network characteristics of how countries relate.

For [other projects in my showcase](https://github.com/reed9999/gdelt-demo/blob/master/readme_more.md#rest-of-showcase), a task list for this project, and other info, see readme\_more.md.
 
## Setup
Most of this code is Python 3 (3.5 or 3.6). To run the analysis code in Python,
you'll likely want to do the standard routine of `pip3 install -r requirements.txt`. 

## News and roadmap

For a while I had turned my attention away from this project to build some Python skills,
but as of mid-January 2019 I'm actively building it out.

At present I'm working on using the dyad queries (from Hadoop/Hive) to predict aggressive 
events, still using version 1 of GDELT. However, disappointingly it seems the only artifact 
I have of data\_related/features/dyad\_events\_by\_year.csv is only for 2016. I don't know
where the rest went but I am in the process of recreating it, which means revisiting my 
`automation` directory.

The roadmap is highly iterative and subject to change, as project roadmaps often should be.

1. 1. Proof of concept, done.
   1. 1. Done: Extract some features related to countries and how they 
relate. Demonstrate basic classification and clustering techniques. 
      1. Still to do: Add basic 
visualizations using matplotlib.
   3. Expand the universe of research questions under 
consideration and deploy the above tools to derive more "real world" value in 
the findings. Enhance visualizations.
   4. Consider alternative interfaces into the data, at a much higher level of
 sophistication and interactivity (e.g. Django site? Interactive 
 visualizations?) to make the findings more accessible to the public. 

## Skills demonstrated and accomplishments

### Skills

* **Ideation and asking "good questions"**: Since ideation is an important soft skill that I can contribute in abundance, I've documented my thought process in devising new questions.
 See research questions under Start\_here.ipynb.

* **Regression analysis** (Scikit-learn LinearRegression class): Findings in Start\_here.ipynb. See [analysis](https://github.com/reed9999/gdelt-demo/tree/master/queries/analysis) for code. 

* **SQL and HiveQL**: The most complex examples are my first cuts at feature 
extraction; see [queries/feature_extrac](https://github.com/reed9999/gdelt-demo/tree/master/queries/exploration). See [queries/exploration](https://github.com/reed9999/gdelt-demo/tree/master/queries/exploration). The SQL ones should run against a local MySQL. Many of the Hive ones will run against MySQL with minimal modification.
  
* **AWS setup** (S3, EMR cluster creation): Data engineering skills are not my 
highest priority, but they are useful to complement the purely data science skills.
  * **via CLI**: See [automation/scripts](https://github.com/reed9999/gdelt-demo/tree/master/automation/scripts).
  * **via boto3**: See [automation](https://github.com/reed9999/gdelt-demo/tree/master/automation).
  * **Hadoop on Elastic MapReduce (EMR)**: 

* **Spark** (via PySpark): See [queries/spark_sql](https://github.com/reed9999/gdelt-demo/tree/master/queries/spark_sql). 
Hadoop has worked fine with HiveQL, but 
  so far, my Spark apps hang when run as steps. Learning what's going on here will be helpful 
  to my overall understanding.
  
### Accomplishments
The preceding list is oriented toward showcasing specific skills, but the 
findings themselves (as enumerated in Start_here.ipynb) are an accomplishment. 
So far I've: 
* Found that media coverage of *in general*, holding constant the kinds of events covereed, 
tends to get more negative in general over time. By in general I mean that 
it's not just the lifespan of a given event (e.g. a war that lasts for years) 
but all coverage.
* Found that media coverage of events tends to be more positive for the kinds 
of events that promote stability, but not to what I would consider a great extent 
after controlling for the previous time effect.

In addition the automation itself is an accomplishment, because it starts to 
give structure and reproducibility to setting up various environments 
(local, remote SQL, AWS EMR) for analysis.

