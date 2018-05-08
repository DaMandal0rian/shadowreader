
def _transform_uri(uri: str, base_url: str) -> str:
    url = f'{base_url}{uri}'
    return url


def _transform_load(load: list, base_url: str) -> list:
    if 'request_uri' in load[0]:
        uri_key = 'request_uri'
    elif 'uri' in load[0]:
        uri_key = 'uri'

    for l in load:
        l['url'] = _transform_uri(l[uri_key], base_url)
    return load


def main(**kwargs) -> list:
    load = kwargs.get('load', [])
    base_url = kwargs.get('base_url', '')
    if not base_url:
        raise ValueError(f'Base URL was not set! {base_url}')

    # If base_url ends with a "/", remove it
    if base_url.endswith('/'):
        base_url = base_url[:-1]

    # If base_url does not specify http or https, prefix it with http://
    if not (base_url.startswith('http://') or base_url.startswith('https://')):
        base_url = f'http://{base_url}'

    if load:
        load = _transform_load(load, base_url)

    return load
