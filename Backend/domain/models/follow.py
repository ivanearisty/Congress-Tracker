from domain.models import db

class Follow(db.Model):
    follower_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)

    def __init__(self, follower_id):
        self.follower_id = follower_id

# Temporary code, may not be implemented in the future
class FollowBill(Follow):
    bill_id = db.Column(db.Integer, db.ForeignKey('bill.id'), primary_key=True)

    def __init__(self, follower_id, bill_id):
        super().__init__(follower_id)
        self.bill_id = bill_id

class FollowCongressMember(Follow):
    congress_member_id = db.Column(db.Integer, db.ForeignKey('congress_member.id'), primary_key=True)

    def __init__(self, follower_id, congress_member_id):
        super().__init__(follower_id)
        self.congress_member_id = congress_member_id