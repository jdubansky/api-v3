from . import Base
from sqlalchemy import Column, String, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship


class Jurisdiction(Base):
    __tablename__ = "opencivicdata_jurisdiction"

    id = Column(String, primary_key=True, index=True)
    name = Column(String)
    url = Column(String)
    classification = Column(String, index=True)
    division_id = Column(String)

    organizations = relationship(
        "Organization",
        primaryjoin="""and_(
        Jurisdiction.id == Organization.jurisdiction_id,
        Organization.classification.in_(('upper', 'lower', 'legislature', 'executive'))
        )"""
    )


class Organization(Base):
    __tablename__ = "opencivicdata_organization"

    id = Column(String, primary_key=True, index=True)
    name = Column(String)
    classification = Column(String)

    jurisdiction_id = Column(String, ForeignKey(Jurisdiction.id))
    jurisdiction = relationship("Jurisdiction")


class Person(Base):
    __tablename__ = "opencivicdata_person"

    id = Column(String, primary_key=True, index=True)
    name = Column(String, index=True)
    family_name = Column(String)
    given_name = Column(String)
    image = Column(String)
    gender = Column(String)
    summary = Column(String)
    biography = Column(String)
    birth_date = Column(String)
    death_date = Column(String)
    party = Column("primary_party", String)
    current_role = Column(JSONB)
    created_at = Column(DateTime(timezone=True))
    updated_at = Column(DateTime(timezone=True))
    extras = Column(JSONB)
    jurisdiction_id = Column("current_jurisdiction_id", String)
