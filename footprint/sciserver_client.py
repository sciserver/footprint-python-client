from footprint.api_client import ApiClient
from cookies import Cookies, Cookie

class SciServerClient(ApiClient):
    """SciServer wrapper around auto-generated API client
    
    Supports SciServer token authentication and session cookies
    """

    def __init__(self, authentication=None, configuration=None):

        super(SciServerClient, self).__init__(configuration=configuration)

        self.user_agent = 'SciServer Footprint Service Client/1.0.0/python'
        self.authentication = authentication
        self.cookies = Cookies()

    def request(self, method, url, query_params=None, headers=None,
                post_params=None, body=None, _preload_content=True,
                _request_timeout=None):

        if self.authentication is not None:
            if headers is None:
                headers = {}
            headers['X-Auth-Token'] = authentication.getToken()

        if self.cookies is not None and len(self.cookies) > 0:
            headers['Cookie'] = self.cookies.render_request()

        response = super(SciServerClient, self).request(
            method, url, query_params, headers,
            post_params, body, _preload_content,
            _request_timeout)

        if 'Set-Cookie' in response.urllib3_response.headers:
            cookies = Cookies.from_response(response.urllib3_response.headers['Set-Cookie'])
            for key in cookies:
                self.cookies.add(cookies[key])
            
        return response

        