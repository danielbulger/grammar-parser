from parser import Grammar, LexerRule, BasicLexer
from parser.earley import EarleyParser

lexer = BasicLexer(LexerRule.make_from_file('lexer.rules'))
parser = EarleyParser(grammar=Grammar([]))
parser.parse(lexer.tokenize("This is a test string!"))
