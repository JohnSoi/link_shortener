"""Константы для работы с базой данных."""

# Регулярное выражение для преобразования CamelCase в snake_case
CAMEL_CASE_REGEX: str = r"(.)([A-Z][a-z]+)"
# Регулярное выражение для преобразования аббревиатур CamelCase в snake_case
CAMEL_CASE_ABBR_REGEX: str = r"([a-z0-9])([A-Z])"
# Паттерн для замены CamelCase на snake_case
REPLACE_PATTERN: str = r"\1_\2"
