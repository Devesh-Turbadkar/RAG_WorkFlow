text= """
documents or text
"""

chunking = text.strip().split("\n")

for chunk in chunking:
    print("chunk:")
    print(chunk)
    print()