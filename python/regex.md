Expression | Meaning | Comments
------------ | ------------- | --------------------
\ | escape special characters | instead of escaping characters, always use raw strings-r describer in the next row
r | nothing in this string should be escaped | '\t' is a tab character, but r'\t'is really the backslash character \ followed by the letter t. I recommend always using r (raw strings) when dealing with regular expressions
$ | end of the string, or line
