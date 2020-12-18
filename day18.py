with open('day18.in') as f:
    lines = [line.rstrip() for line in f]

import re

import enum
import re


class TokenType(enum.Enum):
    T_NUM = 0
    T_PLUS = 1
    T_MINUS = 2
    T_MULT = 3
    T_DIV = 4
    T_LPAR = 5
    T_RPAR = 6
    T_END = 7


import operator

operations = {
    TokenType.T_PLUS: operator.add,
    TokenType.T_MINUS: operator.sub,
    TokenType.T_MULT: operator.mul,
    TokenType.T_DIV: operator.truediv
}

def compute(node):
    if node.token_type == TokenType.T_NUM:
        return node.value
    left_result = compute(node.children[0])
    right_result = compute(node.children[1])
    operation = operations[node.token_type]
    return operation(left_result, right_result)

class Node:
    def __init__(self, token_type, value=None):
        self.token_type = token_type
        self.value = value
        self.children = []


def lexical_analysis(s):
    mappings = {
        '*': TokenType.T_MULT,
        '-': TokenType.T_MINUS,
        '+': TokenType.T_PLUS,
        '/': TokenType.T_DIV,
        '(': TokenType.T_LPAR,
        ')': TokenType.T_RPAR}

    tokens = []
    for c in s:
        if c in mappings:
            token_type = mappings[c]
            token = Node(token_type, value=c)
        elif re.match(r'\d', c):
            token = Node(TokenType.T_NUM, value=int(c))
        else:
            raise Exception('Invalid token: {}'.format(c))
        tokens.append(token)
    tokens.append(Node(TokenType.T_END))
    return tokens


def match(tokens, token):
    if tokens[0].token_type == token:
        return tokens.pop(0)
    else:
        raise_syntax_error(tokens)


def parse_e(tokens):
    return parse_ea(tokens, parse_e2(tokens))


def parse_ea(tokens, left_node):
    if tokens[0].token_type in [TokenType.T_MULT, TokenType.T_DIV]:
        node = tokens.pop(0)
        node.children.append(left_node)
        next_node = parse_e(tokens)

        if next_node.token_type in [TokenType.T_MULT, TokenType.T_DIV]:
            next_left_node = next_node.children[0]
            node.children.append(next_left_node)
            next_node.children[0] = node
            return next_node

        node.children.append(next_node)
        return node
    elif tokens[0].token_type in [TokenType.T_RPAR, TokenType.T_END]:
        return left_node
    raise_syntax_error(tokens)


def parse_e2(tokens):
    return parse_e2a(tokens, parse_e3(tokens))


def parse_e2a(tokens, left_node):
    if tokens[0].token_type in [TokenType.T_PLUS, TokenType.T_MINUS]:
        node = tokens.pop(0)
        node.children.append(left_node)
        next_node = parse_e(tokens)

        if next_node.token_type in [TokenType.T_PLUS, TokenType.T_MINUS]:
            next_left_node = next_node.children[0]
            node.children.append(next_left_node)
            next_node.children[0] = node
            return next_node

        node.children.append(next_node)
        return node
    elif tokens[0].token_type in [TokenType.T_MULT, TokenType.T_DIV, TokenType.T_END, TokenType.T_RPAR]:
        return left_node
    raise_syntax_error(tokens)


def parse_e3(tokens):
    if tokens[0].token_type == TokenType.T_NUM:
        return tokens.pop(0)
    match(tokens, TokenType.T_LPAR)
    e_node = parse_e(tokens)
    match(tokens, TokenType.T_RPAR)
    return e_node


def raise_syntax_error(tokens):
    raise Exception('Invalid syntax on token {}'.format(tokens[0].token_type))


def parse(inputstring):
    tokens = lexical_analysis(inputstring)
    ast = parse_e(tokens)
    match(tokens, TokenType.T_END)
    return ast

def parseX(l, startIdx=0):
    print("entering parse with idx = {}", startIdx)
    currIdx = startIdx
    mode = ""

    if l[currIdx] == '(':
        r, i = parse(l, currIdx+1)
        result = r
        currIdx = i
    else:
        result = int(l[currIdx])
        currIdx += 1

    while currIdx < len(l):
        print("")
        print("current mode is ", mode)
        print("working on", l[currIdx], currIdx)
        if l[currIdx] == ')':
            print("exiting parse with ) = {}", currIdx)
            return result, currIdx+1
        elif l[currIdx] == "+" or l[currIdx] == "*":
            mode = l[currIdx]
            print("changing mode to ", mode, currIdx)
        else:
            if l[currIdx] == '(':
                r, i = parse(l, currIdx+1)
                curr = r
                currIdx = i - 1
            else:
                curr = int(l[currIdx])
            if mode == "+":
                print("add ", result, curr, result+curr)
                r, i = parse(l, currIdx+1)
                curr = r
                currIdx = i - 1
                result += curr
            elif mode == "*":
                print("mul ", result, curr, result*curr)
                result *= curr
            else:
                print(mode)
                assert False
        currIdx += 1

    return result, currIdx

s = 0
#((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2
for l in lines:
    l1 = l.replace(" ", "")
    r = re.findall(r'\d+|\(|\)|\*|\+', l1)
    #l2 = l1.replace("+", "X").replace("*", "+").replace("X", "*")
    #print(l2)
    parsed = parse(l1)
    print(parsed.value)
    x = compute(parsed)
    print(x)
    s+=x

print(s)