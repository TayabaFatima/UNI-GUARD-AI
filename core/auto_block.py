def take_action(result, link):
    if result == "danger":
        print(f"🚫 BLOCKED: {link}")
        return "blocked"

    elif result == "suspicious":
        print(f"⚠️ WARNING: {link}")
        return "warning"

    else:
        print(f"✅ SAFE: {link}")
        return "allowed"
