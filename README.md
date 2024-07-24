
# sensor_regex

Regex (Regular Expression) patterns for parsing oceanographic, navigation, and meteorological sensor ASCII data messages.

To parse messages (data strings) received from sensors, the format of each message must first be described. Regex patterns for sensors used on oceanographic research vessels are catalogued here.

Note that for sensors that output multiple message types (like GNSS sensors), it is necessary to write the regex patterns in such a way that they only match a single message type.  

A summary of commonly-used regex metacharacters and sequences are provided at the bottom of this document for quick reference.

-----------------------------------------

# files and scripts

---- ---- ---- ---- ----

1. sensor_regex_patterns.yaml

This yaml file contains regex patterns and sample data messages for a variety of oceanographic and meteorological sensors.
The contents are ordered alphabetically by manufacturer, then alphabetically by sensor model.

Example yaml section:

'SBE 38':
        NERC_L22_label: 'Sea-Bird SBE 38 thermometer'
        pseudonyms:
        manufacturers:
        - 'Sea-Bird Scientific'
        - 'Sea-Bird Electronics'
        message_samples:
        - '0.4168'
        message_regex_patterns:
        - '^\s*(?P<temperature>\-?\d+\.\d+)$'

Key:                         The sensor key (e.g. 'SBE 38') is the manufacturer's model name for the sensor.
                             The key may contain spaces. 
                             This key should be unique within the yaml file.
NERC_L22_label:              The standard identifier for the sensor model (or sensor class) as listed in the NERC Vocabulary Server L22 Seavox Device Catalogue
                             (https://vocab.nerc.ac.uk/collection/L22/current/). 
                             Please use the "preferred label" from L22 for this field.
pseudonyms:                  A list of other names that may be commonly used to reference this sensor model (if applicable).
manufacturers:               A list of manufacturer names attributed to this sensor model.
message samples:             A list of one or more example data messages output by the sensor. 
                             The data message format may differ depending on the sensor configuration. 
                             The sensor may output several different data message types.
                             For accuracy, the data message should be copied and pasted from the sensor output.
                             The syntax must match the sensor output exactly (for example, spaces must be represented accurately).
message_regex_patterns:      A list of one or more regex patterns for parsing the sensor data messages.

                             
Note: If a sensor outputs more than one message style, the regex patterns must be written such that they match with only the correct message.

Strings should be enclosed in single quotes ('this is an example string').
All fields are optional.
Indents must be spaces, not tabs, as per the yaml convention.


---- ---- ---- ---- ----

2. validate_sensor_regex_yaml.py

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


---- ---- ---- ---- ----

3. extract_sensor_regex.py

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

---- ---- ---- ---- ----

4. check_regex_format.py

Check whether a string matches a given regex pattern.

Usage example:
  > python check_regex_format.py \
      --format '^$GPGLL,(?P<latitude>\-?\d+\.\d+),(?P<lat_dir>[NS]),(?P<longitude>\-?\d+\.\d+),(?P<lon_dir>[EW])$' \
      --string '$GPGLL,2203.672,S,01759.539,W'

*** NOTE: Use single (not double) quotes on your strings,
otherwise any "$" character may be interpreted
as the start of a shell variable.

This is a utility script that is imported by validate_sensor_regex_yaml.py.

-----------------------------------------



## Common Regex Metacharacters

Regex  | Meaning                                 | Equivalent To
--- | --- | ---
\	     | escape prefix (special character)	     |
\\\	   | backslash	|
.	     | any single character except newline	   | [^\n]
\d	   | any digit	                             | [0-9]
\D	   | any non-digit	                         | [^0-9]
\w	   | any word character	                     | [a-zA-Z0-9_]
\W	   | any non-word character	                 | [^a-zA-Z0-9_]
\s	   | any whitespace character	               | [ \n\r\t\f]
\S	   | any non-whitespace character	           | [^ \n\r\t\f]
^	     | start of line (also means "not" if it is the first character in a range)	 |
$    	 | end of line	|
\*	   | zero or more times |	
?	     | zero or one times	|
\+	   | one or more times	|
{m}    | exactly m times	|
{m,n}	 | m to n times only (inclusive)	|
{m,}	 | m or more times	|
\|	   | or	|
!	     | not	|
(?P\<name\>pattern)	| capture a named group |	
(pattern)	          | group but do not capture |	

-----------------------------------------

## Useful Regex Combinations

Regex                          | Use Case                                    | Matches
--- | --- | ---
\d+	                           | positive integer	                           | 1987
\d+\.\d+	                     | positive float	                             | 1562.543789234
\-?\d+\.\d+	                   | float (positive or negative)	               | -89.321
\d+(\.\d+)?	                   | positive integer or float	                 | 543.00 and 543
[0-9T:\-]{19}Z	               | ISO datetime (UTC)	                         | 2021-11-09T16:52:23Z
(\d+\s+){5}\d+	               | set of space-delimited positive integers	   | 98 23  521 92 1
\*(?P<checksum>[0-9A-F]{2})	   | checksum	                                   | *9F
(?P<name>pattern)?	           | capture a named group as usual, but still works if the field is empty (e.g. $GPVTG,123.4,T,,M,0.00,N,0.00,K*4E)	 | None (if empty)
\W	                           |                                             | $

-----------------------------------------

## Tips

To match "$" in a sensor message string (such as in '$GPGGA') use \W rather than \$.  Dollar signs in regex strings can cause issues later (they are treated as special characters by some interpreters). Using \W avoids this headache.

-----------------------------------------




