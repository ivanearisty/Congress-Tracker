from domain.models.follow import Follow
from domain.models.bill import Bill
from domain.models.congress_member import CongressMember
from domain.models import db

class FollowType:
    BILL = "bill"
    CONGRESS_MEMBER = "member"



class FollowController:
    @staticmethod
    def get_followee(followee_id, follow_type):
        match follow_type:
            case FollowType.BILL:
                return Bill.query.get(followee_id)
            case FollowType.CONGRESS_MEMBER:
                return CongressMember.query.get(followee_id)
            case _:
                return None
    @staticmethod
    def follow(follower_id, followee_id, follow_type):

        followee = FollowController.get_followee(followee_id, follow_type)
        if followee is None:
            return {"message": "Invalid follow type"}, 400

        follow = Follow.query.filter_by(follower_id=follower_id, followee_id=followee).first()
        if follow:
            return {"message": "Already following"}, 400

        new_follow = Follow(follower_id=follower_id, followee_id=followee_id)
        db.session.add(new_follow)
        db.session.commit()
        return {"message": "Followed successfully"}, 200

    @staticmethod
    def unfollow(follower_id, followee_id, follow_type):
        followee = FollowController.get_followee(followee_id, follow_type)
        if followee is None:
            return {"message": "Invalid follow type"}, 400

        follow = Follow.query.filter_by(follower_id=follower_id, followee_id=followee).first()
        if follow:
            return {"message": "Already following"}, 400

        if follow:
            db.session.delete(follow)
            db.session.commit()
            return {"message": "Unfollowed successfully"}, 200
        return {"message": "Follow relationship not found"}, 404
