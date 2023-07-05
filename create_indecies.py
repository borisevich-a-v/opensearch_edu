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


def catch_error_and_log(index_name):
    def decorator(create_index):
        def wrapper():
            try:
                create_index(index_name)
                print(f"Index `{index_name}` has been created")
            except RequestError:
                print(f"Index name `{index_name}` is already in use. So index wasn't created")
        return wrapper
    return decorator


@catch_error_and_log(TAGS_INDEX_NAME)
def create_tags_index(index_name):
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

    client.indices.create(index=index_name, body=index_body)


@catch_error_and_log(RATINGS_INDEX_NAME)
def create_ratings_index(index_name):
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
    client.indices.create(index=index_name, body=index_body)


def main():
    create_tags_index()
    create_ratings_index()


if __name__ == "__main__":
    main()
