import json

def read_user_data(file_path):
    try:
        with open(file_path, 'r') as file:
            user_data = json.load(file)
        print("Användardata läst från fil.")
        return user_data
    except FileNotFoundError:
        print("Ingen användardata tillgänglig.")
        return {}
    except json.JSONDecodeError:
        print("Felaktigt filformat.")
        exit()

def read_groups(file_path):
    try:
        with open(file_path, 'r') as file:
            groups = json.load(file)
        print("Grupper:")
        for group in groups:
            print(f"* {group}")
        return groups
    except FileNotFoundError:
        print("Fil saknas")
        exit()
    except json.JSONDecodeError:
        print("Felaktigt filformat.")
        exit()

def get_group_members(groups, group_name):
    if group_name not in groups:
        print("Felaktig grupp")
        exit()
    members = groups[group_name]
    return members

def main():
    user_data_file = "game_of_thrones.json"
    groups_file = "houses.json"

    user_data = read_user_data(user_data_file)
    groups = read_groups(groups_file)

    group_name = input("Välj en grupp: ")
    members = get_group_members(groups, group_name)

    for member_id in members:
        if member_id in user_data:
            print(user_data[member_id])
        else:
            print(member_id)

if __name__ == "__main__":
    main()
