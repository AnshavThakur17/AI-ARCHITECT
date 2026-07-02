def system_decisions(requirements):

    decisions = {
        "needs_queue": False,
        "needs_cache": False,
        "needs_cdn": False,
        "needs_sharding": False,
        "consistency_requirement":
        requirements["consistency_requirement"]
    }

    if requirements["write_heavy"]:
        decisions["needs_queue"] = True

    if requirements["low_latency"]:
        decisions["needs_cache"] = True

    if requirements["geo_distributed"]:
        decisions["needs_cdn"] = True

    if requirements["scale"] > 1000000:
        decisions["needs_sharding"] = True

    return decisions