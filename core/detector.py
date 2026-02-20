import re

SUSPICIOUS_KEYWORDS = [
    "login", "verify", "bank", "secure", "free", "offer", "win", "click"
]

def analyze_link(link):
    score = 0

    for word in SUSPICIOUS_KEYWORDS:
        if word in link.lower():
            score += 1

    if re.search(r"(xyz|tk|ml|ga)", link):
        score += 2

    if link.count(".") > 3:
        score += 1

    if score >= 3:
        return "danger"
    elif score == 2:
        return "suspicious"
    else:
        return "safe"
