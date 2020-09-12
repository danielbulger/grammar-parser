from parser import Grammar, GrammarRule, LexerRule, BasicLexer
from parser.earley import EarleyParser

lexer_rules = LexerRule.make_from_file('lexer.rules')
lexer = BasicLexer(lexer_rules)

tokens = lexer.tokenize('2 + 3 * 4')

grammar_rules = GrammarRule.make_from_file("grammar.rules")
grammar = Grammar(grammar_rules)

parser = EarleyParser(grammar, lexer_rules)
parser.parse(tokens)
