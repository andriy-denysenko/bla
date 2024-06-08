import configparser
from const import *
import configparser

from const import *


# Read or create configuration
def config_read():
    config = configparser.ConfigParser()

    if not os.path.exists('settings.ini'):
        config['DEFAULT'] = {
            'SOUND_BATTERY_LOW': os.path.join(SOUNDS_DIR, 'battery-low.wav'),
            'SOUND_BATTERY_HIGH': os.path.join(SOUNDS_DIR, 'battery-high.mp3'),
            'CHECK_INTERVAL': '3',
            'MIN_PERCENT': '15',
            'MAX_PERCENT': '95'
        }
        config_write(config)

    config.read(CONFIG_FILE_NAME)
    return config


def config_apply(conf):
    # Sound files
    global SOUND_BATTERY_LOW
    SOUND_BATTERY_LOW = conf['DEFAULT']['SOUND_BATTERY_LOW']

    global SOUND_BATTERY_HIGH
    SOUND_BATTERY_HIGH = conf['DEFAULT']['SOUND_BATTERY_HIGH']

    # Default check interval im minutes
    global CHECK_INTERVAL
    CHECK_INTERVAL = conf['DEFAULT']['CHECK_INTERVAL']

    # Default battery percents in percents
    global MIN_PERCENT
    MIN_PERCENT = conf['DEFAULT']['MIN_PERCENT']

    global MAX_PERCENT
    MAX_PERCENT = conf['DEFAULT']['MAX_PERCENT']


def config_write(conf):
    with open(CONFIG_FILE_NAME, 'w') as config_file:
        conf.write(config_file)


config = config_read()

# Sound files
SOUND_BATTERY_LOW = config['DEFAULT']['SOUND_BATTERY_LOW']
SOUND_BATTERY_HIGH = config['DEFAULT']['SOUND_BATTERY_HIGH']

# Default battery percents in percents
MIN_PERCENT = int(config['DEFAULT']['MIN_PERCENT'])
MAX_PERCENT = int(config['DEFAULT']['MAX_PERCENT'])

# Default check interval im minutes
CHECK_INTERVAL = int(config['DEFAULT']['CHECK_INTERVAL'])
