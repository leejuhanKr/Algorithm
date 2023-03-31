def solution(name, yearning, photos):
    total_score = sum(yearning)
    score_map = dict(zip(name, yearning))
    def get_score(photo):
        return sum(score_map.get(name,0) for name in photo)
    return [get_score(photo) for photo in photos]
    