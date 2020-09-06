from parser import Grammar, GrammarRule, LexerRule, BasicLexer
from parser.earley import EarleyParser

lexer = BasicLexer(LexerRule.make_from_file('lexer.rules'))
grammar = Grammar(GrammarRule.make_from_file("grammar.rules"))
parser = EarleyParser(grammar)
parser.parse(lexer.tokenize('This is a test string"'))
