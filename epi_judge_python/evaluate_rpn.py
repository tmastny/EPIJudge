from test_framework import generic_test


def evaluate(expression: str) -> int:
    stack = []
    i = 0
    while i < len(expression):
        token = []
        while i < len(expression) and expression[i] != ",":
            token.append(expression[i])
            i += 1
        i += 1
        token = "".join(token)

        if token in "+-*/":
            arg2 = stack.pop()
            if token == "+":
                stack[-1] += arg2
            elif token == "-":
                stack[-1] -= arg2
            elif token == "*":
                stack[-1] *= arg2
            elif token == "/":
                stack[-1] //= arg2
        else:
            stack.append(int(token))

    return stack[-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('evaluate_rpn.py', 'evaluate_rpn.tsv',
                                       evaluate))
