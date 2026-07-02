import re


def extract_requirements(prompt: str):

    prompt = prompt.lower()

    result = {
        "app_type": "unknown",
        "users": 10000,
        "real_time": False,
        "read_heavy": False,
        "write_heavy": False,
        "global_distribution": False,
        "latency_sensitive": False,
        "storage_needs": []
    }

    
    # Clean prompt to replace commas in numbers (e.g. 50,000 -> 50000)
    cleaned_prompt = re.sub(r'(\d+),(\d+)', r'\1\2', prompt)

    # match numbers, supporting words like million, m, k, thousand, users
    match = re.search(r'(\d+)\s*(million|m|k|thousand|users|voters)?', cleaned_prompt)

    if match:
        val = int(match.group(1))
        unit = match.group(2)
        if unit:
            if "million" in unit or unit == "m":
                result["users"] = val * 1000000
            elif "thousand" in unit or unit == "k":
                result["users"] = val * 1000
            else:
                result["users"] = val
        else:
            result["users"] = val

    
    if "chat" in prompt:
        result["app_type"] = "chat"
        result["real_time"] = True
        result["write_heavy"] = True
        result["storage_needs"] = [
            "messages",
            "attachments"
        ]

    elif "ecommerce" in prompt:
        result["app_type"] = "ecommerce"
        result["read_heavy"] = True
        result["storage_needs"] = [
            "products",
            "orders",
            "payments"
        ]

    elif "video" in prompt or "streaming" in prompt:
        result["app_type"] = "video_streaming"
        result["read_heavy"] = True
        result["latency_sensitive"] = True
        result["storage_needs"] = [
            "video files",
            "metadata",
            "watch history"
        ]

    elif "food delivery" in prompt:
        result["app_type"] = "food_delivery"
        result["real_time"] = True
        result["storage_needs"] = [
            "orders",
            "payments",
            "location"
        ]

    elif "payment" in prompt or "stripe" in prompt:
        result["app_type"] = "payment_processing"
        result["write_heavy"] = True
        result["latency_sensitive"] = True
        result["storage_needs"] = [
            "transactions",
            "audit logs",
            "payment records"
        ]

    # global detection
    if "global" in prompt:
        result["global_distribution"] = True

    # latency detection
    if "low latency" in prompt:
        result["latency_sensitive"] = True

    return result