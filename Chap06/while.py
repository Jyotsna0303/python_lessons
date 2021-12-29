#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

secret = 'swordfish'
pw = ''

# while pw != secret:
#     pw = input("What's the secret word? ")

#Controls  in loops continue, break, else

auth=False
count=0
max_attempt=5

while pw != secret:
    count +=1 #no ++ in python
    if count>max_attempt : break
    pw = input(f"{count}: What's the secret word?")
else:
    auth = True
# else with loop is new in python,
# This will only get executed when the while loops exits normally where condition gets false or all steps are exhauseted.
# othwerwise it is skipped.

print('Authorized' if auth else "Calling FBI....")