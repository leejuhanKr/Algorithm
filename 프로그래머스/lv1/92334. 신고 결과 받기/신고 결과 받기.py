from collections import defaultdict


def solution(id_list, report, k):
    reported_data = defaultdict(set)
    report_data = defaultdict(int)

    report = [i.split() for i in report]

    for i, j in report:
        reported_data[j].add(i)

    for i, j in reported_data.items():
        if len(j) < k:
            continue
        for r in j:
            report_data[r] += 1

    return [report_data[i] for i in id_list]