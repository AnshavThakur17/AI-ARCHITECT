def estimate_cost(users):

    servers = users // 10000000

    if servers < 1:
        servers = 1

    monthly_cost = servers * 250

    return {
        "servers_needed": servers,
        "monthly_cost_usd": monthly_cost
    }