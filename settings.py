from pathlib import Path
from urllib.parse import urljoin

from prettyconf import config

PROJECT_DIR = Path(__file__).resolve().parent

COPERNICUS_BASE_URL = config(
    'COPERNICUS_BASE_URL',
    default='https://emergency.copernicus.eu/mapping/list-of-components/',
)
COPERNICUS_COMPONENT_ID = config('COPERNICUS_COMPONENT_ID')
COPERNICUS_COMPONENT_URL = urljoin(COPERNICUS_BASE_URL, COPERNICUS_COMPONENT_ID)

TARGET_MONITORING_ID = config('TARGET_MONITORING_ID', cast=int)
TARGET_MONITORING_DISPLAY = f'Monitoring {TARGET_MONITORING_ID}'
TARGET_MAP_ID = config('TARGET_MAP_ID', cast=int)
TARGET_MAP_DISPLAY = f'RTP Map #{TARGET_MAP_ID:02d}'
TARGET_STATUS = config('TARGET_STATUS', default='QUALITY APPROVED')

DOWNLOADS_DIR = PROJECT_DIR / config('DOWNLOADS_DIR', default='downloads')

NOTIFICATION_FROM_ADDR = config('NOTIFICATION_FROM_ADDR')
NOTIFICATION_TO_ADDRS = config('NOTIFICATION_TO_ADDRS', cast=config.list)
SMTP_SERVER = config('SMTP_SERVER')
SMTP_PORT = config('SMTP_PORT')
SMTP_USERNAME = config('SMTP_USERNAME')
SMTP_PASSWORD = config('SMTP_PASSWORD')
