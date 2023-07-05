This project allows you to set up opensearch cluster locally and 
add  [this dataset](https://grouplens.org/datasets/movielens/25m/) to the cluster

Difference indecies are in different stage of improvement for now. 
The `tags`, `ratings`, and `movies` are in the best condition to check

## How to run
1. Run cluster with `make up-cluster`

2. Create indecies with `create_indecies.py`

3. Run logstash for all `.conf` files in logsatsh_conf directory. Use this order: 
tags.conf -> ratings.conf -> movies.conf -> longs.conf -> genome-tags.conf -> 
genome-score.conf

   1. Change in docker-compose volumes path to a target file
   2. run in console ```make logstash``` 

4. Denormalize dataset with `denormilize.py`
