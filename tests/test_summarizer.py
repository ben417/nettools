from summarizer import summarizer
import ipaddress


def test_summarizer_1():
    output = summarizer(["1.1.1.1/32"], 1)
    assert [str(n) for n in output] == ["1.1.1.1/32"]


def test_summarizer_2():
    output = summarizer(["1.1.1.0/32", "1.1.1.1/32"], 1)
    assert [str(n) for n in output] == ["1.1.1.0/31"]
