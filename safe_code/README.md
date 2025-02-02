# Lab Manual: HTTP Authentication Brute-Forcing with Burp Suite  

-> `http://webs.local`

---

## Introduction  
Web applications often rely on numeric codes for authentication. While convenient, these codes can be vulnerable to brute-force attacks if poorly implemented. In this lab, you will target a safe simulator protected by a 4-digit code. Your task is to bypass authentication using Burp Suite Community Edition while adhering to **ethical constraints** (simulated environment only).  

---

## Scenario Background  
The target system is a digital safe with the following characteristics:  
- Uses a **4-digit numeric code** for authentication  
- No account lockouts or rate limiting  
- The code was set by a citizen of Geneva, proud of his neighborhood! 

---

## Objective  
Gain unauthorized access to the safe by:  
1. Identifying the authentication endpoint  
2. Analyzing server responses  
3. Executing a **targeted brute-force attack**  
4. Recovering the secret message  

---

## Lab Setup Requirements  
1. **Target:** Safe simulator at `http://webs.local`  
2. **Tools:**  
   - Burp Suite Community Edition  
   - Web browser with proxy configuration  
3. **Knowledge:**  
   - Basic Burp Suite functionality (Proxy/Intruder)  
   - HTTP response interpretation  

---

## Hints for Success  

### 1. Endpoint Identification  
- Monitor network traffic during legitimate authentication attempts  
- Look for `POST` requests containing numeric parameters  

### 2. Response Analysis  
- Compare HTTP response bodies for valid/invalid attempts  
- Focus on JSON structure differences (`success` flag)  

### 3. Payload Construction  
- Consider creating a **custom numeric list**  
- Narrow down possibilities using historical context clues  
  > *"Sometimes the best codes are memorable numbers from significant eras"*  

---

## Key Investigation Areas  
1. How does the server differentiate valid/invalid codes?  
2. What makes numeric-only codes vulnerable?  
3. How can attack efficiency be improved without a pre-made wordlist?  

---

<!--- **Instructor Note** --->  
**Solution Pathway (Hidden from Students):**  
The working solution involves:  
1. Intercepting the `POST` request to `validate.php`  
2. Setting up Burp Intruder with:  
   - Attack type: **Sniper**  
   - Payload: Numeric range **1200-1299**  
   - Grep-match rule: `"success":true`  
3. Identifying the valid code from the unique `200 OK` response  
