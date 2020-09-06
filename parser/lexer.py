import re
from abc import abstractmethod
from typing import Tuple, List


class Token:

    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __str__(self):
        return f'{self.name}={self.value}'

    def __repr__(self):
        return repr(self.__str__())


class LexerRule:

    @staticmethod
    def make_from_file(file_path):

        with open(file_path, 'r') as input_file:

            rules = []

            pattern = re.compile('([\\w_-]+)\\s*([:=])\\s*(.*?(?=(-> skip)|$))')

            for line in input_file.readlines():

                match = pattern.match(line.strip())

                if not match:
                    raise Exception(f'Unable to parse lexer rule due to {line}')

                groups = match.groups()

                rule = groups[2].strip()

                if groups[1] == '=':
                    rule = re.escape(rule)

                rules.append(LexerRule(
                    groups[0], rule, groups[3] is not None
                ))

            return rules

    def __init__(self, name: str, pattern: str, skip: bool = False):
        self.name = name
        self.pattern = re.compile(pattern)
        self.skip = skip

    def match(self, string):
        return self.pattern.match(string)

    def __str__(self):
        return f'{self.name} -> {self.pattern.pattern}/{"skip" if self.skip else ""}'

    def __repr__(self):
        return self.__str__()


class Lexer:

    def __init__(self, rules: List[LexerRule]):
        self.rules = rules

    def tokenize(self, string: str) -> List[Token]:
        tokens = []

        while string:
            [rule, value] = self.next_token(string)

            if not rule.skip:
                tokens.append(Token(rule.name, value))

            string = string[len(value):]

        return tokens

    @abstractmethod
    def next_token(self, string: str) -> Tuple[LexerRule, Token]:
        pass


class BasicLexer(Lexer):

    def next_token(self, string: str) -> Tuple[LexerRule, str]:
        for rule in self.rules:

            match_token = rule.match(string)

            if match_token is not None:
                return rule, match_token.group(0)

        raise Exception(f'Unknown token for {string}')
