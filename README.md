# sensor_regex

Regex (Regular Expression) patterns for parsing oceanographic, navigation, and meteorological sensor ASCII data messages.

To parse messages (data strings) received from sensors, the format of each message must first be described. Regex patterns for sensors used on oceanographic research vessels are catalogued here.

Note that for sensors that output multiple message types (like GNSS sensors), it is necessary to write the regex patterns in such a way that they only match a single message type.  

A summary of commonly-used regex metacharacters and sequences are provided below for quick reference.

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
\\*(?P\<checksum\>[0-9A-F]{2})	   | checksum	                                   | *9F
(?P\<name\>pattern)?	           | capture a named group as usual, but still works if the field is empty (e.g. $GPVTG,123.4,T,,M,0.00,N,0.00,K*4E)	 | None (if empty)
\W	                           |                                             | $

-----------------------------------------
