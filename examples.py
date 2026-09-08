"""
Example scripts demonstrating the Unicode lookalike encoder
"""

from unicode_encoder import encode_text, decode_text, compare_texts, get_hex_codes

def example_1_basic_encoding():
    """Example 1: Basic encoding and decoding"""
    print("\n" + "="*70)
    print("EXAMPLE 1: Basic Encoding and Decoding")
    print("="*70)
    
    text = "Hello World"
    encoded = encode_text(text)
    decoded = decode_text(encoded)
    
    print(f"\nOriginal:  {text}")
    print(f"Encoded:   {encoded}")
    print(f"Decoded:   {decoded}")
    print(f"\nMatch? {decoded == text}")


def example_2_hex_comparison():
    """Example 2: Show hex codes side-by-side"""
    print("\n" + "="*70)
    print("EXAMPLE 2: Hexadecimal Code Point Comparison")
    print("="*70)
    
    text = "Python"
    print(f"\nOriginal text: {text}")
    
    hex_codes = get_hex_codes(text)
    print("\nASCII Hex Codes:")
    for char, code in hex_codes:
        print(f"  {char}: {code}")
    
    encoded = encode_text(text)
    print(f"\nEncoded text: {encoded}")
    
    hex_codes_encoded = get_hex_codes(encoded)
    print("\nUnicode Hex Codes:")
    for char, code in hex_codes_encoded:
        print(f"  {char}: {code}")


def example_3_detailed_comparison():
    """Example 3: Detailed character-by-character comparison"""
    print("\n" + "="*70)
    print("EXAMPLE 3: Detailed Character Comparison")
    print("="*70)
    
    compare_texts("GitHub")


def example_4_multiple_texts():
    """Example 4: Encode multiple different texts"""
    print("\n" + "="*70)
    print("EXAMPLE 4: Multiple Text Transformations")
    print("="*70)
    
    texts = [
        "Admin",
        "Password",
        "Secret123",
        "Test User",
        "GitHub Username"
    ]
    
    for text in texts:
        encoded = encode_text(text)
        print(f"\n{text:<20} → {encoded}")


def example_5_character_mapping_table():
    """Example 5: Show the complete character mapping"""
    print("\n" + "="*70)
    print("EXAMPLE 5: Complete Character Mapping Table")
    print("="*70)
    
    from unicode_encoder import UNICODE_LOOKALIKES
    
    print("\nUppercase Letters:")
    uppercase = {k: v for k, v in UNICODE_LOOKALIKES.items() if k.isupper() and k.isalpha()}
    for i, (orig, enc) in enumerate(sorted(uppercase.items())):
        print(f"  {orig} (U+{ord(orig):04X}) → {enc} (U+{ord(enc):04X})", end="")
        if (i + 1) % 3 == 0:
            print()
        else:
            print("  |", end="")
    print("\n")
    
    print("Lowercase Letters:")
    lowercase = {k: v for k, v in UNICODE_LOOKALIKES.items() if k.islower() and k.isalpha()}
    for i, (orig, enc) in enumerate(sorted(lowercase.items())):
        print(f"  {orig} (U+{ord(orig):04X}) → {enc} (U+{ord(enc):04X})", end="")
        if (i + 1) % 3 == 0:
            print()
        else:
            print("  |", end="")
    print("\n")


def example_6_numbers_and_punctuation():
    """Example 6: Show that numbers and punctuation stay the same"""
    print("\n" + "="*70)
    print("EXAMPLE 6: Numbers and Punctuation Preservation")
    print("="*70)
    
    text = "Test123!@#$%^&*()"
    encoded = encode_text(text)
    
    print(f"\nOriginal: {text}")
    print(f"Encoded:  {encoded}")
    
    print("\nCharacter Analysis:")
    for orig, enc in zip(text, encoded):
        if orig == enc:
            print(f"  {orig} → {enc} (UNCHANGED - not a letter)")
        else:
            print(f"  {orig} → {enc} (CHANGED - is a letter)")


def example_7_reversibility():
    """Example 7: Test reversibility of encoding/decoding"""
    print("\n" + "="*70)
    print("EXAMPLE 7: Encoding Reversibility Test")
    print("="*70)
    
    original_texts = [
        "Hello World",
        "The Quick Brown Fox",
        "Unicode Test 12345",
        "Special!@# Characters?"
    ]
    
    print("\nTesting encode → decode reversibility:\n")
    all_pass = True
    
    for text in original_texts:
        encoded = encode_text(text)
        decoded = decode_text(encoded)
        matches = (decoded == text)
        all_pass = all_pass and matches
        
        status = "✓ PASS" if matches else "✗ FAIL"
        print(f"{status}: {text:<30} → {encoded:<30} → {decoded}")
    
    print(f"\nAll tests passed: {all_pass}")


def example_8_string_comparison():
    """Example 8: Demonstrate string comparison differences"""
    print("\n" + "="*70)
    print("EXAMPLE 8: String Comparison Behavior")
    print("="*70)
    
    original = "admin"
    encoded = encode_text(original)
    
    print(f"\nOriginal: {original}")
    print(f"Encoded:  {encoded}")
    
    print(f"\nComparisons:")
    print(f"  original == original: {original == original}")
    print(f"  encoded == encoded:   {encoded == encoded}")
    print(f"  original == encoded:  {original == encoded}")
    print(f"  original.lower() == encoded.lower(): {original.lower() == encoded.lower()}")
    
    print(f"\nByte representations:")
    print(f"  original bytes: {original.encode('utf-8')}")
    print(f"  encoded bytes:  {encoded.encode('utf-8')}")
    
    print(f"\nVisually they look the same, but technically they're different!")


def example_9_unicode_normalization():
    """Example 9: Show how Unicode normalization can undo the encoding"""
    print("\n" + "="*70)
    print("EXAMPLE 9: Unicode Normalization (Security Consideration)")
    print("="*70)
    
    import unicodedata
    
    original = "Hello"
    encoded = encode_text(original)
    
    # Try different normalization forms
    normalization_forms = ['NFC', 'NFD', 'NFKC', 'NFKD']
    
    print(f"\nOriginal: {original}")
    print(f"Encoded:  {encoded}")
    
    print("\nNormalization results:")
    for form in normalization_forms:
        normalized = unicodedata.normalize(form, encoded)
        matches = (normalized == original)
        print(f"  {form}: {normalized} (matches original: {matches})")


def example_10_practical_use_case():
    """Example 10: Practical use case simulation"""
    print("\n" + "="*70)
    print("EXAMPLE 10: Practical Use Case - Website Username Check")
    print("="*70)
    
    # Simulate a website database
    valid_usernames = ["admin", "user", "guest"]
    
    print(f"\nValid usernames in database: {valid_usernames}")
    
    # Try logging in with normal and encoded versions
    test_cases = [
        ("admin", "Normal ASCII"),
        (encode_text("admin"), "Unicode Lookalike"),
    ]
    
    print("\nLogin attempts:")
    for username, description in test_cases:
        is_valid = username in valid_usernames
        print(f"  {description:<25} '{username}' → {'✓ Valid' if is_valid else '✗ Invalid'}")
    
    print("\nConclusion: Without proper normalization, lookalike characters bypass simple checks!")


if __name__ == "__main__":
    print("\n" + "#"*70)
    print("# UNICODE LOOKALIKE ENCODER - COMPREHENSIVE EXAMPLES")
    print("#"*70)
    
    # Run all examples
    example_1_basic_encoding()
    example_2_hex_comparison()
    example_3_detailed_comparison()
    example_4_multiple_texts()
    example_5_character_mapping_table()
    example_6_numbers_and_punctuation()
    example_7_reversibility()
    example_8_string_comparison()
    example_9_unicode_normalization()
    example_10_practical_use_case()
    
    print("\n" + "#"*70)
    print("# END OF EXAMPLES")
    print("#"*70 + "\n")
