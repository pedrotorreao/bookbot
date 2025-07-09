def get_book_text(filepath):
    file_contents = ""

    with open(filepath) as f:
        file_contents = f.read()

    return file_contents
