import re


def parse_prompt(prompt: str):

    prompt = prompt.lower()

    app_type = "Unknown"

    users = 10000


    if "chat" in prompt:
        app_type = "Chat Application"

    elif "ecommerce" in prompt:
        app_type = "Ecommerce Application"

    elif "video" in prompt:
        app_type = "Video Streaming Platform"

    elif "ride" in prompt or "uber" in prompt:
        app_type = "Ride Sharing App"


    match = re.search(r'(\d+)\s*million', prompt)

    if match:
        users = int(match.group(1)) * 1000000


    return {
        "app_type": app_type,
        "users": users
    }