# Check how many vowels are in the entire phrase

# Receive an input
phrase = input("Enter a phrase to analyze: ").lower()

a = phrase.count("a")
e = phrase.count("e")
i = phrase.count("i")
o = phrase.count("o")
u = phrase.count("u")

print("Number of a's:", a, "\n" +
      "Number of e's:", e, "\n" +
      "Number of i's:", i, "\n" +
      "Number of o's:", o, "\n" +
      "Number of u's:", u, "\n")