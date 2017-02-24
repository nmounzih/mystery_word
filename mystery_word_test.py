import mystery_word

def test_range():
    assert mystery_word.get_range('e') == (4, 6)
    assert mystery_word.get_range('m') == (6, 8)
    assert mystery_word.get_range('h') == (8, 46)


def test_guessed_all():
    assert mystery_word.guessed_all("cloud", ['c', 'o', 'l', 'u', 'd']) == True
    assert mystery_word.guessed_all("tart", ['t', 'a', 'r']) == True
    assert mystery_word.guessed_all("drink", ['d', 'i', 'n', 'k']) == None
    assert mystery_word.guessed_all("tart", ['t', 'r', 't']) == None




test_range()
test_guessed_all()
