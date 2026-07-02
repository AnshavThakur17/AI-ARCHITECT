def recommend_cache(decisions):

    if decisions["needs_cache"]:

        return {
            "cache": "Redis",
            "reason": "Low latency caching required"
        }

    return {
        "cache": "No cache required",
        "reason": "Caching not critical"
    }