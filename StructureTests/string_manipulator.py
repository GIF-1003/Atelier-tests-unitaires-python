class EmptyStringException(Exception):
    def __init__(self, message="The string is empty"):
        super().__init__(message)

class StringManipulator:
    @staticmethod
    def count_characters(s):
        return len(s)

    @staticmethod
    def remove_spaces(s):
        return "".join(c for c in s if not c.isspace())

    @staticmethod
    def convert_to_lowercase(s):
        return s.lower()

    @staticmethod
    def count_number_of_words(s):
        if not s:
            raise EmptyStringException()

        word_count = 0
        inside_the_word = False

        for c in s:
            if c.isalnum():
                if not inside_the_word:
                    word_count += 1
                    inside_the_word = True
            else:
                inside_the_word = False

        return word_count
