from kmp import kmp


def test_kmp():
    print()
    assert kmp("ababcabcabababd", "ababd") == (10, 14)
    assert kmp("Some real text to show reliability of algo", "re") == (5, 6)
    assert kmp("Some real text to show reliability of algo", "axios") == -1


def test_exec_time():
    print()
    with open("resources/text1.txt") as file:
        text1 = file.readline()
    with open("resources/text2.txt") as file:
        text2 = file.readline()
    with open("resources/text3.txt") as file:
        text3 = file.readline()
    kmp(text1, "aaaaaaaaaaaaaaaaaaaaaaa")
    kmp(text2, "abababababababababdf")
    kmp(text3, "acaacaacaacadf")
    kmp(text3, "xxxxxxxxxxxxxx")
