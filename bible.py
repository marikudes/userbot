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
        self.max_length = 4000  # Maximum length for the chapter text

    def clean_text(self, text):
        # Remove excessive line breaks and extra whitespace
        cleaned_lines = [line.strip() for line in text.split('\n') if line.strip()]
        cleaned_text = ' '.join(cleaned_lines)
        return cleaned_text

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
            chapter_text = self.clean_text(chapter_text)  # Clean the chapter text
            # Truncate the chapter text if it's too long
            if len(chapter_text) > self.max_length:
                chapter_text = chapter_text[:self.max_length]
            
            return chapter_text
        else:
            return False

    def return_random_chapter(self):
        book = random.choice(list(BibleBooks))
        total_chapters = CHAPTERS_IN_BOOKS[book.value]
        chapter_number = random.randint(1, total_chapters)
        chapter_text = self.return_chapter(book.value, chapter_number)
        
        if chapter_text:
            # Ensure the final message is within the limit
            final_message = f"{book.value}\n{chapter_text}"
            if len(final_message) > self.max_length:
                final_message = final_message[:self.max_length]
            return final_message
        else:
            return "Chapter not found."
