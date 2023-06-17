from opensearchpy import OpenSearch



client = OpenSearch(
    hosts=[{'host': 'localhost', 'port': 9200}],
    http_compress=True,
    http_auth=('admin', 'admin'),
    use_ssl=True,
    verify_certs=False,
    ssl_assert_hostname=False,
    ssl_show_warn=False,
)

# response = client.index(
#         index="opensearch-logstash-docker-2023.06.14/3S8sXVBNSiWiz7pF4MtNRw",
#         body=document,
#         id=id,
#         refresh=True
#     )


q = 'kdaekasdas'
query = {
    'size': 5,
    'query': {
        'multi_match': {
            'query': q
        }
    }
}
response = client.search(
        body=query,
        index="movies"
    )
print(query)
print("-")
print(response)



# def _trash_bin():
#     # Add a document to the index.
#     document = {
#         'title': 'Moneyball',
#         'director': 'Bennett Miller',
#         'year': '2011'
#     }
#     id = '1'
#
#     response = client.index(
#         index=MOVIES,
#         body=document,
#         id=id,
#         refresh=True
#     )
#
#     print('\nAdding document:')
#     print(response)
#
#     # Search for the document.
#     q = 'miller'
#     query = {
#         'size': 5,
#         'query': {
#             'multi_match': {
#                 'query': q,
#                 'fields': ['title^2', 'director']
#             }
#         }
#     }
#
#     response = client.search(
#         body=query,
#         index=MOVIES
#     )
#     print('\nSearch results:')
#     print(response)
#
#     # Delete the document.
#     response = client.delete(
#         index=MOVIES,
#         id=id
#     )
#
#     print('\nDeleting document:')
#     print(response)
#
#     # Delete the index.
#     response = client.indices.delete(
#         index=MOVIES
#     )
#
#     print('\nDeleting index:')
#     print(response)
#
#
#
# def main():
#     # create_index()
#     ...
#
#
#
#
#
#
# main()