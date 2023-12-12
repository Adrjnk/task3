import unittest
from project.books.models import Book

# Testy poprawnych danych

class TestBookValidData(unittest.TestCase):
    def test_valid_data_complete(self):
        Book(name="Harry Potter", author="J.K. Rowling", year_published=1997, book_type="Fantasy", status="available")

    def test_valid_book_type_formats(self):
        valid_book_types = ["Fantasy", "Mystery", "Science Fiction"]
        for book_type in valid_book_types:
            Book(name="Game of Thrones", author="George R.R. Martin", year_published=1996, book_type=book_type, status="available")

    def test_valid_complex_author(self):
        authors = ["John Doe", "Jane Smith-Jones", "Dr. Alan Johnson, PhD"]
        for author in authors:
            Book(name="Example Book", author=author, year_published=2000, book_type="Fiction", status="available")

# Testy niepoprawnych danych

class TestBookInvalidData(unittest.TestCase):
    def test_invalid_status_format(self):
        with self.assertRaises(ValueError):
            Book(name="Invalid Book", author="Invalid Author", year_published=2022, book_type="Sci-Fi", status="invalid")

    def test_negative_year_published(self):
        with self.assertRaises(ValueError):
            Book(name="Negative Year Book", author="Author Name", year_published=-100, book_type="Mystery", status="available")

    def test_extremely_short_book_type_name(self):
        with self.assertRaises(ValueError):
            Book(name="Short Genre Book", author="Author X", year_published=2010, book_type="A", status="available")

    def test_invalid_name_characters(self):
        invalid_names = ["abcdefghijk", "1234!67890x", "0000000000?"]
        for name in invalid_names:
            with self.assertRaises(ValueError):
                Book(name=name, author="Invalid Author", year_published=2021, book_type="Thriller", status="available")

    def test_invalid_email_as_author(self):
        with self.assertRaises(ValueError):
            Book(name="Email Author Book", author="john.doe@email.com", year_published=2015, book_type="Drama", status="available")

# Testy wstrzyknięć

class TestBookSQLAndJavaScriptInjections(unittest.TestCase):
    def test_extended_sql_injection(self):
        attack_vectors = ["' OR '1'='1'; --", "' UNION SELECT * FROM users; --"]
        for vector in attack_vectors:
            with self.assertRaises(ValueError):
                Book(name=vector, author="Injected Author", year_published=2023, book_type="Suspense", status="available")

    def test_javascript_injection_variants(self):
        scripts = ["<script>alert('XSS')</script>", "<script>console.log('Hack')</script>"]
        for script in scripts:
            with self.assertRaises(ValueError):
                Book(name="JavaScript Book", author=script, year_published=2024, book_type="Sci-Fi", status="available")

# Testy ekstremalnych danych

class TestBookExtremeData(unittest.TestCase):
    def test_extremely_long_name(self):
        with self.assertRaises(ValueError):
            Book(name="A" * 1000, author="Long Author", year_published=2018, book_type="Adventure", status="available")

    def test_excessive_year_published_number(self):
        with self.assertRaises(ValueError):
            Book(name="High Year Published Book", author="Author Z", year_published=10000, book_type="Mystery", status="available")

if __name__ == '__main__':
    unittest.main()