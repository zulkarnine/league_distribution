# Program to distribute sorted teams into N groups.

import random
import argparse


def distribute_teams(team_count, group_count, teams=[], verbose=False):
    # Team number starts from 1 (not 0).
    if not teams:
        teams = [i for i in range(1, team_count + 1)]
    else:
        team_count = len(teams)
    if verbose:
        print("teams: ", teams)

    # Create ranked buckets to distribute to n different groups.
    bucket_start = 0
    ranked_buckets = []
    while bucket_start < team_count:
        ranked_buckets.append(teams[bucket_start: bucket_start + group_count])
        bucket_start += group_count
    if verbose:
        print("ranked buckets: ", ranked_buckets)

    # randomize ranked buckets.
    for bucket in ranked_buckets:
        random.shuffle(bucket)
    if verbose:
        print("shuffled ranked buckets:", ranked_buckets)

    # Then distribute them to groups.
    groups = [[] for _ in range(group_count)]
    for bucket in ranked_buckets:
        for i in range(len(bucket)):
            groups[i].append(bucket[i])
    if verbose:
        print("groups: ", groups)
    return groups


def print_groups(groups, randomize_order_in_group):
    print()
    for i in range(len(groups)):
        group_name = chr(ord('A') + i)
        print(f"Group: {group_name}")
        group = groups[i]
        if randomize_order_in_group:
            random.shuffle(group)
        for j in range(len(group)):
            print(f"{group_name}{j + 1}: team-{group[j]}")
        print()


if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser()

    team_group = arg_parser.add_mutually_exclusive_group(required=True)
    team_group.add_argument("-t", "--team_count", type=int, help="Number of teams.")
    team_group.add_argument("-f", "--teams_file", type=str, help="File with teams (sorted).")

    arg_parser.add_argument("-g", "--group", type=int, help="Number of groups.", required=True)
    arg_parser.add_argument("-v", "--verbose", type=bool, help="Shows verbose messages.")
    arg_parser.add_argument("-r", "--randomize_order_in_group", type=bool, help="Randomize order within group.",
                            default=True)
    args = arg_parser.parse_args()

    team_count = args.team_count
    group_count = args.group
    teams_file = args.teams_file  # Reads teams from file if provided.

    teams = []
    if teams_file:
        with open(teams_file, 'r') as f:
            teams = [line.strip() for line in f.readlines()]

    print(f"Generating league distribution for {team_count} teams in {group_count} groups")
    groups = distribute_teams(team_count, group_count, teams)
    print_groups(groups, args.randomize_order_in_group)
