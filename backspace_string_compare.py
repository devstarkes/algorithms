from itertools import zip_longest


class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        for s, t in zip_longest(self.get_is(S), self.get_is(T)):
            if s != t:
                return False

        return True

    def get_is(self, s):
        skip = 0
        for l in reversed(s):
            if l == '#':
                skip += 1
            elif skip:
                skip -= 1
            else:
                yield l
