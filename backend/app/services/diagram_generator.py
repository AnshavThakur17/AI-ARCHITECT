def generate_diagram(architecture, database):

    nodes = []

    edges = []

    # starting node

    nodes.append("User")


    # architecture nodes

    for component in architecture:
        nodes.append(component)


    # database node

    nodes.append(database)


    # create edges

    previous = "User"

    for component in architecture:

        edges.append({
            "from": previous,
            "to": component
        })

        previous = component


    edges.append({
        "from": previous,
        "to": database
    })


    return {
        "nodes": nodes,
        "edges": edges
    }