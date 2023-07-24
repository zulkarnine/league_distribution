# Program to distribute sorted teams into N groups.

import random
import argparse
import itertools


def distribute_teams(team_count: int, group_count: int, randomize_order_in_group=False, teams=[], verbose=False):
    # Team number starts from 1 (not 0).Ï
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
            if group[j] is int:
                print(f"{group_name}{j + 1}: team-{group[j]}")
            else:
                print(f"{group_name}{j + 1}: {group[j]}")
        print()


def make_parallel_schedule(matches, parallelism):
    parallel_schedule = [[] for _ in range(parallelism)]
    picked_matches = set()
    for i in range(len(matches)):
        already_picked_for_current_slot = set()
        for j in range(parallelism):
            found_match = None
            for match in matches:
                if match in picked_matches or match[0] in already_picked_for_current_slot or match[
                    1] in already_picked_for_current_slot:
                    continue
                found_match = match
                break
            parallel_schedule[j].append(found_match)
            if found_match is None:
                continue
            else:
                picked_matches.add(found_match)
            already_picked_for_current_slot.add(found_match[0])
            already_picked_for_current_slot.add(found_match[1])
        if len(picked_matches) == len(matches):
            break
    return parallel_schedule


def get_match(match):
    if match is None:
        return "NA"
    return f"{match[0]} vs {match[1]}"


def get_max_match_name_len(matches):
    max_len = 0
    for match in matches:
        match_string_len = len(get_match(match))
        if match_string_len > max_len:
            max_len = match_string_len
    return max_len


def print_group_stage_matches(groups, parallelism=1):
    print()
    for i in range(len(groups)):
        group_name = chr(ord('A') + i)
        print(f"Group {group_name} matches:")
        group = groups[i]
        matches = []
        for match in itertools.combinations(group, 2):
            matches.append(match)

        max_match_name_len = get_max_match_name_len(matches)
        if parallelism <= 1:
            for match in matches:
                print(get_match(match))
        else:
            parallel_matches = make_parallel_schedule(matches, parallelism)
            slot_count = len(parallel_matches[0])
            for j in range(slot_count):
                print(f"Slot-{j + 1:2}: ", end="")
                for k in range(parallelism):
                    match_str = get_match(parallel_matches[k][j])
                    print(f"{match_str}", end=" " * (max_match_name_len - len(match_str) + 5))
                    print(" : ", end="")
                print()
        print()


if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser()

    arg_parser.add_argument("-g", "--group", type=int, help="Number of groups.", required=True)

    team_group = arg_parser.add_mutually_exclusive_group(required=True)
    team_group.add_argument("-t", "--team_count", type=int, help="Number of teams.")
    team_group.add_argument("-f", "--teams_file", type=str, help="File with teams (sorted).")

    arg_parser.add_argument("-p", "--parallelism", type=int, help="Number of matches that may run in parallel.",
                            default=1)
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
    print_group_stage_matches(groups, args.parallelism)
