from mypackage import myModule

def test_top_n():
    """
    make sure top_n works correctly
    """

    assert myModule.top_n([8, 4, 3, 2, 7], 3) == [8, 7, 4], "incorrect"
    assert myModule.top_n([5, 9, 1, 6, 12, 19], 3) == [19, 12, 9], "incorrect"
    assert myModule.top_n([800, 400, 300, 200, 700], 3) == [800, 700, 400], "incorrect"