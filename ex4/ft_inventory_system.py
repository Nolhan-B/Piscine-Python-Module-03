import sys

def main() -> None:
    """Analyse simple d'un inventaire."""
    print("=== Inventory System Analysis ===")

    inventory: dict = dict()

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
                "type": "unknown",
                "quantity": int(quantity)
            }
        })

    total_items = 0
    for item in inventory.values():
        total_items += item.get("quantity")

    print(f"Total items in inventory: {total_items}")
    print(f"Unique item types: {len(inventory)}")

    print("\n=== Current Inventory ===")
    for name, data in inventory.items():
        percent = (data.get("quantity") / total_items) * 100
        data.update({"value": round(percent, 1)})
        print(f"{name}: {data.get('quantity')} units ({data.get('value')}%)")

if __name__ == "__main__":
    main()
