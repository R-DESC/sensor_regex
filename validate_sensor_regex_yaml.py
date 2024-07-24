"""
This script may be used to verify
the contents of the sensor_regex_patterns.yaml file.

It is recommended that this script be run
whenever edits are made to the yaml file.

Features:
- Confirms that the sensor_regex_patterns yaml file can be loaded.
- Validates the regex patterns against the sample data messages.
- Outputs the list of sensor models in the file with their validation status.

Usage:
  > python validate_sensor_regex_yaml.py

Requires:
    pyyaml (pip install pyyaml)
"""

import yaml
import check_regex_format as crf


def load_yaml(file):
    """ Opens a yaml file and returns a dict."""

    with open(file, 'r') as stream:
        try:
            data_dict = yaml.safe_load(stream)
        except Exception as e:
            print("Unable to load yaml file.")
            print(e)

    return data_dict


###############################################################################
if __name__ == '__main__':

    sensor_regex_file = "sensor_regex_patterns.yaml"

    sensor_regex_dict = load_yaml(sensor_regex_file)

    # loop over every sensor in the file
    for sensor in sensor_regex_dict['sensors'].keys():

        # output the sensor model name
        print(sensor)

        # extract the regex patterns for that sensor
        sensor_regex_patterns = sensor_regex_dict['sensors'][sensor]['message_regex_patterns']

        # extract the sample messages for that sensor
        message_samples = sensor_regex_dict['sensors'][sensor]['message_samples']

        # check the regex patterns against the sample messages
        if sensor_regex_patterns:
            if message_samples:
                for scount, sample in enumerate(message_samples):
                    hasmatch = False
                    for pcount, pattern in enumerate(sensor_regex_patterns):
                        match = crf.check_regex_format(pattern, sample)
                        if match:
                            hasmatch = True
                            print(' * Matches')
                            # print(' * Sample ' + str(scount) + ' matches pattern ' + str(pcount) + '.')
                            # print(match)
                    if not hasmatch:
                        print('   *** WARNING!!! Sample does not match any regex patterns.')
                        print('   *** ' + sample)
            else:
                print('   *** WARNING!!! Message samples array is empty.')
        else:
            print('   *** WARNING!!! Regex patterns array is empty.')
