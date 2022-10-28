def solution(id_pw, db):
    answer = {k:v for k,v in db}
    _id, _pw = id_pw
    pw = answer.get(_id)
    if not pw:
        return 'fail'
    if pw != _pw:
         return 'wrong pw'
    return 'login'