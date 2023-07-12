from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    with pytest.raises(TypeError):
        encrypt_message("message", "key")

    with pytest.raises(TypeError):
        encrypt_message("Teste", 3)

    assert encrypt_message("Teste", 0) == "etseT"

    assert encrypt_message("Algoritmos", 2) == "somtirog_lA"

    assert encrypt_message("vivianne", 4) == "enna_iviv"

    assert encrypt_message("", 3) == ""
