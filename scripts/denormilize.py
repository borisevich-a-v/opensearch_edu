from typing import NamedTuple

from scripts.client import get_client

client = get_client()


class Tag(NamedTuple):
    tag_id: int
    tag: str


def get_genome_tags():
    """Just pull tags from elasticsearch"""
    tag_amount = 1200
    query = {
        'size': tag_amount,
        'query': {"match_all": {}}
    }
    response = client.search(
        body=query,
        index="genome-tags"
    )
    tags = response["hits"]["hits"]
    return [Tag(tag['_source']["tagId"], tag['_source']["tag"]) for tag in tags]


def update_genome_score_by_tag(tag: Tag):
    query = {
        "query": {
            "match": {
                "tagId": tag.tag_id
            }
        },
        "script": {
            "source": f"ctx._source.tag_name = params.tag",
            "params": {
                "tag": tag.tag
            }
        }
    }

    response = client.update_by_query(index="genome-score", body=query)
    if response['updated'] > 0:
        print("Documents updated successfully.")
    else:
        print("No documents matched the query.")


def main():
    tags = get_genome_tags()
    updated_tags = []
    for tag in tags:
        print(f"Updating tag {tag.tag_id}:{tag.tag}")
        update_genome_score_by_tag(tag)
        updated_tags.append(tag)
    print(len(updated_tags), "was updated")


main()
