#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    vowels = 'аеёиоуыэюя'
    st = {i for i in input() if i in vowels}
    print(len(st))