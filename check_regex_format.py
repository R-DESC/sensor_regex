"""
Check whether a string matches a given regex pattern.

Usage example:
  > check_regex_format.py \
      --format '^$GPGLL,(?P<latitude>\-?\d+\.\d+),(?P<lat_dir>[NS]),(?P<longitude>\-?\d+\.\d+),(?P<lon_dir>[EW])$' \
      --string '$GPGLL,2203.672,S,01759.539,W'

*** NOTE: Use single (not double) quotes on your strings,
otherwise any "$" character may be interpreted
as the start of a shell variable.

"""

import re
import argparse
import pprint


###############################################################################
def check_regex_format(format, string):
    """Check whether a regex pattern matches a string. If there is a
    complete match, return the match dictionary, otherwise return None.
    """

    mf = re.compile(format)
    out = mf.match(string)

    if out:
        return out.groupdict()
    else:
        return None


###############################################################################
if __name__ == '__main__':

    # parse the arguments
    parser = argparse.ArgumentParser()

    parser.add_argument('--format', dest='format', help='Regex pattern')
    parser.add_argument('--string', dest='string', help='String to match')
    args = parser.parse_args()

    # check the string against the regex format
    match_dict = check_regex_format(args.format, args.string)

    # return results
    if match_dict is None:
        print('String does not match regex format.')
    else:
        print('Matches: %s.<br/><br/>' % pprint.pformat(match_dict))
