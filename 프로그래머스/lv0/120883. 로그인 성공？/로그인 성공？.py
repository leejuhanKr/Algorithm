def solution(id_pw, db):
    _id, _pw = id_pw
    pw = dict(db).get(_id)
    if not pw:
        return 'fail'
    if pw != _pw:
         return 'wrong pw'
    return 'login'