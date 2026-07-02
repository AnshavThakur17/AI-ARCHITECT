def estimate_cost(scale, database=None, cache=None, needs_queue=False, needs_cdn=False):
    try:
        scale = int(scale)
    except (ValueError, TypeError):
        scale = 10000

    # 1. Compute Cost (Servers/VMs)
    if scale <= 100000:
        servers = 1
        compute_cost = 15  # 1 micro instance at $15/mo
    elif scale <= 1000000:
        servers = 2
        compute_cost = 50  # 2 instances at $25/mo for HA
    else:
        servers = max(2, scale // 500000)
        compute_cost = servers * 50

    # 2. Database Cost
    db_name = str(database).lower() if database else ""
    if "cassandra" in db_name:
        if scale <= 100000:
            db_cost = 90  # Cassandra cluster minimum
        elif scale <= 1000000:
            db_cost = 180
        else:
            db_cost = 300 + ((scale - 1000000) // 5000000) * 150
    else:
        # PostgreSQL / MongoDB or other standard DB
        if scale <= 100000:
            db_cost = 15
        elif scale <= 1000000:
            db_cost = 50
        else:
            db_cost = 150 + ((scale - 1000000) // 5000000) * 75

    # 3. Cache Cost (Redis)
    cache_name = str(cache).lower() if cache else ""
    if "redis" in cache_name or "cache" in cache_name or cache_name == "active":
        if scale <= 100000:
            cache_cost = 15
        elif scale <= 1000000:
            cache_cost = 45
        else:
            cache_cost = 120
    else:
        cache_cost = 0

    # 4. Message Queue Cost
    if needs_queue:
        if scale <= 100000:
            queue_cost = 10
        elif scale <= 1000000:
            queue_cost = 30
        else:
            queue_cost = 100
    else:
        queue_cost = 0

    # 5. CDN Cost
    if needs_cdn:
        if scale <= 100000:
            cdn_cost = 0
        elif scale <= 1000000:
            cdn_cost = 20
        else:
            cdn_cost = 50 + (scale // 1000000) * 10
    else:
        cdn_cost = 0

    total_monthly_cost = compute_cost + db_cost + cache_cost + queue_cost + cdn_cost

    return {
        "servers_needed": servers,
        "monthly_cost_usd": total_monthly_cost,
        "breakdown": {
            "compute": compute_cost,
            "database": db_cost,
            "cache": cache_cost,
            "queue": queue_cost,
            "cdn": cdn_cost
        }
    }