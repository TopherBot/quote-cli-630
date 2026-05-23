import argparse
from quote_cli import __main__ as cli


def test_random_quote_returns_string():
    quote = cli.get_random_quote()
    assert isinstance(quote, str) and len(quote) > 0


def test_list_quotes_length():
    quotes = cli.list_quotes()
    assert len(quotes) == 5


def test_argparse_list_flag(monkeypatch, capsys):
    # Simulate ``quote-cli --list``
    monkeypatch.setattr(argparse.ArgumentParser, "parse_args", lambda self: argparse.Namespace(list=True))
    cli.main()
    captured = capsys.readouterr()
    assert "1." in captured.out and "5." in captured.out
