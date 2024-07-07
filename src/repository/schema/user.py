from sqlalchemy import Column, String
from repository.schema import Base
from sqlalchemy.orm import relationship, Mapped
from repository.schema.challenge import Instance


class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, index=True)
    slug = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    display_name = Column(String)

    joined_instances: Mapped["Instance"] = relationship(
        "Instance", secondary="joins", back_populates="players", lazy="select"
    )

    created_instances: Mapped["Instance"] = relationship(
        "Instance", back_populates="creator", lazy="select"
    )
