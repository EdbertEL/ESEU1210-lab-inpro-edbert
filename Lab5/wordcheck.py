# def main():
#     dictionary = {}

#     infile = open(".\\Lab5\\words.txt", "r")
#     fields = extractRecord(infile)
#     while len(fields) > 0:
#         addWord(dictionary, fields[1], fields[0])
#         fields = extractRecord(infile)
    
#     infile.close()

# def addWord(entries, term, page):


# PERLU SPLIT ALICE STORY DARI PUNCTUATION ( , ? ! . " \ ` etc)
def count_words(text):
    word_count = 0
    unique_words = set()
    words = text.split()
    
    for word in words:
        word_count += 1
        unique_words.add(word.lower())
    
    return word_count, len(unique_words)

def find_misspelled_words(text, dictionary):
    misspelled_words = set()
    words = text.split()
    dictionary_set = set(dictionary)
    
    for word in words:
        if word.lower() not in dictionary_set:
            misspelled_words.add(word)
    
    return misspelled_words

# Read from alice.txt
with open(".\\Lab5\\alice.txt", "r") as alice_file:
    alice_text = alice_file.read()
    split_text = alice_text

# Count words and unique words
word_count, unique_word_count = count_words(alice_text)
print("Total words:", word_count)
print("Unique words:", unique_word_count)

# Read from words.txt
with open(".\\Lab5\\words.txt", "r") as words_file:
    dictionary = words_file.read().splitlines()

# Find misspelled words
misspelled_words = find_misspelled_words(alice_text, dictionary)
print("Misspelled words:", misspelled_words)






















# def main():
#     dictionary = {}

#     infile = open(".\\Lab5\\words.txt", "r")
#     fields = extractRecord(infile)
#     while len(fields) > 0:
#         addWord(dictionary, fields[1], fields[0])
#         fields = extractRecord(infile)
    
#     infile.close()

#     print(dictionary)

# def extractRecord(infile):
#     line = infile.readline()
#     if line != "":
#         fields = line.split(":")
#         page = int(fields[0])
#         term = fields[1].rstrip()
#         return [page, term]
#     else:
#         return []
    
# def addWord(entries, term, page):
#     if term in entries:
#         pageSet = entries[term]
#         pageSet.add(page)

#     else:
#         pageSet = set([page])
#         entries[term] = pageSet

#     for key in sorted(entries):
#         print(key, end="")
#         pageSet = entries[key]
#         first = True
#         for page in sorted(pageSet):
#             if first:
#                 print(page, end="")
#                 first = False
#             else:
#                 print(",", page, end="")
#         print()