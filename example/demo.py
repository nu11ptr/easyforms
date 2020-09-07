import easyforms


def login(username, password):
    if username == "admin" and password == "password":
        return ["ALL"]

    return []


def submit_sym(data, progress):
    progress(f"Symbol '{data['sym']}'' successfully added.", 100)
    return True


def sym_is_valid(sym, values):
    if "sym_type" in values:
        if sym == "AAPL" and "sym_type" == "Stock":
            return ""
        elif sym == "ES" and "sym_type" == "Future":
            return ""
    else:
        return "Symbol type must be chosen before symbol can be determined valid"

    return "Invalid or unknown symbol"


def add_symbols():
    sym = easyforms.DataField(
        label="Symbol",
        desc="Enter a valid market symbol",
        name="sym",
        validate=sym_is_valid,
    )
    sym_type = easyforms.DataField(
        label="Symbol Type",
        desc="Enter a valid symbol type",
        name="sym_type",
        default="Stock",
        control=easyforms.Control.RADIO_BUTTONS,
        options=["Stock", "Future", "ETF", "Forex", "Mutual Fund"],
    )
    futures_mo = easyforms.DataField(
        label="Futures Month",
        name="futures_mo",
        desc="Enter futures month in <letter<2-digit-year> format",
        validate=(
            r"^[FfGgHhJjKkMmNnQqUuVvXxZz]\d{2}$",
            "Invalid futures month - must be in form: <letter><2-digit-year>",
        ),
    )

    return easyforms.Page(
        section="Market Data",
        title="Add Symbols",
        fields=[sym, sym_type, futures_mo],
        submit_func=submit_sym,
        group="ALL",
    )


if __name__ == "__main__":
    easyforms.run(login_func=login, pages=[add_symbols()])
