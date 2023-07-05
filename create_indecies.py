from opensearchpy import OpenSearch, RequestError

TAGS_INDEX_NAME = "tags"
RATINGS_INDEX_NAME = "ratings"

client = OpenSearch(
    hosts=[{'host': 'localhost', 'port': 9200}],
    http_compress=True,
    http_auth=('admin', 'admin'),
    use_ssl=True,
    verify_certs=False,
    ssl_assert_hostname=False,
    ssl_show_warn=False,
)


def create_tags_index():
    name = TAGS_INDEX_NAME
    index_body = {
        'settings': {
            'index': {
                'number_of_shards': 1,
                "number_of_replicas": 1
            }
        },
        "mappings": {
            "properties": {
                "@timestamp": {
                    "type": "date"
                },
                "@version": {
                    "type": "integer"
                },
                "movieId": {
                    "type": "integer"
                },
                "tag": {
                    "type": "text",
                    "fields": {
                        "keyword": {
                            "type": "keyword",
                            "ignore_above": 256
                        }
                    }
                },
                "userId": {
                    "type": "integer"
                }
            }
        }
    }

    client.indices.create(index=name, body=index_body)


def create_ratings_index():
    name = RATINGS_INDEX_NAME
    index_body = {
        'settings': {
            'index': {
                'number_of_shards': 1,
                "number_of_replicas": 1
            }
        },
        "mappings": {
            "properties": {
                "@timestamp": {
                    "type": "date"
                },
                "@version": {
                    "type": "integer"
                },
                "movieId": {
                    "type": "integer"
                },
                "rating": {
                    "type": "half_float"
                },
                "userId": {
                    "type": "integer"
                }
            }
        }
    }
    client.indices.create(index=name, body=index_body)


def main():
    try:
        create_tags_index()
        print(f"Index `{TAGS_INDEX_NAME}` for tags.csv has been created")
    except RequestError:
        print(f"Index name `{TAGS_INDEX_NAME}` is already in use. So index wasn't created")
    try:
        create_ratings_index()
        print(f"Index `{RATINGS_INDEX_NAME}` for ratings.csv has been created")
    except RequestError:
        print(f"Index name `{RATINGS_INDEX_NAME}` is already in use. So index wasn't created")


if __name__ == "__main__":
    main()
