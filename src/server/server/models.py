from server import db
from datetime import datetime

class House(db.Model):
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    lianjiaId = db.Column(db.String(20), index=True)
    title = db.Column(db.String(50), index=True)
    follower_num = db.Column(db.Integer,index=True)
    total_price = db.Column(db.Integer,index=True)
    area = db.Column(db.Float,index=True)
    avg_price = db.Column(db.Integer,index=True)
    directions = db.Column(db.String(20),index=True)
    floor = db.Column(db.String(4),index=True)
    year = db.Column(db.Integer,index=True)
    decoration = db.Column(db.String(20),index=True)
    location = db.Column(db.String(300),index=True)
    school= db.Column(db.Integer,index=True)
    mall = db.Column(db.Integer,index=True)
    traffic = db.Column(db.Integer,index=True)
    medicine = db.Column(db.Integer,index=True)
    total_floor = db.Column(db.Integer,index=True)
    ring = db.Column(db.Integer,index=True)
    room = db.Column(db.Integer,index=True)
    parlor = db.Column(db.Integer,index=True)
    kitchen = db.Column(db.Integer,index=True)
    toilet = db.Column(db.Integer,index=True)
    district = db.Column(db.String(40),index=True)
    block = db.Column(db.String(40),index=True)
    name = db.Column(db.String(50),index=True)
    address = db.Column(db.String(50),index=True)
    des = db.Column(db.String(1000),index=True)
    community = db.Column(db.String(100),index=True)
    
    def __repr__(self):
        return '<House {}>'.format(self.lianjiaId)

    # 查询单条数据
    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    # 查询多条数据
    def dobule_to_dict(self):
        result = {}
        for key in self.__mapper__.c.keys():
            if getattr(self, key) is not None:
                result[key] = str(getattr(self, key))
            else:
                result[key] = getattr(self, key)
        return result

    #配合todict一起使用
    def to_json(all_vendors):
        v = [ven.dobule_to_dict() for ven in all_vendors]
        return v

    def to_json(self): 
        dict = self.__dict__
        if "_sa_instance_state" in dict:
            del dict["_sa_instance_state"]
        return dict







