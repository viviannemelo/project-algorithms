from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    # with pytest.raises(TypeError):
    #     encrypt_message("message", "key")

    with pytest.raises(TypeError):
        encrypt_message(123, "1")

    assert encrypt_message("Teste", -5) == "etseT"

    assert encrypt_message("Algoritmos", 3) == "glA_somtiro"

    assert encrypt_message("vivianne", 4) == "enna_iviv"
