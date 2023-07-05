This project allows you to set up opensearch cluster locally and 
add  [this dataset](https://grouplens.org/datasets/movielens/25m/) to the cluster


## How to run
1. Run cluster with `make up-cluster`

2. Create indeces with `create_indeces.py`

3. Run logstash for all `.conf` files in logsatsh_conf directory. Use this order: 
tags.conf -> ratings.conf -> movies.conf -> longs.conf -> genome-tags.conf -> genome-score.conf

   1. Change in docker-compose volumes target file
   2. run in console ```make logstash``` 

4. Denormalize dataset with `denormilize.py`
