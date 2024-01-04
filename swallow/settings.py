from argparse import ArgumentParser, Namespace


def get_settings() -> Namespace:
    """
    Settings of kc_auto script.
    """
    parser = ArgumentParser()
    parser.add_argument("dirname")
    parser.add_argument("redis_url")
    # parser.add_argument("--queue", dest='queue', required=True)

    return parser.parse_args()
