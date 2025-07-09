# Merchants-Guide-to-the-Galaxy-Problem

This is a classic code-challenging task based on the "Merchant's Guide to the Galaxy" problem. During a job interview for a position as a Python developer, the following question was posed to me. The Classic Merchant's Guide to the Galaxy was modified to incorporate a blend of natural language, the Roman numeral system, and price calculation.

I was successful in my application for the position, and it is possible that this project may serve as a source of inspiration for other individuals.



\## Traders' Translator



You are a medieval trader. 

This requires you to convert numbers and units. All trade is based on the roman numeral system although some traders seem to use terms of their local languages instead. You decide to write a program to help you (seems to be a parallel universe with computers in medieval times). 



\## Task



The program needs to learn values and translations from statements you are able to pick up. 

Then the program can answer questions about the prices of goods and the number system. 

The input to your program consists of lines of text detailing your notes on the conversion between units, roman numerals and prices of goods. 

This is directly followed by your questions. 



\### Input:



```

unu is I

kvin is V

dek is X

kvindek is L

unu unu Silver is 34 coins

unu kvin Gold is 57800 coins

dek dek Iron is 3910 coins

how much is dek kvindek unu unu ?

how many coins is unu kvin Silver ?

how many coins is unu kvin Gold ?

how many coins is unu kvin Iron ?

how much wood could a woodchuck chuck if a woodchuck could chuck wood ?

```



\### Expected output:



```

dek kvindek unu unu is 42

unu kvin Silver is 68 coins

unu kvin Gold is 57800 coins

unu kvin Iron is 782 coins

I have no idea what you are talking about

```



Of course, the program should be able to handle all questions that are formatted as above. The program is also expected to handle invalid queries appropriately.



\### Roman numerals



Roman numerals are based on the know values and rules (see http://en.wikipedia.org/wiki/Roman\_numerals): I, V, X, L, C, D, M. Numbers are formed by combining symbols together and adding the values. For example, MMVI is 1000 + 1000 + 5 + 1 = 2006. Generally, symbols are placed in order of value, starting with the largest values. When smaller values precede larger values, the smaller values are subtracted from the larger values, and the result is added to the total. For example MCMXLIV = 1000 + (1000 − 100) + (50 − 10) + (5 − 1) = 1944. The symbols "I", "X", "C", and "M" can be repeated three times in succession, but no more. (They may appear four times if the third and fourth are separated by a smaller value, such as XXXIX.). "D", "L", and "V" can never be repeated. "I" can be subtracted from "V" and "X" only. "X" can be subtracted from "L" and "C" only. "C" can be subtracted from "D" and "M" only. "V", "L", and "D" can never be subtracted. Only one small-value symbol may be subtracted from any large-value symbol.



