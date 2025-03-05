def custom_encrypt(data):
    """Applies ROT13 to letters and custom substitution for numbers/symbols."""
    mapping = {
        **{chr(i): chr(((i - 65 + 13) % 26) + 65) for i in range(65, 91)},  # A-Z ROT13 (Proper Wrapping)
        **{chr(i): chr(((i - 97 + 13) % 26) + 97) for i in range(97, 123)},  # a-z ROT13 (Proper Wrapping)
        '1': '!', '2': '@', '3': '#', '4': '$', '5': '%', '6': '^', '7': '&', '8': '*', '9': '(', '0': ')',
        '!': '1', '@': '2', '#': '3', '$': '4', '%': '5', '^': '6', '&': '7', '*': '8', '(': '9', ')': '0'
    }
    return ''.join(mapping.get(c, c) for c in data)
