# Attacking local passwords

## Introduction

This lab demonstrates the risks of hardcoding passwords in programs and highlights the importance of protecting sensitive information. Students will analyze a vulnerable application, test multiple passwords, and discuss why secure password management is crucial in software development.


## Understanding Hardcoded Passwords

- How Hardcoded Passwords Work:


- Passwords are stored as plaintext within the source code or binary.
- During execution, the program compares the user-provided input against the hardcoded password.
- If the passwords match, access is granted; otherwise, access is denied.
- Why Hardcoding Passwords Is Not Secure:


## Objective of the Lab

- The goal of this lab is to demonstrate the risks of hardcoding passwords and the importance of secure password management. You will:
	- Analyze a C program with a hardcoded password.
	- Use a shell script to test multiple passwords against the program.
	- Extract the hardcoded password from the program using reverse engineering tools.
	- Discuss better ways to handle passwords in applications.

## What We Will Exploit

- In this lab, you will explore the following vulnerabilities:
	- Hardcoded Passwords: Passwords stored in the program can be easily extracted by attackers.
	- Predictable Behavior: The logic of password comparison can be exploited.
	- Lack of Secure Storage: The absence of mechanisms like hashed and salted passwords makes the program inherently insecure.
	- You will use these weaknesses to identify the correct password and gain access to the program.








