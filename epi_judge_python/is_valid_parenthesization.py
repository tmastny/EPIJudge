from test_framework import generic_test

CLOSED_2_OPENED = {
    "}": "{",
    "]": "[",
    ")": "("
}

def matches(opened, closed):
    return opened == CLOSED_2_OPENED[closed]

def is_well_formed(s: str) -> bool:
    stack = []
    for i in range(len(s)):
        if s[i] in "{([":
            stack.append(s[i])
        elif s[i] != ",":
            if stack and matches(stack[-1], s[i]):
                stack.pop()
            else:
                return False

    return len(stack) == 0


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_valid_parenthesization.py',
                                       'is_valid_parenthesization.tsv',
                                       is_well_formed))
