# Name    : 05CountVowels 
# Author  : John Merchant 
# Date    : 11 Jul 2016 
# Purpose : Exercise to count vowels in word 

word = str(input("Please enter a word: ")) 

count_vowel = 0 
for char in word: 

    if char == "a" or char == "e" or char == "i" or char == "o" or char == "u": 

        count_vowel = count_vowel + 1 

 

print("Number of vowels in",word,"=",count_vowel)   

vowels = ["a","e","i","o","u"] 

count_vowel = 0 

 
for char in word: 

    if char in vowels: 

        count_vowel = count_vowel + 1 

 

print("Number of vowels in",word,"=",count_vowel) 
