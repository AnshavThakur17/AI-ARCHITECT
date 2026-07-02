def recommend_architecture(
        requirements):

    architecture = [
        "Load Balancer",
        "API Gateway"
    ]

    if requirements["real_time"]:
        architecture.append(
            "WebSocket Server"
        )

    if requirements["low_latency"]:
        architecture.append(
            "Redis Cache"
        )

    if requirements["geo_distributed"]:
        architecture.append(
            "CDN"
        )

        architecture.append(
            "Edge Server"
        )

    architecture.append(
        "Core Service Layer"
    )

    return architecture