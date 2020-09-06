from abc import abstractmethod
from typing import List

from . import Token


class GrammarRule:

    @staticmethod
    def make_from_file(file_path) -> List:
        with open(file_path, 'r') as input_file:

            rules = []

            for line in input_file.readlines():

                parts = [x.strip() for x in line.split("->")]

                rules.append(GrammarRule(parts[0], parts[1].split(' ')))

            return rules

    def __init__(self, name: str, tokens: List[str]):
        self.name = name
        self.tokens = tokens

    def __contains__(self, item) -> bool:
        return item in self.tokens

    def __eq__(self, other) -> bool:
        return type(other) is GrammarRule and \
               self.name == other.name and \
               self.tokens == other.tokens

    def __getitem__(self, item) -> str:
        return self.tokens[item]

    def __len__(self) -> int:
        return len(self.tokens)

    def __repr__(self) -> str:
        return repr(self.__str__())

    def __str__(self) -> str:
        return f"{self.name} -> {' '.join(self.tokens)}"


class Grammar:

    def __init__(self, rules: List[GrammarRule]):
        self.rules = rules

    def __str__(self):
        return '\n'.join([str(rule) for rule in self.rules])

    def __repr__(self):
        return repr(self.__str__())


class Parser:

    def __init__(self, grammar: Grammar):
        self.grammar = grammar

    @abstractmethod
    def parse(self, tokens: List[Token]):
        pass
