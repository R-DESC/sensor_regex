"""
Extract the regex patterns for a specific sensor
from the sensor_regex_patterns yaml file.

Usage examples:
  > python extract_sensor_regex.py --sensor '4300'
  > python extract_sensor_regex.py --sensor 'WindMaster Pro'
  > python extract_sensor_regex.py

where the 'sensor' argument is a sensor model name that corresponds
to a 'sensor' entry in the yaml file.

If the sensor model is not found in the file (or no model is provided),
this script will output a list of all available models.

Requires:
    pyyaml (pip install pyyaml)
"""

import yaml
import argparse


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

    # parse the arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--sensor', dest='sensor', help='Sensor model to extract')
    args = parser.parse_args()

    # load the yaml file
    sensor_regex_file = "sensor_regex_patterns.yaml"
    sensor_regex_dict = load_yaml(sensor_regex_file)

    # extract the list of sensor models from the yaml file
    sensors = sensor_regex_dict['sensors'].keys()

    if args.sensor in sensors:

        # load the information about the requested sensor
        sensor_dict = sensor_regex_dict['sensors'][args.sensor]

        # extract the regex pattern(s)
        sensor_regex_patterns = sensor_dict['message_regex_patterns']
        for pattern in sensor_regex_patterns:
            print(pattern)

    else:
        # Return a list of available sensors if the sensor is not found
        print(' *** WARNING *** ')
        print('Sensor model not extracted.')
        print('Available sensor models include:')
        print(sorted(list(sensors)))
