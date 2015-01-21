from .models import RequestLog


class RequestLoggingMiddleware(object):
    """
    Logs requests that return a 200 HTTP status code and belong to a logged in
    user.
    """
    def process_response(self, request, response):
        if response.status_code == 200 and hasattr(request, 'user') and \
           request.user and not request.user.is_anonymous():
            RequestLog.objects.create_log(request)
        return response
