def status(status):
    match status:
        case 200:
            return "ok"
        case 404:
            return "error not found"
        case 500:
            return "Internal service error"
        case _:
            return "Unknown status"