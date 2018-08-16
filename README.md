# gdelt-demo
Demonstration project--Learning to do interesting stuff with AWS and the GDELT dataset

This is an early-stage demo project to showcase my autodidactic process for learning about AWS and in particular how to ''do data science'' (whatever that ends up meaning to me) on AWS. The main goal is to demonstrate the value of my work to potential employers.

## Accomplished so far
I created a toy example where I query for all the unique ``actor1code`` values. To limit AWS charges for now, I ran it for only one date's worth of data which I manually copied to my S3 bucket. See ``scripts/first-demo-shorter.q``.

I have also just installed my own local Spark and am beginning to play around with it.

## Next steps
1. Learn more about Hive and about PySpark and integrate in here as helpful.
1.1. Install 
1. Automate pulling scripts from github to my S3 bucket.
1. Automate creating cluster with step[s] then terminating.
1. Something more analytical in my queries than just ``SELECT DISTINCT``.
1. Learn how to do this locally or in a smaller sandbox environment so not needed to use an AWS xlarge every time.
1. Build "something more analytical" into a full suite showing data science understanding.

## Background 
I have some data sciencey, big dataish skills from my PhD program; now I need a millieu to showcase and keep building them.

The premise is that I want to use a big open dataset on AWS and do some analysis (using data science skills) while learning the AWS stuff. [GDELT, the Global Database of Events, Language and Tone](https://registry.opendata.aws/gdelt/) seems like a good choice because media and language are interesting to me.

## Additional showcase items
[This is my first-authored paper](https://www.sciencedirect.com/science/article/pii/S0049089X16302368) using a million row dataset that we got published. About 90% of the analysis and 90% of the prose is mine, although the dataset was preexisting. I wrote this code in R and am working to get it up here.

[This was some exploratory work](https://dl.acm.org/citation.cfm?id=2909632) that died there because we couldn't find anything attention-grabbing to study, at least not in the initial investigations. Nevertheless it gave me a good chance to use numpy/pandas and to learn a little bit of QGIS.

My [neural-networks-and-deep-learning repo](https://github.com/reed9999/neural-networks-and-deep-learning) is probably also of interest. It's not intended to be a finished project, but it does show my curiosity in playing around with NN stuff to try to solve one of the ''mysteries'' about ML to my social-science-educated brain: Why can't we improve predictions with a little bit of a theoretical nudge? 

I also did a lot of qualitative research. I'm a big believer in mixed quant/qual methods.
