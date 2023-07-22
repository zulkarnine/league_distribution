# Program to distribute sorted teams into N groups.

import random


def distribute_teams(team_count, group_count):
    # Team number starts from 1 (not 0).
    teams = [i for i in range(1, team_count + 1)]
    print("teams: ", teams)

    # Create ranked buckets to distribute to n different groups.
    bucket_start = 0
    ranked_buckets = []
    while bucket_start < team_count:
        ranked_buckets.append(teams[bucket_start: bucket_start + group_count])
        bucket_start += group_count
    print("ranked buckets: ", ranked_buckets)

    # randomize ranked buckets.
    for bucket in ranked_buckets:
        random.shuffle(bucket)
    print("shuffled ranked buckets:", ranked_buckets)

    # Then distribute them to groups.
    groups = [[] for _ in range(group_count)]
    for bucket in ranked_buckets:
        for i in range(len(bucket)):
            groups[i].append(bucket[i])
    print("groups: ", groups)
    return groups


def print_groups(groups):
    print()
    for i in range(len(groups)):
        group_name = chr(ord('A') + i)
        print(f"Group: {group_name}")
        group = groups[i]
        for j in range(len(group)):
            print(f"{group_name}{j+1}: team-{group[j]}")
        print()


if __name__ == '__main__':
    groups = distribute_teams(16, 4)
    print_groups(groups)
