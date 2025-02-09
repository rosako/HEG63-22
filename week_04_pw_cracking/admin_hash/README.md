# **Lab Manual: Cracking a Linux Admin Password**  

## **Introduction**  
Hardcoded credentials and weak password storage methods are common security flaws in embedded systems. In this lab, you will explore an **extracted file system** from a router, analyze how credentials are stored, and use **John the Ripper** to crack the **admin** password.  

By the end of this lab, you will:  
- Understand how Linux user authentication works.  
- Use **John the Ripper** to crack a password from a **hash stored in /etc/passwd**.  

---

## **Prerequisites**  
- A Linux machine (or a virtual machine) with:  
  - `John the Ripper` installed (`sudo apt install john` if not already done).  
- The **extracted file system**, provided to you.  

---

## **Lab Objectives**  
1. **Explore the extracted Linux file system.**  
2. **Locate the `etc/passwd` file and analyze its contents.**  
3. **Use John the Ripper to recover the admin password.**  
4. **Discuss the security implications of storing passwords in this way.**  

---

## **Step 1: Explore the Extracted File System**  
Navigate into the provided extracted file system:  
```bash
cd squashfs-root/
ls -la
```
🔹 **Question:** What directories do you recognize as part of a Linux system?  

List the contents of the `/etc/` directory:  
```bash
ls -la etc/
```
Locate the **passwd** file and display its contents:  
```bash
cat etc/passwd
```

---

## **Step 2: Analyzing the /etc/passwd File**  
The `/etc/passwd` file traditionally stores **user account information**, including usernames and password hashes. Each line follows this format:  
```
username:password_hash:UID:GID:Full Name:Home Directory:Shell
```
Here is the **content of the provided /etc/passwd** file:  
```
admin:$1$$iC.dUsGpxNNJGeOm1dFio/:0:0:root:/:/bin/sh
dropbear:x:500:500:dropbear:/var/dropbear:/bin/sh
nobody:*:0:0:nobody:/:/bin/sh
```
### **Analysis**  
- The **admin** user has a **hashed password**.  
- The **admin** user has UID `0`, meaning it has **root privileges**.  

---

## **Step 3: Recovering the Admin Password**  
Now, you will attempt to recover the admin password using **John the Ripper**.  

### **Tasks**  
- **Extract the password hash for the admin user.**  
-  **Use John the Ripper to recover the plaintext password.**  
-  **Write down the recovered password.**  

🔹 **Question:** How strong is this password? Would it be considered secure?

---

## **Ethical Considerations**  
🔹 **This lab is for educational purposes only.**  
🔹 **Never attempt to crack passwords on unauthorized systems.**  
🔹 **Always follow responsible disclosure if you find vulnerabilities.**  

---

