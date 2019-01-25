# Project Idea 
A dashboard to provide the reliability of Amazon reviews for customers to make buying decisions. As the user enter the product link, this dashboard will automatically show top 10 most reliable reviews and the least reliable reviews (based on the average helpfulness score, word count and the review history).

# Tech Stack

![pipeline](https://user-images.githubusercontent.com/11646036/51764047-f1730980-2088-11e9-9584-d076dcaf27bc.png)


# Data Source
Amazon review data: !http://jmcauley.ucsd.edu/data/amazon/
1. Review data (40 GB) 
2. Product metadata (10 GB)

![reviews_df](https://user-images.githubusercontent.com/11646036/51401319-4bab2200-1aff-11e9-8083-0c8741a102c3.png)
  

# Engineering Challenge
1. How to join different datasets, especially there're 50 datasets (1 GB/per data set) seperatedly within AWS S3.
2. How to join/query efficiently?

# Business Value
Customers can refer to the reliable reviews to make buying decisions.

# MVP
A web application that user can enter the product link or name. It will show some basic information (e.g. item name, price, rating etc) and the ranking about the top 10 most/least reliable reviews. 

# Stretch Goals
* Workflow automation: Schedulers like Airflow?
* Optimize the performance: Join different data sources, caching
