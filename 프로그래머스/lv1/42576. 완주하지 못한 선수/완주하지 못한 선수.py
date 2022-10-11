def solution(participants, completion):
    marthoners = Marthoners()
    for participant in participants:
        marthoners.add(participant)
    for participant in completion:
        marthoners.remove(participant)
    return marthoners.remain

class Marthoners:
    def __init__(self):
        self._dict = {}
    def add(self,name):
        if name in self._dict:
            self._dict[name] += 1
        else:
            self._dict[name] = 1
    def remove(self, name):
        if self._dict[name] == 1:
            del self._dict[name]
        else:
            self._dict[name]-=1
    @property
    def remain(self):
        return list(self._dict.keys())[0]