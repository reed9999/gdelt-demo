# gdelt-demo


<!--borrowed shamelessly from https://www.w3schools.com/css/css_border.asp-->
<!--
<style>
oops. apparently GitHub doesn't deal well with this sort of markup.
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

<div class="w3-container w3-pale-blue w3-leftbar w3-border-blue reed9999-note">
-->
For the main showcase, <a href="https://github.com/reed9999/gdelt-demo/blob/master/Start-here.ipynb">start here</a>. If you have Jupyter Notebook installed, run `jupyter notebook` and then via the Web GUI access `Start-here.ipynb`. 
<!--
</div>
-->

Demonstration project--Learning to do interesting stuff with AWS and the GDELT dataset

This is an early-stage demo project to showcase my autodidactic process and my acquired skills. Broadly speaking the goal is to get better at ''doing data science'' (whatever that ends up meaning to me) while enhancing skills in Spark, AWS, Hadoop, and Python along the way.

For [more project background](#background) and [other projects I want to showcase](#rest-of-showcase), please see below.


## Currently working on...

Updated 2018-09-09. Some of these overlap with the "next steps" section below, 
but better to track everything that comes to mind rather than worry too much about defining each item.

1. Get my first attempts at Spark SQL to work well.
    1. Column names
1. Finish Karau et al.'s *Learning Spark* and integrate in here as helpful.
    1. Convert existing QL.
    2. Do more interesting queries.
    3. Use the fruits of those queries to do more interesting analysis if appropriate. 
1. Continuing to drive repetitive tasks with Python3 and boto3 rather than bash and CLI. Actually each is better for different things, but Python gives me more intuitive control over looping (I don't really love bash syntax) and supports my broader pedagogical goals. See `automation` directory.
1. Developing more interesting queries (and soon regressions) to get closer to answering RQs. For example I was exploring the Rosenstein score as a proxy for the positive or negative nature of each event, but `AvgTone` needs to come into play.   

## Accomplished so far
I've created several toy examples which can form the basis of my more serious work here. See `queries/hive` directory (to be converted to Spark SQL):

* `load-gdelt-events.q` is just a hacked example to create and populate our gdelt_events table.
* `first-demo-shorter.q` and `demo-*.q` from 003 to 010 are just simple queries to get familiar with this table.6

I have also been working through the Karau book, up to chapter 4 but also jumping to 9 on Spark SQL. 

## Next steps 
Updated 2018-09-09. Some of these overlap with each other, and also with the "working on" section above, 
but better not to lose track of them.

1. Build more analytical queries to at least the mid-range level--more meaningful than what I have now, and starting to build up toward my research questions, even if not quite 'production-quality' (i.e. my final RQs)
1. Better job of showcasing -- Web site or similar
1. Learn more about GDELT itself.
    1. Learn more about other ways people have used GDELT:
        * [linwoodc3/gdeltPyR](https://github.com/linwoodc3/gdeltPyR)
        * Examples at [AWS GDELT page](https://registry.opendata.aws/gdelt/)
    1. GDELT's setup on Google Big Query could be helpful here (if a tangent from my AWS tutelage). See [this explanation](https://www.gdeltproject.org/data.html).
1. Read everything I can find about data science on AWS -- SageMaker, Athena, Redshift. All buzzwords I barely understand.
1. Build more than just queries--regression, other data science techiques, etc.
1. Build "something more analytical" into a full suite showing data science understanding. (In other words, the presentation.)
1. Do more investigation on whether I can do my EMR creation in boto3. In particular, how do I choose the spot rate?
    1. Also refactor a lot of this stuff. Look for a third-party open-source wrapper. If it doesn't exist, just extract interesting params to a YAML file or similar.
. 
1. Automate pulling scripts from github to my S3 bucket.
1. Learn more about parquet and other storage formats.
.  

## <a name="background">Background</a>
I have some data sciencey, big dataish skills from my PhD program; now I need a millieu to showcase and keep building them.

The premise is that I want to use a big open dataset on AWS and do some analysis (using data science skills) while learning the AWS stuff. [GDELT, the Global Database of Events, Language and Tone](https://registry.opendata.aws/gdelt/) seems like a good choice because media and language are interesting to me.


## <a name="rest-of-showcase">The rest of the showcase</a>
This GDELT project is the latest one I'm building on here, but some of my previous work will also be of interest. See the respective README.md files for more:


* **[Thumbs up for Privacy?](https://github.com/reed9999/thumbs-up-for-privacy)** (R, regressions) [This is my first-authored paper](https://www.sciencedirect.com/science/article/pii/S0049089X16302368) using a million row dataset. This work was published as "Thumbs Up for Privacy?" in _Social Science Research_, by Reed, Spiro, and Butts. About 90% of the analysis, the prose, and the R code are my original work.

* **[Neural Networks and Deep Learning](https://github.com/reed9999/neural-networks-and-deep-learning)** (exploratory, Python, neural networks) I hacked around on Nielsen's eBook code. It shows my curiosity about one of the ''mysteries'' about ML to my social-science-educated brain: Why can't we improve predictions with a little bit of a theoretical nudge?

* **[EconGraphs](https://github.com/reed9999/econgraphs)** 
(Matplotlib, Django, Python) Plots arbitrary user-submitted functions. 
Intent is to make it easier for me to understand econ papers. Not very developed and probably has security holes, but a worthwhile Django/Matplotlib demo.

Rest of my github forked repos aren't showcasing anything yet, but stuff I want to hack around with.

* **Observing gender dynamics and disparities with mobile phone metadata** (highly exploratory, numpy/pandas, QGIS, billion-row dataset) No github repo.  [This was some exploratory work](https://dl.acm.org/citation.cfm?id=2909632) that died there because we couldn't find anything attention-grabbing to study. Although my colleague did most of the hardcore big-data it gave me a good chance to use numpy/pandas and to learn a little bit of QGIS.

I also did a good bit of qualitative research for my dissertation. I'm a big believer in mixed quant/qual methods.
