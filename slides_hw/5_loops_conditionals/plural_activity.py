
# Activity

## Plural Activity


``` python
word = "bʌs"

# define natural classes
sibilants = ["s", "z", "ʃ", "ʒ", "tʃ", "dʒ"]
voiceless = ["p", "t", "k", "f", "θ"]

# check word-final segment
ends_sibilant = any(word.endswith(sib) for sib in sibilants)
ends_voiceless = any(word.endswith(vcl) for vcl in voiceless)

print("Sibilant final?", ends_sibilant)
print("Voiceless final?", ends_voiceless)

if ends_sibilant:
    plural = word + "ɪz"
elif ends_voiceless:
    plural = word + "s"
else:
    plural = word + "z"

print("Plural:", plural)
```
