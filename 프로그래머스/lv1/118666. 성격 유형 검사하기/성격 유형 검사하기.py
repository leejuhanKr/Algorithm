def solution(survey, choices):
    data = {c: 0 for c in "RTCFJMAN"}

    for [i, j], c in zip(survey, choices):
        data[i] += c - 4

    values = ["RT", "CF", "JM", "AN"]

    return "".join([i, j][data[i] - data[j] > 0] for i, j in values)