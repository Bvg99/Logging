import requests
import logging

logging.basicConfig(level=logging.INFO)
success_logger = logging.getLogger('success_responses')
success_handler = logging.FileHandler('success_responses.log')
success_logger.addHandler(success_handler)

bad_logger = logging.getLogger('bad_responses')
bad_handler = logging.FileHandler('bad_responses.log')
bad_logger.addHandler(bad_handler)

blocked_logger = logging.getLogger('blocked_responses')
blocked_handler = logging.FileHandler('blocked_responses.log')
blocked_logger.addHandler(blocked_handler)

websites = [
    'https://www.youtube.com/',
    'https://wikipedia.org',
    'https://yahoo.com',
    'https://yandex.ru',
    'https://whatsapp.com',
    'https://amazon.com',
    'https://www.ozon.ru',
    'https://instagram.com',
    'https://twitter.com'
]

for site in websites:
    try:
        response = requests.get(site)
        if response.status_code == 200:
            success_logger.info(f"INFO: '{site}', response - {response.status_code}")
        else:
            bad_logger.warning(f"WARNING: '{site}', response - {response.status_code}")
    except:
        blocked_logger.error(f"ERROR: '{site}', NO CONNECTION")

success_handler.close()
bad_handler.close()
blocked_handler.close()