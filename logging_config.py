from config import config
import logging

logging.basicConfig(
    filename=config['logging']['filename'],
    level=getattr(logging, config['logging']['level'].upper()),
    format=config.get('logging','format', raw=True), # raw=True permite la interpolation para poder usar el %
)

logger = logging.getLogger(__name__)