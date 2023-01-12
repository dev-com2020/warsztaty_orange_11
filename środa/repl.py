from _decimal import Decimal


def clean_decimal(text: str | None) -> Decimal | None:
    if text is None: return None
    return Decimal(
        text.replace("$", '').replace(",", "")
    )


def f_remove(str: str, chars: str) -> str:
    if chars:
        return f_remove(str.replace(chars[0], ""), chars[1:])
    return str


