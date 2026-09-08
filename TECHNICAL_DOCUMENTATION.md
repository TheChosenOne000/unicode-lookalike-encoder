"""
Technical Documentation: Unicode Lookalike Encoder

This document provides in-depth technical information about Unicode,
character encoding, and how the encoder works.
"""

# ============================================================================
# PART 1: UNICODE FUNDAMENTALS
# ============================================================================

"""
What is Unicode?
================

Unicode is a universal character encoding standard that assigns a unique 
numerical value (code point) to every character across all writing systems.

Key Facts:
- Unicode 15.0 contains over 149,000 characters
- Each character has a unique 21-bit code point (0x0 to 0x10FFFF)
- Code points are written in hex with "U+" prefix (e.g., U+0041 for 'A')
- ASCII (0x0-0x127) is a subset of Unicode for backwards compatibility

Unicode Planes:
- Basic Multilingual Plane (BMP): U+0000–U+FFFF (most common characters)
- Supplementary planes: U+10000–U+10FFFF (less common symbols, emojis, etc.)

This encoder uses characters from the Supplementary Multilingual Plane (SMP),
specifically the Mathematical Alphanumeric Symbols block (U+1D400–U+1D7FF).
"""

# ============================================================================
# PART 2: CHARACTER ENCODING SCHEMES
# ============================================================================

"""
How Characters are Encoded in Memory:
======================================

UTF-8 (Variable-length encoding):
- ASCII characters (U+0000–U+007F): 1 byte
- Most Latin characters (U+0080–U+07FF): 2 bytes
- BMP characters (U+0800–U+FFFF): 3 bytes
- Supplementary characters (U+10000–U+10FFFF): 4 bytes

Example:
- 'A' (U+0041): 0x41 (1 byte)
- '𝐀' (U+1D400): 0xF0 0x9D 0x90 0x80 (4 bytes)

UTF-16 (Fixed/variable-length):
- Most characters: 2 bytes (basic characters)
- Supplementary characters: 4 bytes (surrogate pairs)

UTF-32 (Fixed-length):
- All characters: 4 bytes
- Simple but less efficient

The encoder uses UTF-8 by default in Python strings.
"""

# ============================================================================
# PART 3: MATHEMATICAL ALPHANUMERIC SYMBOLS BLOCK
# ============================================================================

"""
Unicode Block: Mathematical Alphanumeric Symbols
=================================================

Range: U+1D400–U+1D7FF (224 characters)
Purpose: Mathematical typesetting and notation

Styles Available:
1. Bold (U+1D400–U+1D433)
   - Uppercase: U+1D400–U+1D419 (A–Z)
   - Lowercase: U+1D41A–U+1D433 (a–z)
   - Digits: U+1D434–U+1D43D (0–9)

2. Italic (U+1D434–U+1D46D)
   - Similar structure to Bold

3. Bold Italic (U+1D468–U+1D4A1)
   - Combination of bold and italic

4. Double-struck / Blackboard Bold (U+1D538–U+1D56B)
   - Mathematical number sets (ℝ, ℂ, ℤ, etc.)

5. Fraktur (U+1D504–U+1D537)
   - Gothic/medieval style

6. Script (U+1D49C–U+1D4CF)
   - Cursive style

The encoder uses BOLD style (U+1D400–U+1D433) as the primary mapping
because it's most visually similar to regular text.

Code Point Calculation:
=======================

For Bold Uppercase (A–Z):
- U+1D400 + offset = character code point
- Offset = position in alphabet (0–25)
- 'A' → U+1D400 + 0x00 = U+1D400
- 'Z' → U+1D400 + 0x19 = U+1D419

For Bold Lowercase (a–z):
- U+1D41A + offset = character code point
- Offset = position in alphabet (0–25)
- 'a' → U+1D41A + 0x00 = U+1D41A
- 'z' → U+1D41A + 0x19 = U+1D433
"""

# ============================================================================
# PART 4: LOOKALIKE DETECTION AND SECURITY
# ============================================================================

"""
Why Websites Block Lookalikes:
===============================

1. Homograph Attack Prevention
   - Attackers create fake accounts with lookalike usernames
   - Users can't distinguish between 'admin' and '𝐚𝐝𝐦𝐢𝐧'
   - Phishing: fake@gmai𝐥.com looks like fake@gmail.com

2. Unicode Confusables Database
   - Unicode Consortium maintains confusables.txt
   - Lists characters that look identical or very similar
   - Modern systems check against this database

3. NFKC Normalization
   - "Compatibility Decomposition" converts lookalikes to ASCII
   - Recommended by Unicode Security Considerations (TR36)
   - Most web frameworks apply this automatically

Example of NFKC Normalization:
  Input:  𝐇𝐞𝐥𝐥𝐨
  Output: Hello (lookalikes converted to ASCII)

Confusables.txt Example (simplified):
  0061 ; 043E   # LATIN SMALL LETTER A ← CYRILLIC SMALL LETTER O
  0042 ; 0412   # LATIN CAPITAL LETTER B ← CYRILLIC CAPITAL LETTER VE
  0041 ; 0410   # LATIN CAPITAL LETTER A ← CYRILLIC CAPITAL LETTER A
"""

# ============================================================================
# PART 5: HOW THE ENCODER WORKS INTERNALLY
# ============================================================================

"""
Encoding Process (Text → Lookalikes):
======================================

Step 1: Accept Input
  input = "Hello"

Step 2: Iterate Through Characters
  for char in input:
      # Process each character

Step 3: Dictionary Lookup
  UNICODE_LOOKALIKES = {
      'H': '𝐇',  # U+1D407
      'e': '𝐞',  # U+1D41E
      'l': '𝐥',  # U+1D425
      'o': '𝐨',  # U+1D428
  }

Step 4: Replacement
  mapped_char = UNICODE_LOOKALIKES.get(char, char)
  # If char not in dict, use original character

Step 5: Concatenation
  result = ''.join([mapped_char for each char])
  # Result: '𝐇𝐞𝐥𝐥𝐨'

Time Complexity: O(n) where n = length of input string
Space Complexity: O(n) for output string + O(1) for lookup table


Decoding Process (Lookalikes → Text):
=======================================

Same process in reverse using REVERSE_LOOKALIKES dictionary:
  REVERSE_LOOKALIKES = {
      '𝐇': 'H',
      '𝐞': 'e',
      '𝐥': 'l',
      '𝐨': 'o',
  }

Input:  '𝐇𝐞𝐥𝐥𝐨'
Output: 'Hello'
"""

# ============================================================================
# PART 6: LIMITATIONS AND EDGE CASES
# ============================================================================

"""
Limitation 1: Font Rendering
=============================

Mathematical Alphanumeric Symbols require specific font support.

Fonts that support it:
- Cambria Math
- Courier New
- DejaVu Sans Mono
- Noto Sans Math

Fonts that DON'T support it:
- Arial (some versions)
- Helvetica
- System fonts on older OS versions

Fallback behavior:
- Browser displays a "tofu box" (□) if font not available
- Terminal shows replacement character
- Mobile devices may render differently

Impact on encoder:
- Lookalike effect is lost on unsupported systems
- No way to force font rendering from client side
"""

"""
Limitation 2: Unicode Normalization
=====================================

Python's unicodedata module provides normalization:

import unicodedata

# Four normalization forms:
NFC  (Composed)       - combines characters
NFD  (Decomposed)     - separates combining characters
NFKC (Compatibility Composed)     - converts to ASCII equivalents
NFKD (Compatibility Decomposed)   - converts to ASCII + decomposes

Example:
  text = '𝐇𝐞𝐥𝐥𝐨'
  normalized = unicodedata.normalize('NFKC', text)
  print(normalized)  # Output: Hello (converted back!)

This is the BIGGEST vulnerability of this encoder.
NFKC normalization is the industry standard and defeats lookalikes.
"""

"""
Limitation 3: Security Frameworks
==================================

Modern web frameworks include security features:

Django:
- Applies Unicode normalization by default
- Slug fields use NFKC normalization
- Username validation includes confusables check

Flask:
- No automatic normalization, but best practice is to use it
- Extensions like Flask-Principal support it

Ruby on Rails:
- Normalizes usernames automatically
- Detects homograph attacks

Node.js/Express:
- npm packages available for normalization
- Example: npm unidecode

GitHub:
- Uses Unicode normalization
- Detects visually similar usernames
- Blocks accounts with confusable names

Result:
- Encoding doesn't work on most modern platforms
- Best reserved for educational/research purposes
"""

"""
Limitation 4: Character Support
================================

Not all characters have lookalikes:

Supported:
- Letters A-Z, a-z (all have Mathematical Alphanumeric equivalents)
- Can be extended to numbers, Greek letters, etc.

Not supported in this encoder:
- Special characters (@, #, $, etc.)
- Symbols (→, ±, ∞, etc.)
- International characters (é, ñ, ü, etc.)

For unsupported characters:
- They pass through unchanged
- This may make the encoding obvious

Example:
  Input:  "café"
- Output: "𝐜𝐚𝐟é"  (é stays the same)
- Easy to spot that é wasn't encoded
"""

# ============================================================================
# PART 7: ADVANCED TECHNIQUES (NOT IMPLEMENTED)
# ============================================================================

"""
Alternative Lookalike Sources:
===============================

1. Cyrillic Characters
   - А (U+0410) looks like A but is Cyrillic
   - В (U+0412) looks like B but is Cyrillic
   - Advantage: Simple, single-byte in UTF-8 (mostly)
   - Disadvantage: Easier to detect

2. Greek Letters
   - ν (U+03BD) looks like v
   - ρ (U+03C1) looks like p
   - Advantage: Natural looking
   - Disadvantage: Limited mappings

3. Combining Characters
   - Use diacritics to disguise letters
   - Example: A̅ (A with overline)
   - Advantage: Hard to normalize
   - Disadvantage: Very visible to careful observers

4. Zero-width Characters
   - U+200B (Zero-width space)
   - U+200C (Zero-width non-joiner)
   - Advantage: Invisible to humans
   - Disadvantage: Only useful for hidden data

5. Right-to-left Override
   - U+202E reverses text direction
   - Can make filenames appear different than they are
   - Example: "exe.txt" → "txt.exe" (visually)
"""

# ============================================================================
# PART 8: REAL-WORLD ATTACK SCENARIOS
# ============================================================================

"""
Scenario 1: Domain Squatting
============================

Attacker Goal: Create fake GitHub username similar to popular user

Normal:  "torvalds"  (Linus Torvalds)
Attack:  "𝐭𝐨𝐫𝐯𝐚𝐥𝐝𝐬" (looks identical)

Result: Users might not notice the difference and follow the fake account

Defense:
- GitHub normalizes usernames
- Detects homoglyphs
- Only one username per set of confusables


Scenario 2: Phishing Email
===========================

Attacker Goal: Send email from fake sender address

Normal:  admin@company.com
Attack:  𝐚𝐝𝐦𝐢𝐧@𝐜𝐨𝐦𝐩𝐚𝐧𝐲.𝐜𝐨𝐦

Result: Email appears to come from admin, but it's actually different

Defense:
- Email clients normalize headers
- DKIM/SPF verification checks actual domain
- Modern mail servers reject mismatches


Scenario 3: Password Bypass
============================

Attacker Goal: Create account with similar password

Normal:   password123
Attack:   𝐩𝐚𝐬𝐬𝐰𝐨𝐫𝐝123

Result: Password hashes are different, so authentication fails anyway

Defense:
- Already protected by hashing
- This attack doesn't work
"""

# ============================================================================
# PART 9: UNICODE SECURITY BEST PRACTICES
# ============================================================================

"""
For Developers:
===============

1. Always Normalize User Input
   import unicodedata
   
   def normalize_username(username):
       return unicodedata.normalize('NFKC', username).lower()

2. Implement Confusables Detection
   # Use Python package: confusables
   from confusables import is_confusable
   
   if is_confusable(username):
       raise ValueError("Username too similar to existing user")

3. Whitelist Allowed Characters
   import string
   ALLOWED_CHARS = set(string.ascii_letters + string.digits + '-_')
   
   if not all(c in ALLOWED_CHARS for c in username):
       raise ValueError("Invalid character in username")

4. Use Established Libraries
   # Django:
   from django.utils.text import slugify
   
   # Node.js:
   npm install unidecode
   
   # PHP:
   use Normalizer;
   $normalized = Normalizer::normalize($username, Normalizer::FORM_KC);

5. Log Security Events
   - Track attempts to use confusable characters
   - Alert admins of suspicious activity
   - Audit username changes


For Users:
==========

1. Copy-Paste Verification
   - Don't rely on visual inspection
   - Use browser's "inspect element" to verify
   - Check URL bar carefully

2. Bookmarks Over Typing
   - Use bookmarks for important sites
   - Reduces phishing risk

3. Two-Factor Authentication
   - Adds layer of protection
   - Stops account takeover even if password compromised

4. Browser Extensions
   - uBlock Origin: blocks known phishing sites
   - HTTPS Everywhere: enforces secure connections
"""

# ============================================================================
# PART 10: TESTING AND VERIFICATION
# ============================================================================

"""
How to Verify the Encoder Works:
=================================

Test 1: Reversibility
  original = "Test"
  encoded = encode_text(original)
  decoded = decode_text(encoded)
  assert decoded == original

Test 2: Byte Comparison
  original = "A"  # ASCII: 0x41
  encoded = encode_text(original)  # Unicode: 0xF0 0x9D 0x90 0x80
  assert len(original.encode()) != len(encoded.encode())

Test 3: Visual Inspection
  print(f"Original: {original}")
  print(f"Encoded:  {encoded}")
  # Should look the same to human eyes

Test 4: String Comparison
  assert original != encoded
  assert original == decode_text(encoded)

Test 5: Normalization Vulnerability
  import unicodedata
  normalized = unicodedata.normalize('NFKC', encoded)
  assert normalized == original  # Lookalike defeated by normalization

Test 6: Character Mapping
  for char in UNICODE_LOOKALIKES:
      encoded = encode_text(char)
      decoded = decode_text(encoded)
      assert char == decoded

Test 7: Edge Cases
  - Empty string: "" → ""
  - Numbers: "123" → "123" (unchanged)
  - Punctuation: "!!!" → "!!!" (unchanged)
  - Mixed: "Hello123!" → "𝐇𝐞𝐥𝐥𝐨123!"
"""

# ============================================================================
# PART 11: PERFORMANCE ANALYSIS
# ============================================================================

"""
Encoding Performance:
======================

Time Complexity:
- O(n) - iterate through each character once
- Dictionary lookup: O(1) average case
- String concatenation: O(n) amortized (Python strings are immutable)
- Total: O(n)

Space Complexity:
- O(n) - output string size
- O(1) - lookup tables (fixed 52 letters + numbers + punctuation)

Benchmark (approximate, Python 3.9+):
- 1 KB text: < 1 ms
- 1 MB text: < 100 ms
- 1 GB text: < 100 seconds

Optimization opportunities:
- Use list + join instead of string concatenation
- Pre-compile regex for validation
- Use Cython for C-level performance
- Parallel processing for very large texts


Memory Usage:
=============

Small text (< 1 KB):
- Original: ~1 KB
- Encoded: ~4 KB (Mathematical Alphanumeric are 4 bytes each in UTF-8)

Large text (1 MB):
- Original: ~1 MB
- Encoded: ~4 MB (4x expansion due to UTF-8 encoding)

Notes:
- Mathematical Alphanumeric characters are 4 bytes in UTF-8
- Pure ASCII is 1 byte per character
- Mixed content has variable size
"""

if __name__ == "__main__":
    print(__doc__)
