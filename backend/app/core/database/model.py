import re

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from app.core.database.consts import CAMEL_CASE_REGEX, REPLACE_PATTERN, CAMEL_CASE_ABBR_REGEX


class BaseModel(DeclarativeBase):
    __abstract__: bool = True

    id: Mapped[int] = mapped_column(primary_key=True)

    def to_dict(self) -> dict:
        return {
            column.name: getattr(self, column.name)
            for column in self.__table__.columns
        }

    @classmethod
    def __tablename__(cls) -> str:
        s1: str = re.sub(CAMEL_CASE_REGEX, REPLACE_PATTERN, cls.__name__)
        s2: str = re.sub(CAMEL_CASE_ABBR_REGEX, REPLACE_PATTERN, s1)
        return s2.lower()

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} {self.id}>"
