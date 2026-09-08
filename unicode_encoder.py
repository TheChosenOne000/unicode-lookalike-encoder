"""
Unicode Lookalike Text Encoder
Transforms English text into visually identical Unicode characters
that may not be recognized by exact-match text detection systems.
"""

# Unicode lookalike character mappings
# Maps standard ASCII letters to Unicode characters that look nearly identical
UNICODE_LOOKALIKES = {
    # Uppercase Latin to Cyrillic/Mathematical lookalikes
    'A': '𝐀',  # Mathematical Alphanumeric Bold A (U+1D400)
    'B': '𝐁',  # Mathematical Alphanumeric Bold B (U+1D401)
    'C': '𝐂',  # Mathematical Alphanumeric Bold C (U+1D402)
    'D': '𝐃',  # Mathematical Alphanumeric Bold D (U+1D403)
    'E': '𝐄',  # Mathematical Alphanumeric Bold E (U+1D404)
    'F': '𝐅',  # Mathematical Alphanumeric Bold F (U+1D405)
    'G': '𝐆',  # Mathematical Alphanumeric Bold G (U+1D406)
    'H': '𝐇',  # Mathematical Alphanumeric Bold H (U+1D407)
    'I': '𝐈',  # Mathematical Alphanumeric Bold I (U+1D408)
    'J': '𝐉',  # Mathematical Alphanumeric Bold J (U+1D409)
    'K': '𝐊',  # Mathematical Alphanumeric Bold K (U+1D40A)
    'L': '𝐋',  # Mathematical Alphanumeric Bold L (U+1D40B)
    'M': '𝐌',  # Mathematical Alphanumeric Bold M (U+1D40C)
    'N': '𝐍',  # Mathematical Alphanumeric Bold N (U+1D40D)
    'O': '𝐎',  # Mathematical Alphanumeric Bold O (U+1D40E)
    'P': '𝐏',  # Mathematical Alphanumeric Bold P (U+1D40F)
    'Q': '𝐐',  # Mathematical Alphanumeric Bold Q (U+1D410)
    'R': '𝐑',  # Mathematical Alphanumeric Bold R (U+1D411)
    'S': '𝐒',  # Mathematical Alphanumeric Bold S (U+1D412)
    'T': '𝐓',  # Mathematical Alphanumeric Bold T (U+1D413)
    'U': '𝐔',  # Mathematical Alphanumeric Bold U (U+1D414)
    'V': '𝐕',  # Mathematical Alphanumeric Bold V (U+1D415)
    'W': '𝐖',  # Mathematical Alphanumeric Bold W (U+1D416)
    'X': '𝐗',  # Mathematical Alphanumeric Bold X (U+1D417)
    'Y': '𝐘',  # Mathematical Alphanumeric Bold Y (U+1D418)
    'Z': '𝐙',  # Mathematical Alphanumeric Bold Z (U+1D419)
    
    # Lowercase Latin to Mathematical lookalikes
    'a': '𝐚',  # Mathematical Alphanumeric Bold a (U+1D41A)
    'b': '𝐛',  # Mathematical Alphanumeric Bold b (U+1D41B)
    'c': '𝐜',  # Mathematical Alphanumeric Bold c (U+1D41C)
    'd': '𝐝',  # Mathematical Alphanumeric Bold d (U+1D41D)
    'e': '𝐞',  # Mathematical Alphanumeric Bold e (U+1D41E)
    'f': '𝐟',  # Mathematical Alphanumeric Bold f (U+1D41F)
    'g': '𝐠',  # Mathematical Alphanumeric Bold g (U+1D420)
    'h': '𝐡',  # Mathematical Alphanumeric Bold h (U+1D421)
    'i': '𝐢',  # Mathematical Alphanumeric Bold i (U+1D422)
    'j': '𝐣',  # Mathematical Alphanumeric Bold j (U+1D423)
    'k': '𝐤',  # Mathematical Alphanumeric Bold k (U+1D424)
    'l': '𝐥',  # Mathematical Alphanumeric Bold l (U+1D425)
    'm': '𝐦',  # Mathematical Alphanumeric Bold m (U+1D426)
    'n': '𝐧',  # Mathematical Alphanumeric Bold n (U+1D427)
    'o': '𝐨',  # Mathematical Alphanumeric Bold o (U+1D428)
    'p': '𝐩',  # Mathematical Alphanumeric Bold p (U+1D429)
    'q': '𝐪',  # Mathematical Alphanumeric Bold q (U+1D42A)
    'r': '𝐫',  # Mathematical Alphanumeric Bold r (U+1D42B)
    's': '𝐬',  # Mathematical Alphanumeric Bold s (U+1D42C)
    't': '𝐭',  # Mathematical Alphanumeric Bold t (U+1D42D)
    'u': '𝐮',  # Mathematical Alphanumeric Bold u (U+1D42E)
    'v': '𝐯',  # Mathematical Alphanumeric Bold v (U+1D42F)
    'w': '𝐰',  # Mathematical Alphanumeric Bold w (U+1D430)
    'x': '𝐱',  # Mathematical Alphanumeric Bold x (U+1D431)
    'y': '𝐲',  # Mathematical Alphanumeric Bold y (U+1D432)
    'z': '𝐳',  # Mathematical Alphanumeric Bold z (U+1D433)
    
    # Numbers stay the same
    '0': '0', '1': '1', '2': '2', '3': '3', '4': '4',
    '5': '5', '6': '6', '7': '7', '8': '8', '9': '9',
    
    # Common punctuation stays the same
    ' ': ' ', '.': '.', ',': ',', '!': '!', '?': '?',
    "'": "'", '"': '"', '-': '-', '_': '_', ':': ':', ';': ';',
}

# Create reverse mapping for decoding
REVERSE_LOOKALIKES = {v: k for k, v in UNICODE_LOOKALIKES.items()}


def encode_text(text):
    """
    Transform English text into Unicode lookalike characters.
    
    Args:
        text (str): The original English text
        
    Returns:
        str: Text with ASCII characters replaced by Unicode lookalikes
    """
    encoded = []
    for char in text:
        # Use lookalike if available, otherwise keep original
        encoded.append(UNICODE_LOOKALIKES.get(char, char))
    return ''.join(encoded)


def decode_text(text):
    """
    Convert Unicode lookalike text back to normal ASCII English.
    
    Args:
        text (str): The encoded Unicode text
        
    Returns:
        str: Text converted back to standard ASCII
    """
    decoded = []
    for char in text:
        # Use reverse mapping if available, otherwise keep original
        decoded.append(REVERSE_LOOKALIKES.get(char, char))
    return ''.join(decoded)


def get_hex_codes(text):
    """
    Get hexadecimal Unicode code points for each character.
    
    Args:
        text (str): The text to analyze
        
    Returns:
        list: List of tuples (character, unicode_code_point)
    """
    return [(char, hex(ord(char))) for char in text]


def compare_texts(original):
    """
    Compare original and encoded texts side-by-side with hex codes.
    
    Args:
        original (str): The original English text
    """
    encoded = encode_text(original)
    
    print("\n" + "="*70)
    print("UNICODE LOOKALIKE TRANSFORMATION COMPARISON")
    print("="*70)
    
    print(f"\nOriginal text:  {original}")
    print(f"Encoded text:   {encoded}")
    print(f"\nVisually identical? {original == encoded}  (Should be False)")
    print(f"Visually similar? Yes (looks the same to human eyes)")
    
    print("\n" + "-"*70)
    print(f"{'Char':<8} {'Original Hex':<18} {'Encoded Hex':<18} {'Encoded Char':<8}")
    print("-"*70)
    
    for orig_char, enc_char in zip(original, encoded):
        orig_hex = hex(ord(orig_char))
        enc_hex = hex(ord(enc_char))
        print(f"{orig_char:<8} {orig_hex:<18} {enc_hex:<18} {enc_char:<8}")
    
    print("="*70 + "\n")


def demonstrate_encoding():
    """
    Demonstrate the encoder with multiple examples.
    """
    examples = [
        "Hello World",
        "Python Code",
        "Secret Message",
        "GitHub User",
        "Unicode Test 123",
    ]
    
    for example in examples:
        compare_texts(example)
        encoded = encode_text(example)
        decoded = decode_text(encoded)
        print(f"Decoded back:   {decoded}")
        print(f"Match original? {decoded == example}\n")


if __name__ == "__main__":
    # Run demonstrations
    demonstrate_encoding()
    
    # Interactive mode
    print("\n" + "="*70)
    print("INTERACTIVE MODE")
    print("="*70)
    user_input = input("\nEnter text to encode (or press Enter to skip): ").strip()
    
    if user_input:
        encoded = encode_text(user_input)
        print(f"\nOriginal:  {user_input}")
        print(f"Encoded:   {encoded}")
        print(f"Hex comparison:")
        for orig, enc in zip(user_input, encoded):
            print(f"  {orig} (U+{ord(orig):04X}) → {enc} (U+{ord(enc):04X})")
