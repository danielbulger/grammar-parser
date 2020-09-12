from typing import List

from . import Parser, Token, GrammarRule


class EarleyItem:

    def __init__(self, rule: GrammarRule, dot: int, origin: int):
        self.rule = rule
        self.dot = dot
        self.origin = origin

    def is_complete(self):
        return self.dot == len(self.rule)

    def next(self) -> str:
        return self.rule[self.dot]

    def __eq__(self, other):
        return type(other) == EarleyItem and \
               other.rule == self.rule and \
               other.dot == self.dot and \
               other.origin == self.origin

    def __str__(self):
        return f'EarleyItem[rule=[{self.rule}], dot={self.dot}, origin={self.origin}]'

    def __repr__(self):
        return repr(str(self))


class EarleyParser(Parser):

    def parse(self, tokens: List[Token]):
        charts = [[] for _ in range(len(tokens) + 1)]

        start = self.grammar[0].symbol

        for index, rule in enumerate(self.grammar):
            if rule.symbol == start:
                charts[0].append(EarleyItem(rule, 0, 0))

        for k in range(len(tokens)):

            for item in charts[k]:

                if not item.is_complete():
                    if self.is_terminal(item.next()):
                        if item.dot < len(tokens):
                            self.scan(charts, item, k)
                    else:
                        self.predict(charts, item, k)
                else:
                    self.complete(charts, item, k)

        for item in charts[-1]:
            if item.is_complete() and item.origin == 0:
                print(item)
                return True
        raise Exception('Input was not accepted by this Grammar')

    def predict(self, charts: List[List[EarleyItem]], item: EarleyItem, position: int):

        for rule in self.grammar.rules:
            if item.next() == rule.symbol:

                new_item = EarleyItem(rule, 0, position)

                if new_item not in charts[position]:
                    charts[position].append(new_item)

    def complete(self, charts: List[List[EarleyItem]], item: EarleyItem, position: int):

        for old_item in charts[item.origin]:

            if not old_item.is_complete() and old_item.next() == item.rule.symbol:

                new_item = EarleyItem(old_item.rule, old_item.dot + 1, old_item.origin)

                if new_item not in charts[position]:
                    charts[position].append(new_item)

    def scan(self, charts: List[List[EarleyItem]], item: EarleyItem, position: int):
        charts[position + 1].append(EarleyItem(item.rule, item.dot + 1, item.origin))
