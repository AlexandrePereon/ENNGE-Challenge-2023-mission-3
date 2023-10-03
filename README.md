# ENNGE-Challenge-2023-mission-3

## Description
First, construct a JSON string like below:

Go solution
```
{
  "github_url": "https://gist.github.com/YOUR_ACCOUNT/GIST_ID",
  "contact_email": "EMAIL",
  "solution_language": "golang"
}
```

Python solution
```
{
  "github_url": "https://gist.github.com/YOUR_ACCOUNT/GIST_ID",
  "contact_email": "EMAIL",
  "solution_language": "python"
}
```

Fill in your email address for EMAIL, and the path to your secret gist for YOUR_ACCOUNT/GIST_ID. In addition, solution_language should be filled with the solution language of your choice (golang or python). Be sure you have double-checked your email address; we will contact you by email.

Then, make an HTTP POST request to the following URL with the JSON string as the body part.

https://api.challenge.hennge.com/challenges/003
Content type
The Content-Type: of the request must be application/json.

### Authorization
The URL is protected by HTTP Basic Authentication, which is explained on Chapter 2 of RFC2617, so you have to provide an Authorization: header field in your POST request

For the userid of HTTP Basic Authentication, use the same email address you put in the JSON string.

For the password, provide a 10-digit time-based one time password conforming to RFC6238 TOTP.

### Authorization password
For generating the TOTP password, you will need to use the following setup:
- You have to read RFC6238 (and the errata too!) and get a correct one time password by yourself.
- TOTP's Time Step X is 30 seconds. T0 is 0.
- Use HMAC-SHA-512 for the hash function, instead of the default HMAC-SHA-1.
- Token shared secret is the userid followed by ASCII string value "HENNGECHALLENGE003" (not including double quotations).
  
Shared secret examples
- For example, if the userid is "ninja@example.com", the token shared secret is "ninja@example.comHENNGECHALLENGE003".
- For example, if the userid is "ninjasamuraisumotorishogun@example.com", the token shared secret is "ninjasamuraisumotorishogun@example.comHENNGECHALLENGE003"
- If your POST request succeeds, the server returns HTTP status code 200.

## Rules
You do not have to disclose how you achieved this mission at this time. Do not hesitate to use source codes or tools on the net, but do the exploring process by yourself of course, do not ask your friend to help you. The only thing that matters is that it works!
No bruteforce attacks, please!

### Sample Request
```
POST /challenges/003 HTTP/1.1
Authorization: Basic bmluamFAZXhhbXBsZS5jb206MTU5NTk0MjU2MA==
Host: api.challenge.hennge.com
Accept: */*
Content-Type: application/json
Content-Length: 133

{"github_url":"https://gist.github.com/hennge/b859bd12e7a7fb418141","contact_email":"ninja@example.com","solution_language":"golang"}
```

### Sample Response
```
HTTP/1.1 200 OK
Content-Type: application/json
Date: Wed, 26 Jun 2019 02:15:16 GMT
Transfer-Encoding: chunked

{"message":"Congratulations! You have achieved mission 3"}
```
