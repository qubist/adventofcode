import sys
import re
input = sys.stdin.readlines()
valid = 0
for line in input:
    pos1, pos2, letter, _, password = re.split(r"[- (: )]", line)

    print(re.split(r"[- (: )]", line))
    print(f'pos1: {pos1}')
    print(f'pos2: {pos2}')
    print(f'letter: {letter}')
    print(f'password: {password}')

    valid += (password[int(pos1)-1] == letter) ^ (password[int(pos2)-1] == letter)

print(valid)
