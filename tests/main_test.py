from dab_0729.main import get_taxis, get_spark


def test_main():
    taxis = get_taxis(get_spark())
    assert taxis.count() > 5
