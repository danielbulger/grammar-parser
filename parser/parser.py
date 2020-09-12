from abc import abstractmethod
from typing import List

from . import Token, LexerRule


class GrammarRule:

    @staticmethod
    def make_from_file(file_path) -> List:
        with open(file_path, 'r') as input_file:

            rules = []

            for line in input_file.readlines():

                parts = [x.strip() for x in line.split("->") if len(x) > 0]

                if len(parts) < 2:
                    raise Exception(f'Unable to parse grammar rules due to {line}')

                for rule in parts[1].split('|'):
                    rules.append(GrammarRule(parts[0], rule.strip().split(' ')))

            return rules

    def __init__(self, symbol: str, tokens: List[str]):
        self.symbol = symbol
        self.tokens = tokens

    def __contains__(self, item: str) -> bool:
        return item in self.tokens

    def __eq__(self, other) -> bool:
        return type(other) is GrammarRule and \
               self.symbol == other.symbol and \
               self.tokens == other.tokens

    def __getitem__(self, item) -> str:
        return self.tokens[item]

    def __len__(self) -> int:
        return len(self.tokens)

    def __repr__(self) -> str:
        return repr(str(self))

    def __str__(self) -> str:
        return f"{self.symbol} -> {' '.join(self.tokens)}"


class Grammar:

    def __init__(self, rules: List[GrammarRule]):
        self.rules = rules

    def add(self, rule: GrammarRule):
        self.rules.append(rule)

    def __getitem__(self, item) -> GrammarRule:
        return self.rules[item]

    def __contains__(self, item) -> bool:
        return item in self.rules

    def __str__(self):
        return '\n'.join([str(x) for x in self.rules])


class Parser:

    def __init__(self, grammar: Grammar, terminals: List[LexerRule]):
        self.grammar = grammar
        self.terminals = terminals

    @abstractmethod
    def parse(self, tokens: List[Token]):
        pass

    def is_terminal(self, symbol: str) -> bool:
        for terminal in self.terminals:
            if terminal.name == symbol:
                return True
        return False
