def recommend_database(requirements):

    if requirements["consistency_requirement"] == "high":

        return {
            "database": "PostgreSQL",
            "reason": "Strong ACID guarantees needed"
        }

    if requirements["write_heavy"] and requirements["geo_distributed"]:

        return {
            "database": "Cassandra",
            "reason": "Distributed writes at global scale"
        }

    if requirements["read_heavy"]:

        return {
            "database": "MongoDB",
            "reason": "Flexible schema and fast reads"
        }

    return {
        "database": "PostgreSQL",
        "reason": "Reliable default database"
    }