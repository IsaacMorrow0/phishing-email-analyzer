def color_text(text, color):
    colors = {
        "red": "\033[91m",
        "green": "\033[92m",
        "yellow": "\033[93m",
        "end": "\033[0m",
    }
    return f"{colors[color]}{text}{colors['end']}"

def extract_header_field(header, field_name):
    import re
    pattern = rf"{field_name}:\s*(.*)"
    match = re.search(pattern, header, re.IGNORECASE)
    return match.group(1).strip() if match else None
