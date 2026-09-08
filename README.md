# Unicode Lookalike Text Encoder

A Python program that transforms English text into visually identical Unicode characters. This is useful for understanding Unicode, text encoding, and why websites need robust text normalization.

## 📋 Overview

This tool converts standard ASCII English letters into Unicode lookalike characters from the **Mathematical Alphanumeric Symbols** block (U+1D400–U+1D7FF). The encoded text **looks identical to human eyes** but consists of completely different Unicode code points, which may bypass exact-match text detection systems.

### Key Features:
- ✅ **Encode text** → Transform ASCII to Unicode lookalikes
- ✅ **Decode text** → Convert Unicode lookalikes back to ASCII
- ✅ **Side-by-side comparison** → View original vs encoded with hex codes
- ✅ **Interactive mode** → Test with your own text
- ✅ **Detailed documentation** → Learn which Unicode characters are used

---

## 🔤 Unicode Character Mappings

### What characters are used?

The encoder uses **Mathematical Alphanumeric Bold** characters from Unicode block U+1D400–U+1D433:

| Original | Unicode | Hex Code | Visual |
|----------|---------|----------|--------|
| A | 𝐀 | U+1D400 | Bold A |
| B | 𝐁 | U+1D401 | Bold B |
| C | 𝐂 | U+1D402 | Bold C |
| ... | ... | ... | ... |
| Z | 𝐙 | U+1D419 | Bold Z |
| a | 𝐚 | U+1D41A | Bold a |
| b | 𝐛 | U+1D41B | Bold b |
| ... | ... | ... | ... |
| z | 𝐳 | U+1D433 | Bold z |

**Numbers, spaces, and punctuation remain unchanged.**

---

## 🚀 Usage

### Installation
```bash
# No external dependencies required!
python unicode_encoder.py
```

### Basic Examples

#### Encoding
```python
from unicode_encoder import encode_text, decode_text

# Encode text
original = "Hello World"
encoded = encode_text(original)
print(f"Original: {original}")
print(f"Encoded:  {encoded}")
# Output:
# Original: Hello World
# Encoded:  𝐇𝐞𝐥𝐥𝐨 𝐖𝐨𝐫𝐥𝐝
```

#### Decoding
```python
# Decode back to ASCII
decoded = decode_text(encoded)
print(f"Decoded: {decoded}")
# Output: Decoded: Hello World
```

#### Side-by-Side Comparison
```python
from unicode_encoder import compare_texts

compare_texts("Python")
```

Output:
```
======================================================================
UNICODE LOOKALIKE TRANSFORMATION COMPARISON
======================================================================

Original text:  Python
Encoded text:   𝐏𝐲𝐭𝐡𝐨𝐧

Visually identical? False  (Should be False)
Visually similar? Yes (looks the same to human eyes)

----------------------------------------------------------------------
Char     Original Hex       Encoded Hex         Encoded Char
----------------------------------------------------------------------
P        0x50               0x1d40f             𝐏
y        0x79               0x1d432             𝐲
t        0x74               0x1d42d             𝐭
h        0x68               0x1d421             𝐡
o        0x6f               0x1d428             𝐨
n        0x6e               0x1d427             𝐧
======================================================================
```

#### Get Hex Codes
```python
from unicode_encoder import get_hex_codes

text = "Hi"
codes = get_hex_codes(text)
for char, hex_code in codes:
    print(f"{char}: {hex_code}")
# Output:
# H: 0x48
# i: 0x69
```

---

## 🎯 Real-World Examples

### Example 1: Website Usernames
```
Original: admin
Encoded:  𝐚𝐝𝐦𝐢𝐧
```

If a website checks `if username == "admin"`, the encoded version would **not match** because the characters are technically different, even though they look the same.

### Example 2: Email Addresses
```
Original: test@example.com
Encoded:  𝐭𝐞𝐬𝐭@𝐞𝐱𝐚𝐦𝐩𝐥𝐞.𝐜𝐨𝐦
```

### Example 3: Authentication Bypass (Theoretical)
```
Original: password123
Encoded:  𝐩𝐚𝐬𝐬𝐰𝐨𝐫𝐝123
```

---

## ⚠️ Limitations & Security Considerations

### 1. **Unicode Normalization**
Modern systems use **Unicode normalization** (NFC, NFD, NFKC, NFKD) which can convert lookalike characters back to ASCII.

```python
import unicodedata

text = "𝐇𝐞𝐥𝐥𝐨"
normalized = unicodedata.normalize('NFKC', text)
print(normalized)  # Output: Hello (converted back!)
```

### 2. **Font Rendering**
- Not all fonts display Mathematical Alphanumeric characters
- Some systems fall back to ASCII, destroying the lookalike effect
- Terminal emulators may not support these characters

### 3. **Security Systems**
- **Confusables databases** (used by browsers, GitHub, etc.) automatically detect and flag lookalike characters
- **Unicode security mechanisms** in modern frameworks prevent these attacks
- Most modern websites normalize text before comparison

### 4. **Website Protection**
Modern websites implement:
- Unicode NFKC normalization on user input
- Confusables detection
- Character whitelisting
- Server-side validation

### 5. **Why This Matters**
Understanding Unicode vulnerabilities helps developers:
- Properly normalize user input
- Implement security validations
- Prevent homograph attacks
- Handle international text correctly

---

## 📚 Unicode Blocks Used

| Block Name | Range | Purpose | Characters |
|------------|-------|---------|------------|
| Mathematical Alphanumeric Symbols | U+1D400–U+1D7FF | Math notation, bold/italic text | Letters, digits, symbols |
| Cyrillic | U+0400–U+04FF | Eastern European languages | Some look like Latin (А, В, С) |
| Greek | U+0370–U+03FF | Greek language, math | Some look like Latin (ρ, ν) |

---

## 🔬 How It Works

### Character Mapping Process
1. **ASCII Character Input**: User provides normal English text
2. **Lookup Table**: Each character is looked up in the `UNICODE_LOOKALIKES` dictionary
3. **Unicode Replacement**: Character replaced with lookalike from Mathematical Alphanumeric block
4. **String Construction**: All replaced characters joined together
5. **Visual Output**: Result looks identical but has different byte representation

### Hex Code Comparison
```
Original: 'H' → ASCII U+0048 (01001000 binary) → Decimal 72
Encoded:  '𝐇' → Unicode U+1D40F (11101 01000001111 binary) → Decimal 119823
```

---

## 🛡️ Educational Use

This project demonstrates:
- Unicode character sets and code points
- Why text normalization is critical for security
- Homograph/lookalike attack vectors
- Proper input validation techniques
- Character encoding fundamentals

---

## 📖 Running the Program

### Option 1: Run Demonstrations
```bash
python unicode_encoder.py
```
This will show examples with "Hello World", "Python Code", etc.

### Option 2: Interactive Mode
```bash
python unicode_encoder.py
# Follow the prompt and enter your own text
```

### Option 3: Use as a Module
```python
from unicode_encoder import encode_text, decode_text, compare_texts

# Your code here
text = "Secret"
encoded = encode_text(text)
print(encoded)
```

---

## 📝 Function Reference

### `encode_text(text: str) -> str`
Transforms ASCII characters into Unicode lookalikes.

```python
result = encode_text("Hello")  # Returns: 𝐇𝐞𝐥𝐥𝐨
```

### `decode_text(text: str) -> str`
Converts Unicode lookalikes back to ASCII.

```python
result = decode_text("𝐇𝐞𝐥𝐥𝐨")  # Returns: Hello
```

### `get_hex_codes(text: str) -> list`
Returns list of (character, hex_code) tuples.

```python
codes = get_hex_codes("Hi")
# Returns: [('H', '0x48'), ('i', '0x69')]
```

### `compare_texts(original: str) -> None`
Prints detailed side-by-side comparison with hex codes.

```python
compare_texts("Test")
```

### `demonstrate_encoding() -> None`
Runs multiple examples showing the encoder in action.

---

## 🚨 Important Note

**This is for educational purposes only.** Using this technique to:
- Bypass security systems
- Evade moderation
- Create fake accounts
- Impersonate users
- Conduct phishing attacks

...is **illegal and unethical**.

Understanding Unicode vulnerabilities helps developers **defend against** these attacks, not exploit them.

---

## 📚 Further Reading

- [Unicode Standard](https://unicode.org/)
- [Unicode Security Considerations](https://unicode.org/reports/tr36/)
- [OWASP: Homograph Attack](https://owasp.org/www-community/attacks/Homograph_attack)
- [Python Unicode HOWTO](https://docs.python.org/3/howto/unicode.html)

---

## 📄 License

MIT License - Educational and research use

---

## 👨‍💻 Author

Created for Unicode text processing education.

**Questions?** Check the examples or read the source code comments!
