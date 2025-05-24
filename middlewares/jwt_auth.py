import jwt
from django.conf import settings
from django.http import JsonResponse
from users.services.user_service import UserService

EXEMPT_URLS = [
    '/api/users/auth/login/',
    '/api/users/auth/forgot/',
    '/api/public/',  # Ejemplo
]

class JWTAuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Saltar validación si la URL está exenta
        if any(request.path.startswith(url) for url in EXEMPT_URLS):
            return self.get_response(request)

        auth_header = request.headers.get('Authorization')
        if auth_header and auth_header.startswith('Bearer '):
            token = auth_header.split(' ')[1]
            try:
                payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
                user = UserService.get_user_from_token(payload)
                request.custom_user = user  # Puedes guardar el payload completo o parte
            except jwt.ExpiredSignatureError:
                return JsonResponse({'detail': 'Expired token'}, status=401)
            except jwt.InvalidTokenError:
                return JsonResponse({'detail': 'Invalid token'}, status=401)
        else:
            return JsonResponse({'detail': 'Invalid auth'}, status=401)

        return self.get_response(request)
