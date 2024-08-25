import random
import enum

class BibleBooks(enum.Enum):
    GENESIS = "Бытие"
    EXODUS = "Исход"
    LEVITICUS = "Левит"
    NUMBERS = "Числа"
    DEUTERONOMY = "Второзаконие"

CHAPTERS_IN_BOOKS = {
    BibleBooks.GENESIS.value: 50,
    BibleBooks.EXODUS.value: 40,
    BibleBooks.LEVITICUS.value: 27,
    BibleBooks.NUMBERS.value: 36,
    BibleBooks.DEUTERONOMY.value: 34,
}

class Bible:
    def __init__(self):
        self.filename = 'bible.txt'

    def return_chapter(self, book_name, chapter_number):
        with open(self.filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        book_str = book_name.upper()
        chapter_str = f"Глава {chapter_number}"
        next_chapter_str = f"Глава {chapter_number + 1}"
        
        in_book = False
        start_index = None
        end_index = None

        for i, line in enumerate(lines):
            if book_str in line.strip().upper():
                in_book = True
            if in_book and chapter_str in line.strip():
                start_index = i
            if in_book and next_chapter_str in line.strip():
                end_index = i
                break

        if start_index is not None:
            if end_index is not None:
                chapter_lines = lines[start_index:end_index]
            else:
                chapter_lines = lines[start_index:]
            
            chapter_text = ''.join(chapter_lines).strip()
            return chapter_text
        else:
            return False

    def return_random_chapter(self):
        book = random.choice(list(BibleBooks))
        total_chapters = CHAPTERS_IN_BOOKS[book.value]
        chapter_number = random.randint(1, total_chapters)
        return book.value + '\n' + self.return_chapter(book.value, chapter_number)

if __name__ == '__main__':
    print(Bible().return_random_chapter())