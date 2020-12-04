import sys
import re
input = sys.stdin.readlines()
valid = 0
for line in input:
    min, max, letter, _, password = re.split(r"[- (: )]", line)

    print(re.split(r"[- (: )]", line))
    print(f'min: {min}')
    print(f'max: {max}')
    print(f'letter: {letter}')
    print(f'password: {password}')

    count = password.count(letter)

    if count <= int(max) and count >= int(min):
        valid += 1

print(valid)
