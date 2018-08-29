# gdelt-demo
Demonstration project--Learning to do interesting stuff with AWS and the GDELT dataset

This is an early-stage demo project to showcase my autodidactic process for learning about AWS and in particular how to ''do data science'' (whatever that ends up meaning to me) on AWS. The main goal is to demonstrate the value of my work to potential employers.

## The entire showcase
This GDELT project is the latest one I'm building on here, but some of my previous work will also be of interest. See the respective README.md files for more: 


* **[Thumbs up for Privacy?](https://github.com/reed9999/thumbs-up-for-privacy)** (R, regressions) [This is my first-authored paper](https://www.sciencedirect.com/science/article/pii/S0049089X16302368) using a million row dataset. This work was published as "Thumbs Up for Privacy?" in _Social Science Research_, by Reed, Spiro, and Butts. About 90% of the analysis, the prose, and the R code are my original work. 

* **[Neural Networks and Deep Learning](https://github.com/reed9999/neural-networks-and-deep-learning)** (exploratory, Python, neural networks) I hacked around on Nielsen's eBook code. It shows my curiosity about one of the ''mysteries'' about ML to my social-science-educated brain: Why can't we improve predictions with a little bit of a theoretical nudge?

* **[EconGraphs](https://github.com/reed9999/econgraphs)** (Matplotlib, Django, Python) Plots arbitrary functions to. Intent is to make it easier for me to understand econ papers. Not very developed and probably has security holes, but a worthwhile Django/Matplotlib demo.

Rest of my github forked repos aren't showcasing anything yet, but stuff I want to hack around with.

* **Observing gender dynamics and disparities with mobile phone metadata** (highly exploratory, numpy/pandas, QGIS, billion-row dataset) No github repo.  [This was some exploratory work](https://dl.acm.org/citation.cfm?id=2909632) that died there because we couldn't find anything attention-grabbing to study. Although my colleague did most of the hardcore big-data it gave me a good chance to use numpy/pandas and to learn a little bit of QGIS.

I also did a good bit of qualitative research for my dissertation. I'm a big believer in mixed quant/qual methods.

## Currently troubleshooting
1. I don't understand why some of my Hive QL scripts fail, and the line numbers in the error output are opaque to me. At the moment demo-004 and demo-005-part2b work. The original demo-005 failed because I had meant to separate out what's now load-gdelt-events.q, but I hadn't deleted the part I wanted to extract out of there into part2. I don't know why 005-part2 is failing. 

1. I need Hive on my computer. Runnincg EMR jobs every time I want to troubleshoot QL is fun for a while, but plainly ridiculous for a development environment. I've mostly got it, but apparently I skipped a few steps in the Hadoop installation tutorial or something.



## Accomplished so far
I created a toy example where I query for all the unique ``actor1code`` values. To limit AWS charges for now, I ran it for only one date's worth of data which I manually copied to my S3 bucket. See ``scripts/first-demo-shorter.q``.

I have also just installed my own local Spark, HDFS, and Hive, and am beginning to play around with them.

## Next steps
1. Troubleshooting above.
1. Finish installation of Hive on my local computer for easier QL debugging.
1. Learn more about Hive and about PySpark and integrate in here as helpful.
    1. Confirm or finish my install of Spark and PySpark
1. Automate pulling scripts from github to my S3 bucket.
1. Automate creating cluster with step[s] then terminating.
1. Something more analytical in my queries than just ``SELECT DISTINCT``.
1. Learn how to do this locally or in a smaller sandbox environment so not needed to use an AWS xlarge every time.
1. Build "something more analytical" into a full suite showing data science understanding.

## Background
I have some data sciencey, big dataish skills from my PhD program; now I need a millieu to showcase and keep building them.

The premise is that I want to use a big open dataset on AWS and do some analysis (using data science skills) while learning the AWS stuff. [GDELT, the Global Database of Events, Language and Tone](https://registry.opendata.aws/gdelt/) seems like a good choice because media and language are interesting to me.

