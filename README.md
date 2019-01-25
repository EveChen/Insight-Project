# Project Idea 
Amazon has over 130+ millions of reviews and ratings for customers to make their buying decisions. However, reading reviews, comparing rankings and ratings take time, especially when unreliable products flood the market place by fake reviews and ratings. Leveraging 50 GB customer buying records, I create **_a dashboard for Amazon users to check the reliability of a specific product, based on trustworthiness of reviews and ratings_**. 

# Tech Stack

![pipeline](https://user-images.githubusercontent.com/11646036/51764047-f1730980-2088-11e9-9584-d076dcaf27bc.png)


# Data Source
Amazon review data: !http://jmcauley.ucsd.edu/data/amazon/
1. Review data (40 GB) 
2. Product metadata (10 GB)

![reviews_df](https://user-images.githubusercontent.com/11646036/51401319-4bab2200-1aff-11e9-8083-0c8741a102c3.png)
  

# Engineering Challenge
1. How to join different datasets, especially there're 50 datasets seperated within AWS S3.
2. How to join/query efficiently?
3. How to adjust the reliable ratio in the real-time manner.

# Business Value
This dashboard updates the reliability of each product in a real-time manner, which prevents customers from chewing too many misleading product information/reviews and misplacing an unsatisfied order.

# MVP
A web application that user can enter the product link or name. It will show some basic information (e.g. item name, price etc) and the **_reliable ratio_** by calculating the overall ratings, reviews, rankings. 

![w2-demo2](https://user-images.githubusercontent.com/11646036/51765825-bde6ae00-208d-11e9-9c81-2c6c7dabd892.png)


# Stretch Goals
* Workflow automation: Schedulers like Airflow?
* Optimize the performance: Join different data sources, caching
