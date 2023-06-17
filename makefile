export logstashconf="movies.conf"

.PHONY: prereq
prereq:
	@docker network create opensearch  || true

.PHONY: up-cluster
up-cluster: | prereq
	@docker compose -p opensearch up node1 node2 dashboards

.PHONY: logstash
logstash: | prereq
	@docker compose -p opensearch  up logstash