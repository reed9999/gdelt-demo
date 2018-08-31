# gdelt-demo
Demonstration project--Learning to do interesting stuff with AWS and the GDELT dataset

This is an early-stage demo project to showcase my autodidactic process for learning about AWS and in particular how to ''do data science'' (whatever that ends up meaning to me) on AWS. The main goal is to demonstrate the value of my work to potential employers.

## The rest of the showcase
This GDELT project is the latest one I'm building on here, but some of my previous work will also be of interest. See the respective README.md files for more:


* **[Thumbs up for Privacy?](https://github.com/reed9999/thumbs-up-for-privacy)** (R, regressions) [This is my first-authored paper](https://www.sciencedirect.com/science/article/pii/S0049089X16302368) using a million row dataset. This work was published as "Thumbs Up for Privacy?" in _Social Science Research_, by Reed, Spiro, and Butts. About 90% of the analysis, the prose, and the R code are my original work.

* **[Neural Networks and Deep Learning](https://github.com/reed9999/neural-networks-and-deep-learning)** (exploratory, Python, neural networks) I hacked around on Nielsen's eBook code. It shows my curiosity about one of the ''mysteries'' about ML to my social-science-educated brain: Why can't we improve predictions with a little bit of a theoretical nudge?

* **[EconGraphs](https://github.com/reed9999/econgraphs)** (Matplotlib, Django, Python) Plots arbitrary functions to. Intent is to make it easier for me to understand econ papers. Not very developed and probably has security holes, but a worthwhile Django/Matplotlib demo.

Rest of my github forked repos aren't showcasing anything yet, but stuff I want to hack around with.

* **Observing gender dynamics and disparities with mobile phone metadata** (highly exploratory, numpy/pandas, QGIS, billion-row dataset) No github repo.  [This was some exploratory work](https://dl.acm.org/citation.cfm?id=2909632) that died there because we couldn't find anything attention-grabbing to study. Although my colleague did most of the hardcore big-data it gave me a good chance to use numpy/pandas and to learn a little bit of QGIS.

I also did a good bit of qualitative research for my dissertation. I'm a big believer in mixed quant/qual methods.

## Research questions
What makes this more than just a SQL tutorial? For one thing, my intent to use this data to address interesting RQs.

In this kind of research there's some iteration in RQs, because things you think *a priori* might be interesting turn out not to be, and vice versa. But it's good to keep a running list of ideas.

1. **Actor affinity by dyad** - Do some actor dyads consistently produce higher Rosenstein scores than others? I'd think this would be a trivial "Yes" because relationships between allies should produce more positive news than those between adversaries. So this is exploring the obvious, but a good sanity check to make sure I'm understanding the nature of this data.
  1. **Asymmetrical relationships** - Just brainstorming. If X threatens Y more than Y threatens X that's also significant and interesting.


## Currently working on...

1. I'm continuing to learn Hive QL which also means brushing up on SQL. See `queries` directory: Right now, everything up to `demo-010` should work, but `demo-011` fails. Its cousin is the `mysql` directory which has some MySQLized versions of setup scripts.

## Accomplished so far
I've created several toy examples which can form the basis of my more serious work here. See `queries` directory:

* `load-gdelt-events.q` is just a hacked example to create and populate our gdelt_events table.
* `first-demo-shorter.q` and `demo-*.q` from 003 to 010 are just simple queries to get familiar with this table.6
I have also just installed my own local Spark, HDFS, and Hive, and am beginning to play around with them.

## Next steps (last update: 2018-08-31)
1. Finish installation of Hive on my local computer for easier QL debugging.
1. Learn more about Hive and about PySpark and integrate in here as helpful.
    1. Confirm or finish my install of Spark and PySpark
1. Automate pulling scripts from github to my S3 bucket.
1. Automate creating cluster with step[s] then terminating.
1. Build more analytical queries to at least the mid-range level--more meaningful than what I have now, and starting to build up toward my research questions, even if not quite 'production-quality' (i.e. my final RQs)
1. Finish installation of Hive on my local computer for easier QL debugging. Less important now that AWS RDS is on the way.  
1. Learn more about GDELT itself.
    1. GDELT's setup on Google Big Query could be helpful here (if a tangent from my AWS tutelage). See [this explanation](https://www.gdeltproject.org/data.html).
1. Build "something more analytical" into a full suite showing data science understanding.

## Background
I have some data sciencey, big dataish skills from my PhD program; now I need a millieu to showcase and keep building them.

The premise is that I want to use a big open dataset on AWS and do some analysis (using data science skills) while learning the AWS stuff. [GDELT, the Global Database of Events, Language and Tone](https://registry.opendata.aws/gdelt/) seems like a good choice because media and language are interesting to me.
