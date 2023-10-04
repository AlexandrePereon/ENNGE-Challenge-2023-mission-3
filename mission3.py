import json
import requests
import base64
import pyotp

email = "yourmail@gmail.com"
github_url = "https://gist.github.com/YOUR_ACCOUNT/GIST_ID"
solution_language = "python"

secret = email + "HENNGECHALLENGE003"
secret_base32 = base64.b32encode(secret.encode())

totp = pyotp.TOTP(secret_base32, 10, "sha512", 30, 0)
totp_password = totp.now()

auth_psws = email + ":" + totp_password
auth_psws_base64 = base64.b64encode(auth_psws.encode()).decode()

payload = {
    "github_url": github_url,
    "contact_email": email,
    "solution_language": solution_language,
}

url = "https://api.challenge.hennge.com/challenges/003"
headers = {
    "Authorization": f"Basic {auth_psws_base64}",
    "Content-Type": "application/json",
}

response = requests.post(url, data=json.dumps(payload), headers=headers)
if response.status_code == 200:
    print("Congratulations! You have achieved mission 3")
else:
    print("Mission 3 was not completed successfully.")
