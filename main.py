def main():
  book_path = "books/frankenstein.txt"
  text = get_book_text(book_path)
  word_count = get_word_count(text)
  char_table = get_uniq_char_count(text)
  header = f"--- Begin report of books/frankenstein.txt ---\n{word_count} words found in the document"
  sorted_char_table = sorted(char_table.items(), key=lambda item:item[1], reverse=True)
  for char in sorted_char_table:
    header += f"\nThe {char[0]} character was found {char[1]} times"
  header += "\n--- End report ---"
  print(header)

def get_book_text(path):
  with open(path) as f:
    return f.read()

def get_word_count(text):
  words = text.split()
  return len(words)

def get_uniq_char_count(text):
  letters = {}
  for char in text:
    if char.isalpha():
      lowered = char.lower()
      if lowered in letters:
        letters[lowered] += 1
      else:
        letters[lowered] = 1
  return letters
main()