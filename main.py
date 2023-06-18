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
