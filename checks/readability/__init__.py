from bootcs.check import check, exists as check_exists, run
from bootcs.check import c

@check()
def exists():
    """readability.c exists"""
    check_exists("readability.c")

@check(exists)
def compiles():
    """readability.c compiles"""
    c.compile("readability.c", lcs50=True)

@check(compiles)
def single_sentence():
    """handles single sentence with multiple words"""
    run("./readability").stdin("In my younger and more vulnerable years my father gave me some advice that I've been turning over in my mind ever since.", prompt=True).stdout("Grade 7\n").exit(0)

@check(compiles)
def single_sentence_other_punctuation():
    """handles punctuation within a single sentence"""
    run("./readability").stdin("There are more things in Heaven and Earth, Horatio, than are dreamt of in your philosophy.", prompt=True).stdout("Grade 9\n").exit(0)

@check(compiles)
def single_sentence_complex():
    """handles more complex single sentence"""
    run("./readability").stdin("Alice was beginning to get very tired of sitting by her sister on the bank, and of having nothing to do: once or twice she had peeped into the book her sister was reading, but it had no pictures or conversations in it, \"and what is the use of a book,\" thought Alice \"without pictures or conversation?\"", prompt=True).stdout("Grade 8\n").exit(0)

@check(compiles)
def multiple_sentences():
    """handles multiple sentences"""
    run("./readability").stdin("Harry Potter was a highly unusual boy in many ways. For one thing, he hated the summer holidays more than any other time of year. For another, he really wanted to do his homework, but was forced to do it in secret, in the dead of the night. And he also happened to be a wizard.", prompt=True).stdout("Grade 5\n").exit(0)

@check(compiles)
def multiple_sentences_complex():
    """handles multiple more complex sentences"""
    run("./readability").stdin("It was a bright cold day in April, and the clocks were striking thirteen. Winston Smith, his chin nuzzled into his breast in an effort to escape the vile wind, slipped quickly through the glass doors of Victory Mansions, though not quickly enough to prevent a swirl of gritty dust from entering along with him.", prompt=True).stdout("Grade 10\n").exit(0)

@check(compiles)
def longer_passages():
    """handles longer passages"""
    run("./readability").stdin("When he was nearly thirteen, my brother Jem got his arm badly broken at the elbow. When it healed, and Jem's fears of never being able to play football were assuaged, he was seldom self-conscious about his injury. His left arm was somewhat shorter than his right; when he stood or walked, the back of his hand was at right angles to his body, his thumb parallel to his thigh.", prompt=True).stdout("Grade 8\n").exit(0)

@check(compiles)
def exclamation_marks():
    """handles multiple sentences with different punctuation"""
    run("./readability").stdin("Congratulations! Today is your day. You're off to Great Places! You're off and away!", prompt=True).stdout("Grade 3\n").exit(0)

@check(compiles)
def question_marks():
    """handles questions in passage"""
    run("./readability").stdin("Would you like them here or there? I would not like them here or there. I would not like them anywhere.", prompt=True).stdout("Grade 2\n").exit(0)

@check(compiles)
def before1():
    """handles reading level before Grade 1"""
    run("./readability").stdin("One fish. Two fish. Red fish. Blue fish.", prompt=True).stdout("Before Grade 1\n").exit(0)

@check(compiles)
def grade16plus():
    """handles reading level at Grade 16+"""
    run("./readability").stdin("A large class of computational problems involve the determination of properties of graphs, digraphs, integers, arrays of integers, finite families of finite sets, boolean formulas and elements of other countable domains.", prompt=True).stdout("Grade 16+\n", regex=False).exit(0)
