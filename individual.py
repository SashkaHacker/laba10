#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    a = {'b', 'k', 'n', 'o', 'q'}
    b = {'a', 'b', 'k', 'u'}
    c = {'o', 'p'}
    d = {'a', 'm', 'n', 'y', 'z'}
    u = set("abcdefghijklmnopqrstuvwxyz")
    x = (a | b) & c
    y = (u.difference(a)) & (u.difference(b)).difference(c | d)
    print(x)
    print(y)
