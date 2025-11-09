def read_book(path):
    with open(path, mode="r", encoding="utf-8") as book_file:
        book_lines = book_file.readlines()
    clean_lines = [line.strip().lower() for line in book_lines]
    
    # Split each line into words and flatten the list
    words = [word for line in clean_lines for word in line.split() if word]
    return words
