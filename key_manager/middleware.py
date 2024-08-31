from datetime import datetime, timedelta
from django.utils import timezone
from django.contrib.auth import logout


class SessionTimeoutMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            last_activity = request.session.get('last_activity')
            if last_activity:
                last_activity = datetime.fromisoformat(last_activity)
                now = timezone.now()
                timeout = timedelta(minutes=15)
                if now - last_activity > timeout:
                    logout(request)
                    request.session.flush()
            request.session['last_activity'] = timezone.now().isoformat()
        response = self.get_response(request)
        return response
