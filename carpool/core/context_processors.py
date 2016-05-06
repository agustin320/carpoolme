import hashlib
import hmac
import logging
from django.conf import settings


def facebook_app(request):
    facebook_app_id = getattr(settings, 'FACEBOOK_APP_ID', False)

    response = {}

    if facebook_app_id:
        response['FACEBOOK_APP_ID'] = facebook_app_id

    return response


def segment_io(request):
    segment_id = getattr(settings, 'SEGMENT_ID', False)

    response = {}

    if segment_id:
        response['SEGMENT_ID'] = segment_id

    return response
