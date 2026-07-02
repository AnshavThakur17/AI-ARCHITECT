def generate_reasoning(
        requirements,
        decisions,
        architecture):

    reasoning = []

    for component in architecture:

        if component == "Load Balancer":

            reasoning.append({

                "component":
                "Load Balancer",

                "reason":
                "Distributes incoming traffic across servers"
            })


        elif component == "API Gateway":

            reasoning.append({

                "component":
                "API Gateway",

                "reason":
                "Central entry point for all services"
            })


        elif component == "Redis Cache":

            reasoning.append({

                "component":
                "Redis Cache",

                "reason":
                "Improves low latency data retrieval"
            })


        elif component == "CDN":

            reasoning.append({

                "component":
                "CDN",

                "reason":
                "Global content delivery reduces latency"
            })


        elif component == "WebSocket Server":

            reasoning.append({

                "component":
                "WebSocket Server",

                "reason":
                "Required for real time communication"
            })


        elif component == "Edge Server":

            reasoning.append({

                "component":
                "Edge Server",

                "reason":
                "Processes requests closer to users"
            })


    return reasoning