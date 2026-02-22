def check_link(url):
    suspicious_keywords = [
        "login", "verify", "bank", "secure",
        "account", "update", "password", "phishing"
    ]

    for word in suspicious_keywords:
        if word in url.lower():
            return "BLOCKED ⚠️ Phishing Detected"

    if url.startswith("http://"):
        return "WARNING ⚠️ Not Secure (HTTP)"

    return "SAFE ✅"


link = input("Enter a link: ")
result = check_link(link)
print(result)
