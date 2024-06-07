def get_utc_now() -> str:
    return f'{datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3]}Z'

def handle_proxy(url, params):
    try:
        internal = GsSession.current.is_internal()
    except MqUninitialisedError:
        internal = False
    if internal or socket.getfqdn().split('.')[-2:] == ['gs', 'com']:
        try:
            import gs_quant_auth
            proxies = gs_quant_auth.__proxies__
            response = requests.get(url, params=params, proxies=proxies)
        except ModuleNotFoundError:
            raise RuntimeError('You must install gs_quant_auth to be able to use this endpoint')
    else:
        response = requests.get(url, params=params)
    return response

