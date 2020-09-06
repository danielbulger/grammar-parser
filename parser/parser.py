from abc import abstractmethod
from typing import List

from . import Token


class GrammarRule:

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

    def __init__(self, rules=List[GrammarRule]):
        self.rules = rules

    def __str__(self):
        return '\n'.join(self.rules)

    def __repr__(self):
        return repr(self.__str__())


class Parser:

    def __init__(self, grammar: Grammar):
        self.grammar = grammar

    @abstractmethod
    def parse(self, tokens: List[Token]):
        pass
