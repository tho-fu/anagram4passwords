#!/usr/bin/env python3
# -*- coding: utf-8 -*-

version = "0.1"

__author__ = "ThoFu"
__copyright__ = "Copyright 2021, ThoFu"
__credits__ = "ThoFu"
__license__ = "GPLv2"
__version__ = version
__maintainer__ = "ThoFu"
__website__ = "https://github.com/tho-fu/anagram4passwords"

import os

print ("\nWelcome to the anagram4passwords tool written in Python!\n")
print ("This tool looks for frequently used passwords due to anagrams of your input")
print ("Multiple occurrences of the characters in the possible passwords are also output.\n")
print ("Version is : " + version + "\n")
print ("One moment please, the passwordlist is loading...", end=' ')

filename = "rockyou.txt" # Get it at https://github.com/danielmiessler/SecLists/blob/cb81804316c634728bbddb857ce7dfa5016e01b1/Passwords/Leaked-Databases/rockyou.txt.tar.gz

checkpath = os.path.isfile(filename)
checkread = os.access(filename, os.R_OK)
if checkpath is not False and checkread is not False:
	with open(filename, encoding = "ISO-8859-1") as fh:
		fstring = fh.readlines()
	fh.close()
else:
	print ("password file not found.")
	print ("Get it at https://github.com/danielmiessler/SecLists/blob/cb81804316c634728bbddb857ce7dfa5016e01b1/Passwords/Leaked-Databases/rockyou.txt.tar.gz")
	raise SystemExit()

print ("OK")

print ("\nPlease enter only chars, no spaces or tabs.")
userchars = input ("Enter your chars : ")

# Delete Spaces from Input
userchars = userchars.replace(" ","")

# Convert list to set to eleminate double chars and make a list again
usercharsset = list(set(userchars))

ilen = len(usercharsset)
resultchain = []
for res in fstring:
	rlen = len(res)
	varin = []
	for i in usercharsset:
		varin.append(res.count(i))
	result = rlen - sum(varin)
	if (result <= 0):
		resultchain.append(res)

print ("\n")

if (len(resultchain) >= 1):
	print ("Possible Passwords:\n")
	for x in resultchain:
		print(x)
	print ("\n")
else:
	print ("No results")