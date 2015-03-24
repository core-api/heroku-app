from rest_framework.renderers import BaseRenderer
from coreapi import dump


class CoreAPIJSONRenderer(BaseRenderer):
    media_type = 'application/json'

    def render(self, data, media_type=None, renderer_context=None):
        return dump(data)
