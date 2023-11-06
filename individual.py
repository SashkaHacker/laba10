#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    a = {'b', 'k', 'n', 'o', 'q'}
    b = {'a', 'b', 'k', 'u'}
    c = {'o', 'p'}
    d = {'a', 'm', 'n', 'y', 'z'}
    u = a | b | c | d
    x = (a | b) & c
    print(x)
    yy = (u.difference(a)) & (u.difference(b))
    y = yy.difference(c | d)
    print(x)
    print(y)