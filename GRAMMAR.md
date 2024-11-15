# Informal definition of grammar
## Lexemes
### identifiers
- 'address' of a cell, consisting of one column identifyer and one row identifyer such as `A3`
- name of a function: `SUM`

### operators
- plus `+`
- minus `-`
- multiply `*`
- divide `/`
- exponent `^`

### literals
- int: `42`
- float: `3.14159`
- string: `i am a string` → any cell containing text and not beginning with `=`

### delimiters
- brackets, indicating precedence of an operation `(a + b) * c`
- brackets, indicating the arguments passed to a function `SUM(A1:A5)`
- colon, indicating a range of cells: `A1:A5`