import pytest

from StructureTests.string_manipulator import StringManipulator, EmptyStringException

class TestStringManipulator:
    EMPTY_STRING = ""
    NON_EMPTY_STRING = "Hello, World!"
    STRING_WITH_SPACES = "Hello, World!"
    STRING_WITHOUT_SPACES = "Hello,World!"
    STRING_IN_UPPERCASE = "HELLO, WORLD!"
    STRING_IN_LOWERCASE = "hello, world!"
    STRING_WITH_SPECIAL_CHARACTERS = "Hello,;World!"

    def setup(self):
        self.string_manipulator = StringManipulator()

    def test_given_empty_string_when_count_characters_then_result_is_zero(self):
        # Given
        str = self.EMPTY_STRING

        # When
        num_characters = self.string_manipulator.count_characters(str)

        # Then
        assert num_characters == 0

    def test_given_non_empty_string_when_count_characters_then_result_is_correct(self):
        # Given
        str = self.NON_EMPTY_STRING

        # When
        num_characters = self.string_manipulator.count_characters(str)

        # Then
        assert num_characters == 13

    def test_given_string_with_spaces_when_remove_spaces_then_spaces_are_removed(self):
        # Given
        str = self.STRING_WITH_SPACES

        # When
        result = self.string_manipulator.remove_spaces(str)

        # Then
        assert result == self.STRING_WITHOUT_SPACES

    def test_given_string_without_spaces_when_remove_spaces_then_string_remains_unchanged(self):
        # Given
        str = self.STRING_WITHOUT_SPACES

        # When
        result = self.string_manipulator.remove_spaces(str)

        # Then
        assert result == self.STRING_WITHOUT_SPACES

    def test_given_string_with_uppercase_letters_when_convert_to_lowercase_then_string_is_converted_to_lowercase(self):
        # Given
        str = self.STRING_IN_UPPERCASE

        # When
        result = self.string_manipulator.convert_to_lowercase(str)

        # Then
        assert result == self.STRING_IN_LOWERCASE

    def test_given_string_in_lowercase_when_convert_to_lowercase_then_string_remains_unchanged(self):
        # Given
        str = self.STRING_IN_LOWERCASE

        # When
        result = self.string_manipulator.convert_to_lowercase(str)

        # Then
        assert result == self.STRING_IN_LOWERCASE

    def test_given_empty_string_when_count_number_of_words_then_exception_is_thrown(self):
        # Given
        str = self.EMPTY_STRING

        # When + Then
        with pytest.raises(EmptyStringException):
            self.string_manipulator.count_number_of_words(str)

    def test_given_non_empty_string_when_count_number_of_words_then_count_is_one(self):
        # Given
        str = self.NON_EMPTY_STRING

        # When
        word_count = self.string_manipulator.count_number_of_words(str)

        # Then
        assert word_count == 2

    def test_given_string_with_words_separated_by_spaces_when_count_number_of_words_then_count_is_correct(self):
        # Given
        str = self.STRING_WITH_SPACES

        # When
        word_count = self.string_manipulator.count_number_of_words(str)

        # Then
        assert word_count == 2

    def test_given_string_with_words_separated_by_special_characters_when_count_number_of_words_then_count_is_correct(self):
        # Given
        str = self.STRING_WITH_SPECIAL_CHARACTERS

        # When
        word_count = self.string_manipulator.count_number_of_words(str)

        # Then
        assert word_count == 2
