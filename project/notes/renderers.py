from rest_framework.renderers import BaseRenderer
from coreapi.codecs import HTMLCodec, CoreJSONCodec, HALCodec


class CoreJSONRenderer(BaseRenderer):
    media_type = 'application/vnd.coreapi+json'

    def render(self, data, media_type=None, renderer_context=None):
        codec = CoreJSONCodec()
        return codec.dump(data, verbose=True)


class HALRenderer(BaseRenderer):
    media_type = 'application/hal+json'

    def render(self, data, media_type=None, renderer_context=None):
        codec = HALCodec()
        return codec.dump(data, verbose=True)


class CoreAPIHTMLRenderer(BaseRenderer):
    media_type = 'text/html'

    def render(self, data, media_type=None, renderer_context=None):
        codec = HTMLCodec()
        return codec.dump(data)
