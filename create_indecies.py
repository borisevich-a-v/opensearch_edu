from opensearchpy import OpenSearch, RequestError

TAGS_INDEX_NAME = "tags"
RATINGS_INDEX_NAME = "ratings"
MOVIES_INDEX_NAME = "movies"
GENOME_SCORE_NAME = "genome-scores"

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


@catch_error_and_log(GENOME_SCORE_NAME)
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
                "@version": {
                    "type": "text"
                },
                "movieId": {
                    "type": "integer"
                },
                "relevance": {
                    "type": "float"
                },
                "tagId": {
                    "type": "integer"
                },
                "tag_name": {
                    "type": "text",
                    "fields": {
                        "keyword": {
                            "type": "keyword",
                            "ignore_above": 256
                        }
                    }
                }
            }
        }
    }
    client.indices.create(index=index_name, body=index_body)


@catch_error_and_log(MOVIES_INDEX_NAME)
def create_movies_index(index_name):
    index_body = {
        'settings': {
            'index': {
                'number_of_shards': 1,
                "number_of_replicas": 1
            }
        },
        "mappings": {
            "properties": {
                "@version": {
                    "type": "text"
                },
                "genres": {
                    "type": "text",
                    "fields": {
                        "keyword": {
                            "type": "keyword",
                            "ignore_above": 256
                        }
                    }
                },
                "movieId": {
                    "type": "integer"
                },
                "title": {
                    "type": "text",
                    "fields": {
                        "keyword": {
                            "type": "keyword",
                            "ignore_above": 256
                        }
                    }
                },
                "imdbId": {
                    "type": "text"
                },
                "tmdbId": {
                    "type": "text"
                }
            }
        }
    }
    client.indices.create(index=index_name, body=index_body)


@catch_error_and_log(MOVIES_INDEX_NAME)
def create_genome_score_index(index_name):
    index_body = {
        'settings': {
            'index': {
                'number_of_shards': 1,
                "number_of_replicas": 1
            }
        },
        "mappings": {
            "properties": {
                "@version": {
                    "type": "text"
                },
                "genres": {
                    "type": "text",
                    "fields": {
                        "keyword": {
                            "type": "keyword",
                            "ignore_above": 256
                        }
                    }
                },
                "movieId": {
                    "type": "integer"
                },
                "title": {
                    "type": "text",
                    "fields": {
                        "keyword": {
                            "type": "keyword",
                            "ignore_above": 256
                        }
                    }
                },
                "imdbId": {
                    "type": "text"
                },
                "tmdbId": {
                    "type": "text"
                }
            }
        }
    }
    client.indices.create(index=index_name, body=index_body)


def main():
    create_tags_index()
    create_ratings_index()
    create_movies_index()
    create_genome_score_index()


if __name__ == "__main__":
    main()
