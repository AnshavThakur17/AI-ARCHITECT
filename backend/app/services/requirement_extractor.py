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

    
    match = re.search(r'(\d+)\s*million', prompt)

    if match:
        result["users"] = int(match.group(1)) * 1000000

    
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