from typing import List

from sqlalchemy import Column, String, Integer, ForeignKey, Table
from sqlalchemy.orm import Mapped, Relationship

from pensieve_web import db


class UnitRoles(db.Model):
    __tablename__ = 'unit_roles'

    user_id: Mapped[str] = Column(ForeignKey("users.user_id"), primary_key=True)
    unit_id: Mapped[str] = Column(ForeignKey("units.unit_id"), primary_key=True)
    role: Mapped[str] = Column(String)

    unit: Mapped["Unit"] = Relationship(back_populates="user")
    user: Mapped["User"] = Relationship(back_populates="unit")


class User(db.Model):
    __tablename__ = 'users'

    user_id: Mapped[str] = Column(String, primary_key=True)
    password_hash: Mapped[str] = Column(String)
    role: Mapped[str] = Column(String)

    unit: Mapped[List["UnitRoles"]] = Relationship()

class Unit(db.Model):
    __tablename__ = 'units'

    unit_id: Mapped[int] = Column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = Column(String)

    user: Mapped[List["UnitRoles"]] = Relationship()
    assignments: Mapped[List["Assignment"]] = Relationship(back_populates="unit")


class Assignment(db.Model):
    __tablename__ = 'assignments'

    assignment_id: Mapped[int] = Column(Integer, primary_key=True, autoincrement=True)
    unit_id: Mapped[int] = Column(ForeignKey("units.unit_id"))
    name: Mapped[str] = Column(String)

    unit: Mapped["Unit"] = Relationship(back_populates="assignments")

