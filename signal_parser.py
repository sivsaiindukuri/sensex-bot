import re
from expiry_utils import parse_expiry

def parse_signal(text: str):
    if "SENSEX" not in text:
        return None

    strike = int(re.search(r"(\d{5})PE", text).group(1))
    sl = int(re.search(r"STOPLOSS\s+(\d+)", text).group(1))
    targets = list(map(int, re.findall(r"\d+", text.split("TARGETS")[1])))
    expiry_raw = re.search(r"(\d+\w+\s+\w+)", text).group(1)
    expiry = parse_expiry(expiry_raw)

    return {
        "strike": strike,
        "sl": sl,
        "target": targets[0],
        "expiry": expiry,
        "option_type": "PE"
    }