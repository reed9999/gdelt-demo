# gdelt-demo: Supplement to the README

<!--div class="w3-container w3-pale-blue w3-leftbar w3-border-blue reed9999-note">-->
For the main showcase, <a href="https://github.com/reed9999/gdelt-demo/blob/master/Start-here.ipynb">start here</a>. If you have Jupyter Notebook installed, run `jupyter notebook` and then via the Web GUI access `Start-here.ipynb`. 
<!--/div-->

I want to keep [the main README.md](https://github.com/reed9999/gdelt-demo/blob/master/README.md) brief, so this is excess material. Below you'll find: 

* The non-GDELT projects I want to showcase.
* The tasks I'm working on for this GDELT project.
* What I've accomplished. However, I will merge this with the list of skills demonstrated (even though they're subtly different) so see also the README for that.
* My ideation about next steps.


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



## Currently working on...

Updated 2018-09-09. Some of these overlap with the "next steps" section below, 
but better to track everything that comes to mind rather than worry too much about defining each item.

1. Add some classification demos.
    1. Extract appropriate features. I'm thinking something like: Find external GDP data. Extract features like number of connections.  
1. Polish up my regression examples
    1. Find something more meaningful to plot and include the 

1. I moved Spark learning down my list a bit to focus on demonstrating "real data science" competencies. For now I'm running on my own arbitrary subset of the data, but I want this to run on Spark on AWS. Troubleshoot why my previous attempts at Spark on AWS EMR didn't seem to work.
1. Continuing to drive repetitive tasks with Python3 and boto3 rather than bash and CLI. Actually each is better for different things, but Python gives me more intuitive control over looping (I don't really love bash syntax) and supports my broader pedagogical goals. See `automation` directory.
1. Developing other interesting regressions to get closer to answering RQs. For example I was exploring the Rosenstein score as a proxy for the positive or negative nature of each event, but `AvgTone` needs to come into play.   


## Next steps 
Updated 2018-09-09. Some of these overlap with each other, and also with the "working on" section above, 
but better not to lose track of them.

1. Build more analytical queries to at least the mid-range level--more meaningful than what I have now, and starting to build up toward my research questions, even if not quite 'production-quality' (i.e. my final RQs)
1. Learn more about GDELT itself.
    1. Learn more about other ways people have used GDELT:
        * [linwoodc3/gdeltPyR](https://github.com/linwoodc3/gdeltPyR)
        * Examples at [AWS GDELT page](https://registry.opendata.aws/gdelt/)
    1. GDELT's setup on Google Big Query could be helpful here (if a tangent from my AWS tutelage). See [this explanation](https://www.gdeltproject.org/data.html).
1. Clean up the GDELT data. See explore-dyads-by-avgtone.sql: ITALIAN/ITALY, ESP miscoded as being in IT, etc.
1. Read everything I can find about data science on AWS -- SageMaker, Athena, Redshift. All buzzwords I barely understand.
1. Build more than just queries--regression, other data science techiques, etc.
1. Build "something more analytical" into a full suite showing data science understanding. (In other words, the presentation.)
1. Better job of showcasing -- Web site or similar
1. Finish Karau et al.'s *Learning Spark* and integrate in here as helpful. I have worked up to chapter 4 but also jumped to 9 on Spark SQL. 
    1. Convert existing QL.
    2. Do more interesting queries.
    3. Use the fruits of those queries to do more interesting analysis if appropriate. 
1. Do more investigation on whether I can do my EMR creation in boto3. In particular, how do I choose the spot rate?
    1. Also refactor a lot of this stuff. Look for a third-party open-source wrapper. If it doesn't exist, just extract interesting params to a YAML file or similar.
. 
1. Automate pulling scripts from github to my S3 bucket.
1. Learn more about parquet and other storage formats.
.  


