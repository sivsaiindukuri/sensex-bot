import datetime
import re

MONTHS = {
    "JANUARY":"JAN","FEBRUARY":"FEB","MARCH":"MAR","APRIL":"APR",
    "MAY":"MAY","JUNE":"JUN","JULY":"JUL","AUGUST":"AUG",
    "SEPTEMBER":"SEP","OCTOBER":"OCT","NOVEMBER":"NOV","DECEMBER":"DEC"
}

def parse_expiry(text: str) -> str:
    day = int(re.search(r"\d+", text).group())
    month_word = text.split()[-1].upper()
    month = MONTHS[month_word]
    year = datetime.datetime.now().year % 100
    return f"{day:02d}{month}{year}"