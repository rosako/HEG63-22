# Web security


## Introduction

Web applications are a critical part of modern communication and business operations. However, they are often vulnerable to attacks due to poor coding practices, misconfigurations, or lack of security mechanisms. Understanding these vulnerabilities is essential for securing web applications.

In this lab, you will explore common web application vulnerabilities, including Command Injection, SQL Injection (SQLi), Cross-Site Scripting (XSS), and Cross-Site Request Forgery (CSRF). You will exploit these vulnerabilities in a controlled environment and observe their impact on the application.


## Understanding Web Application Vulnerabilities

### Command Injection:

- Occurs when an attacker can execute arbitrary commands on the server by injecting malicious input into a system command.

- Example: Injecting ; ls into a form field to list files on the server.

### SQL Injection (SQLi):

- Occurs when an attacker manipulates SQL queries by injecting malicious input.

- Example: Injecting ' OR '1'='1 into a login form to bypass authentication.

### Cross-Site Scripting (XSS):

- Occurs when an attacker injects malicious scripts into a web page viewed by other users.

- Example: Injecting <script>alert('XSS');</script> into a comment field.

### Cross-Site Request Forgery (CSRF):

- Occurs when an attacker tricks a user into performing an unwanted action on a web application where they are authenticated.

- Example: Forging a request to change a user’s password without their consent.



## Objective of the Lab

The goal of this lab is to demonstrate how insecure web applications can be exploited due to common vulnerabilities. You will:

- Identify vulnerabilities in the provided web application.

- Exploit these vulnerabilities to achieve specific objectives.

- Observe the impact of these exploits on the application.



## What we will exploit

In this lab, you will exploit the following vulnerabilities:

- Command Injection:
	- Exploit a vulnerable input field to execute arbitrary commands on the server.

- SQL Injection (SQLi):
	- Exploit a vulnerable login form to bypass authentication.

- Cross-Site Scripting (XSS):
	- Exploit a vulnerable comment field to execute malicious scripts in the browser.

- Cross-Site Request Forgery (CSRF):
	- Exploit a vulnerable password change form to perform unauthorized actions.




## Lab Tasks

### Task 1: Command Injection

- Objective: Exploit the command injection vulnerability to execute arbitrary commands on the server.

- Steps:
	- Navigate to the Ping page in the web application.
	- Enter a valid IP address (e.g., 127.0.0.1) and observe the output.
	- Inject a command to list files on the server.
	- Observe the results and document your findings.




### Task 2: SQL Injection (SQLi)
- Objective: Exploit the SQLi vulnerability to bypass authentication.

- Steps:
	- Navigate to the Login page in the web application.
	- Enter a valid username and password (e.g., admin:admin123).
	- Use SQLi payloads to bypass the login form.
	- Observe the results and document your findings.



### Task 3: Cross-Site Scripting (XSS)
- Objective: Exploit the XSS vulnerability to execute malicious JavaScript in the browser.

- Steps:
	- Navigate to the Comment page in the web application.
	- Enter a harmless comment and observe how it is displayed.
	- Inject a malicious script to display an alert box.
	- Observe the results and document your findings.


### Task 4: Cross-Site Request Forgery (CSRF)
- Objective: Exploit the CSRF vulnerability to change a user’s password without their consent.

- Steps:
	- Navigate to the Change Password page in the web application.
	- Create a malicious HTML form that submits a password change request.
	- Trick a victim into submitting the form (simulate this in the lab).
	- Observe the results and document your findings.



