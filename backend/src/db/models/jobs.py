from datetime import datetime

from sqlalchemy import Column, String, ForeignKey, Integer, Boolean, Text, DateTime
from sqlalchemy.orm import relationship

from db.base import Base
from db.models.users import association_table


class Job(Base):
    __tablename__ = "jobs"
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True, index=True)
    email = Column(String)
    user_id = Column(ForeignKey('users.id', ondelete="CASCADE"), nullable=False)
    title = Column(String, index=True)
    description = Column(Text)
    is_active = Column(Boolean, default=False)
    created_at = Column(DateTime, index=True, default=datetime.utcnow)
    updated_at = Column(DateTime, index=True, default=datetime.utcnow)
    salary_from = Column(Integer)
    salary_to = Column(Integer)

    appliers = relationship("User", secondary=association_table, back_populates="vacancies")

    user = relationship("User")




