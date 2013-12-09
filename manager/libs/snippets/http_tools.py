"""
Http tools
"""

import httplib


def http_destination_exists(site, path):
    """
    """

    conn = httplib.HTTPConnection(site)
    conn.request('HEAD', path)
    response = conn.getresponse()
    conn.close()
    return response.status == 200
