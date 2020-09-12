# Grammar Parser

Python implementation of the [Earley Parser](https://en.wikipedia.org/wiki/Earley_parser).

Given the terminals:
* `SUM -> +`
* `MULTIPLY -> *`
* `NUMBER -> \d+`
* `WHITESPACE -> \s+` (skipped)

The production rules:
* `P -> S`
* `S -> S SUM M | M`
* `M -> M MULTIPLY NUMBER | NUMBER`

The parser will output the matched production rule
`M -> M MULTIPLY NUMBER`