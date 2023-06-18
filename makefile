.PHONY: prereq
prereq:
	@docker network create opensearch  || true

.PHONY: up-cluster
up-cluster: | prereq
	@docker compose up opensearch-node1 opensearch-node2 dashboards

.PHONY: logstash
logstash: | prereq
	@docker compose up logstash