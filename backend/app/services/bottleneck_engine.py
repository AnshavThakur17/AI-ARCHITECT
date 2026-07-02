def predict_bottlenecks(app_type):

    bottlenecks = {

        "Chat Application": [
            "WebSocket scaling issue",
            "Database write overload",
            "Memory spikes"
        ],

        "Ecommerce Application": [
            "Inventory race conditions",
            "Payment failures",
            "Heavy database reads"
        ],

        "Video Streaming Platform": [
            "Bandwidth bottleneck",
            "CDN latency",
            "Storage overflow"
        ],

        "Ride Sharing App": [
            "Real-time location overload",
            "Matching delays",
            "High traffic spikes"
        ]
    }

    return bottlenecks.get(app_type, [])