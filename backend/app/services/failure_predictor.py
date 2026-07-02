def predict_failures(
        requirements,
        decisions):

    failures = []

    if decisions["needs_sharding"]:
        failures.append(
            "Database partition imbalance"
        )

    if requirements["low_latency"]:
        failures.append(
            "Latency spikes during peak traffic"
        )

    if requirements["write_heavy"]:
        failures.append(
            "Database write saturation"
        )

    if requirements["geo_distributed"]:
        failures.append(
            "Cross region replication delays"
        )

    return failures