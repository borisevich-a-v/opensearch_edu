from opensearchpy import OpenSearch


def get_client():
    return OpenSearch(
        hosts=[{'host': 'localhost', 'port': 9200}],
        http_compress=True,
        http_auth=('admin', 'admin'),
        use_ssl=True,
        verify_certs=False,
        ssl_assert_hostname=False,
        ssl_show_warn=False,
    )
