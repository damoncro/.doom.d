#!/usr/bin/env python3

with open('init.el', 'r') as f:
    lines = f.readlines()

with open('init.el', 'w') as f:
    for line in lines:
        if line.strip() != '(setq native-comp-deferred-compilation t)':
            f.write(line)
