from .utils import db
# from sqlalchemy import Column,ForeignKey

class Category(db.Model):

    id = db.Column("id", db.Integer, primary_key=True, autoincrement=True)
    name = db.Column("name", db.String(50), nullable=False, unique=True)

    def __repr__(self):
        return self.name

class Car(db.Model):

    id = db.Column("id", db.Integer, primary_key=True, autoincrement=True)
    name = db.Column("name", db.String(50), nullable=False, unique=True)
    # 定义外键
    cid = db.Column("cid", db.ForeignKey("category.id", ondelete="CASCADE"), nullable=False)
    category = db.relationship("Category", backref="cars")

    def __repr__(self):
        return self.name
