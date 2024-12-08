from .common import InfoExtractor

class KoofrIE(InfoExtractor):
    _VALID_URL = r'https://app\.koofr\.net/content/links/(?P<id>[a-f0-9\-]+)/files/get/(?P<filename>[^?]+)\?.*'
    _TEST = {
        'url': 'https://app.koofr.net/content/links/5931f831-302d-4d36-a1a5-d19bd72f3477/files/get/sdfjlke.mp4?path=sdfjlke.mp4',
        'only_matching': True,
    }

    def _real_extract(self, url):
        # Extract the necessary components from the URL
        mobj = self._match_valid_url(url)
        video_id = mobj.group('id')
        filename = mobj.group('filename')

        # Define the referrer based on the ID
        referrer_url = f'https://app.koofr.net/links/{video_id}'

        # Set custom headers for the request
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:133.0) Gecko/20100101 Firefox/133.0',
            'Referer': referrer_url,
        }

        # Fetch metadata (if needed, can fetch webpage here)
        video_title = filename.rsplit('.', 1)[0]  # Use filename as a title

        # Return the extracted information
        return {
            'id': video_id,
            'title': video_title,
            'url': url,
            'ext': 'mp4',
            'http_headers': headers,  # Pass the custom headers to the downloader
        }
