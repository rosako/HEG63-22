# Cryptography

## Introduction

Cryptography is the science of protecting information by transforming it into an unreadable format. However, early encryption methods often had weaknesses that made them easy to break. Two such methods are the Caesar cipher and the Substitution cipher. These ciphers rely on simple transformations of letters, making them vulnerable to cryptanalysis techniques like frequency analysis.

In this lab, you will explore how to break encrypted messages using these methods. You will first decode a Caesar cipher and then use Python to perform frequency analysis and crack a substitution cipher.



## Understanding the ciphers

- Caesar Cipher:
	- A substitution cipher that shifts letters in the alphabet by a fixed number.
	- Example: With a shift of 3, A becomes D, B becomes E, and so on.
	- Easy to break by trying all possible shifts (brute force) or analyzing patterns.

- Substitution Cipher:
	- Each letter in the plaintext is replaced with a unique letter from a shuffled alphabet.
	- More secure than Caesar but still breakable using frequency analysis.
	- English text has predictable letter frequencies (e.g., E, T, A are common).


## Objective of the lab

- The goal of this lab is to introduce students to cryptanalysis techniques by solving two cipher challenges:
	- Decode a message encrypted with the Caesar cipher using manual or brute-force techniques.
	- Crack a substitution cipher using Python and frequency analysis.

## What we will learn

- How the Caesar cipher works and how to decode it.
- Basics of letter frequency analysis for the English language.
- Using Python to analyze and decode a substitution cipher.


## Exercices

1. Decode a Caesar Cipher
	- You will receive a sentence encrypted with a Caesar cipher (e.g., Dwwdfn dw gdzq!).
	- Use either manual analysis or write a Python script to try all shifts (0-25) and decode the message.


2. Exercise 2: Break a Substitution Cipher
	- A short text encrypted with a substitution cipher will be provided in a text file (e.g., cipher_text.txt).
	- Use the provided Python script to:
		- Analyze the frequency of letters in the encrypted text.
		- Compare results with English letter frequencies.
		- Map the most frequent letters to their likely plaintext counterparts.
	- Complete the decryption manually using the insights from frequency analysis




## Further references

- https://pi.math.cornell.edu/~mec/2003-2004/cryptography/subs/frequencies.html











