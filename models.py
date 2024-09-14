from uuid import uuid4
from datetime import datetime, timezone
from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from database import Base


class SQLAlchemyCategory(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique=True, index=True)

    transactions = relationship("Transaction", back_populates="category")


class SQLAlchemyUserAccount(Base):
    __tablename__ = 'user_accounts'
    id = Column(Integer, primary_key=True, index=True)
    number = Column(String(8), unique=True, index=True)
    type = Column(String)
    name = Column(String)
    balance = Column(Float, default=0)

    transactions = relationship("Transaction", back_populates="user_account")


class SQLAlchemyTransaction(Base):
    __tablename__ = 'transactions'
    id = Column(Integer, primary_key=True, index=True)
    number_id = Column(Integer, ForeignKey('user_accounts.id'))
    type = Column(String)
    category_id = Column(Integer, ForeignKey('categories.id'))
    date = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    transaction_id = Column(UUID(as_uuid=True), unique=True, default=lambda: uuid4())
    amount = Column(Float)

    user_account = relationship("UserAccount", back_populates="transactions")
    category = relationship("Category", back_populates="transactions")
