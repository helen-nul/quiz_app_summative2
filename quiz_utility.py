import re

def clean_name(name):
    return name.strip().title()

def presence_check(name: str) -> bool:
    return bool(name)

def length_check(name: str) -> bool:
    return 2 <= len(name) <= 50

def character_check(name: str) -> bool:
    return not re.search(r"\d", name)