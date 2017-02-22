def write_to_file1(file, sentences):
    """
    (file open for writing, list of str) -> NoneType

    Write each sentence from sentences to file, one per line.

    Precondition: The sentences contain no newlines.
    """
    for s in sentences:
        file.write(s)
        file.write('\n')

to_file = open('write_to_file1.txt', 'w')
some_sentences = ["Sentence the first.", "Sentence the second.", "Sentence the third."]
write_to_file1(to_file, some_sentences)


def write_to_file2(file, sentences):
    """
    (file open for writing, list of str) -> NoneType

    Write each sentence from sentences to file, one per line.

    Precondition: The sentences contain no newlines.
    """
    for s in sentences:
        file.write(s + '\n')

to_file = open('write_to_file2.txt', 'w')
some_sentences = ["Sentence the first.", "Sentence the second.", "Sentence the third."]
write_to_file2(to_file, some_sentences)
