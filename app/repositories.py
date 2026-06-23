from sqlalchemy.orm import Session
from app.models import User, IncidentReport
from app.schemas import UserCreate, IncidentReportCreate

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, user: UserCreate) -> User:
        db_user = User(email=user.email, hashed_password=user.password)
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def get(self, user_id: int) -> User:
        return self.db.query(User).filter(User.id == user_id, User.isDeleted == False).first()

class IncidentReportRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, report: IncidentReportCreate) -> IncidentReport:
        db_report = IncidentReport(**report.dict())
        self.db.add(db_report)
        self.db.commit()
        self.db.refresh(db_report)
        return db_report

    def get(self, report_id: int) -> IncidentReport:
        return self.db.query(IncidentReport).filter(IncidentReport.id == report_id, IncidentReport.isDeleted == False).first()