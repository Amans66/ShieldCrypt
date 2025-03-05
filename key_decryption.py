def custom_decrypt(data):
    """Reverses ROT13 for letters and restores numbers/symbols."""
    reverse_mapping = {
        **{chr(((i - 65 + 13) % 26) + 65): chr(i) for i in range(65, 91)},  # A-Z ROT13 reverse
        **{chr(((i - 97 + 13) % 26) + 97): chr(i) for i in range(97, 123)},  # a-z ROT13 reverse
        '!': '1', '@': '2', '#': '3', '$': '4', '%': '5', '^': '6', '&': '7', '*': '8', '(': '9', ')': '0',
        '0': '!', '9': '@', '8': '#', '7': '$', '6': '%', '5': '^', '4': '&', '3': '*', '2': '(', '1': ')'
    }
    return ''.join(reverse_mapping.get(c, c) for c in data)
