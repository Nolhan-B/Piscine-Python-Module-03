import sys


def sort_arr(
    array: dict[str, dict[str, int | str]]
) -> dict[str, dict[str, int | str]]:
    sorted_dict = dict()
    temp = dict()

    for key, value in array.items():
        temp.update({key: value})

    while len(temp) > 0:
        max_key = None
        max_quantity = None

        for name, data in temp.items():
            quantity = data.get("quantity")
            if max_quantity is None or quantity > max_quantity:
                max_quantity = quantity
                max_key = name

        sorted_dict.update({max_key: temp.get(max_key)})

        del temp[max_key]

    return sorted_dict


def main() -> None:
    print("=== Inventory System Analysis ===")

    inventory = dict()

    if (len(sys.argv) == 1):
        print("[ERROR] Please provide items.")
        print("[ERROR] Usage: python ft_inventory_system.py "
              "<item1:qty> <item2:qty>...")
        print("=== Program stops ===")
        return

    for arg in sys.argv[1:]:
        name, quantity = arg.split(':')
        inventory.update({
            name: {
                "quantity": int(quantity),
                "category": "Scarce" if int(quantity) <= 4 else "Moderate"
            }
        })

    total_items = 0
    for value in inventory.values():
        total_items += value.get("quantity")

    print(f"Total items in inventory: {total_items}")
    print(f"Unique item types: {len(inventory)}")

    sorted_inventory: dict = sort_arr(inventory)

    print("\n=== Current Inventory ===")
    for key, value in sorted_inventory.items():
        percent = (value.get("quantity") / total_items) * 100
        print(f"{key}: {value.get("quantity")} units ({percent:.1f}%)")

    print("\n=== Inventory Statistics ===")
    most_abd = None
    least_abd = None

    for key, value in inventory.items():
        if most_abd is None:
            most_abd = key
        elif value.get("quantity") > inventory[most_abd].get("quantity"):
            most_abd = key

        if least_abd is None:
            least_abd = key
        elif value.get("quantity") < inventory[least_abd].get("quantity"):
            least_abd = key

    print(f"Most Abundant: {most_abd} "
          f"({inventory[most_abd].get("quantity")} units)")
    print(f"Least Abundant: {least_abd} "
          f"({inventory[least_abd].get("quantity")} units)\n")

    moderate: dict = dict()
    scarce: dict = dict()

    for key, value in inventory.items():
        match (value.get("category")):
            case "Moderate":
                moderate.update({key: value.get("quantity")})
            case "Scarce":
                scarce.update({key: value.get("quantity")})
            case _:
                pass

    print(f"Moderate: {moderate}")
    print(f"Scarce: {scarce}")

    print("\n=== Management Suggestions ===")

    restock: list = []
    for name, data in inventory.items():
        if data.get("quantity") <= 1:
            restock.append(name)
    print(f"Restock needed: {restock}")

    print("\n=== Dictionary Properties Demo ===")
    keys_arr: list = []
    for key in inventory.keys():
        keys_arr.append(key)
    print(f"Dictionary keys: {keys_arr}")

    values_arr: list = []
    for value in inventory.values():
        values_arr.append(value.get("quantity"))
    print(f"Dictionary values: {values_arr}")

    item_to_find: str = "sword"
    is_in_inv: bool = item_to_find in inventory
    print(f"Sample lookup - '{item_to_find}' in inventory: {is_in_inv}")


if __name__ == "__main__":
    main()
