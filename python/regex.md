* Here I have listed some commonly used syntax for regex in Python. 
* The regular expression parser checks for each of these patterns in order (from left to right), takes the first one that matches, and ignores the rest.


Expression | Meaning | Comments
------------ | -------------
\ | escape special characters | instead of escaping characters, always use raw strings-r describer in the next row
r | nothing in this string should be escaped | '\t' is a tab character, but r'\t'is really the backslash character \ followed by the letter t. I recommend always using r (raw strings) when dealing with regular expressions
$ | end of the string, or line |
^ | beginning of the string, or line |
+ | one or more instances of the preceding item | Note that the + and * symbols are sometimes referred to as Kleene closures, or simply closures.
* | zero or more instances of the preceding item | Note that the + and * symbols are sometimes referred to as Kleene closures, or simply closures.
x?| matches an optional x character (in other words, it matches an x zero or one times) |
(a|b|c) | matches either a or b or c. |
\d | any numeric digit (0 through 9) |
\D |matches any character except a numeric digit|
\D+|matches one or more characters that are not digits|
x{n,m}|matches an x character at least n times, but not more than m times |M{n,m}. E.g.: M{0,4} = "0 to 4 occurences on M"
(x) | in general is a remembered group| You can get the value of what matched by using the groups() method of the object returned by re.search. Adding groups to a pattern lets you isolate parts of the matching text, expanding those capabilities to create a parser. Groups are defined by enclosing patterns in parentheses (( and )).
(?:pattern)|Defining a group containing a sub-pattern is also useful in cases where the string matching the sub-pattern is not part of what you want to extract from the full text| These groups are called non-capturing. non-capturing version of regular parentheses
[a-z]+|sequences of lower case letters|
[A-Z]+|sequences of upper case letters|
[a-zA-Z]+|sequences of lower or upper case letters|
[A-Z][a-z]+|one upper case letter followed by lower case letters|
\s|whitespace (tab, space, newline, etc.); [ \t\n\r\f\v]|
\S|non-whitespace|
\w|alphanumeric; [0-9a-zA-Z_]|
\W|non-alphanumeric|
\A|start of string|
\Z|end of string|
\b|empty string at the beginning or end of a word|a word boundary must occur right here
\B|empty string not at the beginning or end of a word|
[5b-d]|matches any chars '5', 'b', 'c' or 'd'|
[^a-c6]|matches any char except 'a', 'b', 'c' or '6'|
