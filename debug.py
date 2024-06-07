import math
from datetime import timedelta
import psutil


def print_debug_message(percent, prev_percent, secs_left, is_plugged):
    # Make a string for battery percent
    percent_str = f'{math.floor(percent)}% battery'

    # Make a string for seconds left
    secs_left_str = str(secs_left)
    if secs_left == psutil.POWER_TIME_UNKNOWN:
        time_left_str = 'unknown'
    elif secs_left == psutil.POWER_TIME_UNLIMITED:
        time_left_str = 'unlimited'
    else:
        time_left_str = str(timedelta(seconds=secs_left))

    # Try to detect if the device charges or the AC power cable is connected
    if percent > prev_percent or is_plugged:
        is_charging = True
    else:
        is_charging = False

    # Make strings for a test message
    is_charging_str = f'The device is {"not " if not is_charging else ""}charging'
    power_plugged_str = f'and is {"not " if not is_plugged else ""}plugged'

    # Make a test message
    test_msg = f'''-------------
BATTERY INFO:
Percent: {percent}, time left: {time_left_str}
{is_charging_str} {power_plugged_str}

percent: {percent}
prev_percent: {prev_percent}
secs_left: {secs_left}
power_plugged: {is_plugged}
'''

    print(test_msg)