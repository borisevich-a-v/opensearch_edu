docker run -it --rm --name logstash --net test opensearchproject/logstash-oss-with-opensearch-output-plugin:7.13.4 -e 'input { stdin { } } output {
   opensearch {
     hosts => ["https://opensearch-node1:9200"]
     index => "movies"
     user => "admin"
     password => "admin"
     ssl => true
     ssl_certificate_verification => false
   }
 }'