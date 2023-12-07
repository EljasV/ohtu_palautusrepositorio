from matchers import All, PlaysIn, HasAtLeast, And, HasFewerThan, Or


class QueryBuilder:
    def __init__(self, matcher = All()):
        self.matcher = matcher

    def plays_in(self, team: str):
        return QueryBuilder(And(self.matcher, PlaysIn(team)))

    def has_at_least(self, value, attr):
        return QueryBuilder(And(self.matcher, HasAtLeast(value, attr)))

    def has_fewer_than(self, value, attr):
        return QueryBuilder(And(self.matcher, HasFewerThan(value, attr)))

    def one_of(self, *matchers):
        return QueryBuilder(Or(*matchers))

    def build(self):
        return self.matcher
