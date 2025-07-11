import re


async def is_valid_format_phone(phone_str: str) -> bool:
    pattern = r'^\+7\d{10}$'
    return bool(re.fullmatch(pattern, phone_str))