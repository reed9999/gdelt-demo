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

## Roadmap

This is highly iterative and subject to change, as project roadmaps often should be.

1.1. (done in mid-Oct) - Proof of concept. Run a few basic descriptives and regressions.
1.2 (in progress, goal: Nov 15) - Extract some features related to countries and how they 
relate. Demonstrate basic classification and clustering techniques. Add basic 
visualizations using matplotlib.
1.3 (goal: Dec 31) - Expand the universe of research questions under 
consideration and deploy the above tools to derive more "real world" value in 
the findings. Enhance visualizations.
1.4 - Consider alternative interfaces into the data, at a much higher level of
 sophistication and interactivity (e.g. Django site? Interactive 
 visualizations?) to make the findings more accessible to the public. 

## Skills demonstrated and accomplishments

### Skills

* **Ideation / asking good questions**: See research questions under Start_here.ipynb.

* **Regression analysis** (Scikit-learn LinearRegression class): Findings in Start_here.ipynb. See [analysis](https://github.com/reed9999/gdelt-demo/tree/master/queries/analysis) for code. 

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

