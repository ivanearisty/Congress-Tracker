from pydantic import BaseModel, HttpUrl
from datetime import date, datetime
from typing import List, Optional

# TODO: Figure out what the type enum. 
# I think that there are a few type of bills, 
# encompassing as a string could leat to some errors.
# This would also be helpful for indexing and searching.
# TODO: Figure out enum for chamber.
# TODO: Figure out enum for chamber code.
# TODO: Figure out enum for version code.
# TODO: Implement committee-report model
# TODO: Implement committee-print model
# TODO: Implement committee-meeting model
# TODO: Implement congressional-record
# TODO: Implement daily-congressional-record
# TODO: Implement bound-congressional-record
# TODO: Implement daily-congressional-record
# TODO: Implement house-communication
# TODO: Implement house-requirement
# TODO: Implement senate-communication

class LatestAction(BaseModel):
    actionDate: date
    text: str

class Bill(BaseModel):
    congress: int
    latestAction: LatestAction
    number: int
    originChamber: str
    originChamberCode: str
    title: str
    type: str
    updateDate: date
    updateDateIncludingText: datetime
    url: HttpUrl

class Amendment(BaseModel):
    congress: int
    latestAction: LatestAction
    number: int
    purpose: str
    type: str 
    url: HttpUrl

class summary(BaseModel):
    actionDate: date
    actionDesc: str
    bill: Bill
    currentChamber: str
    currentChamberCode: str
    lastSummaryUpdateDate: datetime
    text: str
    updateDate: datetime
    versionCode: str

class Session(BaseModel):
    chamber: str
    endDate: Optional[date]
    number: int
    startDate: date
    type: str

class Congress(BaseModel):
    endYear: str
    name: str
    sessions: List[Session]
    startYear: str

class Term(BaseModel):
    chamber: str
    endYear: Optional[int]
    startYear: int

class Depiction(BaseModel):
    attribution: str
    imageUrl: HttpUrl

class Member(BaseModel):
    bioguideId: str
    depiction: Optional[Depiction]
    district: Optional[str]
    name: str
    partyName: str
    state: str
    terms: List[Term]
    updateDate: datetime
    url: HttpUrl

class Subcommittee(BaseModel):
    name: str
    systemCode: str
    url: HttpUrl

class Committee(BaseModel):
    chamber: str
    committeeTypeCode: str
    name: str
    parent: Optional[str] = None
    subcommittees: List[Subcommittee]
    systemCode: str
    updateDate: datetime
    url: HttpUrl

class Hearing(BaseModel):
    chamber: str
    congress: int
    jacketNumber: int
    updateDate: datetime
    url: HttpUrl

class NominationType(BaseModel):
    isMilitary: bool

class Nomination(BaseModel):
    citation: str
    congress: int
    latestAction: LatestAction
    nominationType: NominationType
    number: int
    organization: str
    partNumber: str
    receivedDate: date
    updateDate: datetime
    url: HttpUrl

class Treaty(BaseModel):
    congressReceived: int
    congressConsidered: int
    number: int
    parts: Dict #????? I have no idea what this is supposed to be.
    suffix: Optional[str] = ""
    topic: str
    transmittedDate: datetime
    updateDate: datetime
    url: HttpUrl
