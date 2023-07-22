# Program to distribute sorted teams into N groups.

import random
import argparse
import itertools


def distribute_teams(team_count, group_count, randomize_order_in_group=False, teams=[], verbose=False):
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

    # Randomize order within group.
    if randomize_order_in_group:
        for group in groups:
            random.shuffle(group)
        if verbose:
            print("groups (after randomization): ", groups)
    return groups


def print_groups(groups):
    print()
    for i in range(len(groups)):
        group_name = chr(ord('A') + i)
        print(f"Group: {group_name}")
        group = groups[i]
        for j in range(len(group)):
            print(f"{group_name}{j + 1}: team-{group[j]}")
        print()


def print_group_stage_matches(groups):
    print()
    for i in range(len(groups)):
        group_name = chr(ord('A') + i)
        print(f"Group {group_name} matches:")
        group = groups[i]
        for match in itertools.combinations(group, 2):
            print(f"{match[0]} vs {match[1]}")
        print()


if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser()

    arg_parser.add_argument("-g", "--group", type=int, help="Number of groups.", required=True)

    team_group = arg_parser.add_mutually_exclusive_group(required=True)
    team_group.add_argument("-t", "--team_count", type=int, help="Number of teams.")
    team_group.add_argument("-f", "--teams_file", type=str, help="File with teams (sorted).")

    arg_parser.add_argument("-v", "--verbose", action="store_true", help="Shows verbose messages.")
    arg_parser.add_argument("-r", "--randomize_order_in_group", action="store_true",
                            help="Randomize order within group.")
    args = arg_parser.parse_args()

    group_count = args.group
    teams_file = args.teams_file  # Reads teams from file if provided.

    teams = []
    if teams_file:
        with open(teams_file, 'r') as f:
            teams = [line.strip() for line in f.readlines()]

    team_count = len(teams) if teams else args.team_count

    print(f"Generating league distribution for {team_count} teams in {group_count} groups")
    groups = distribute_teams(team_count, group_count, args.randomize_order_in_group, teams, verbose=args.verbose)
    print_groups(groups)
    print_group_stage_matches(groups)
