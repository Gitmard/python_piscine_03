#!/usr/bin/env python3

class Inventory:
    __items: dict[str, dict[str, int]]

    def __init__(self):
        self.__items = {
            "scarse": {},
            "moderate": {},
            "abundant": {}
        }

    def get_items(self) -> dict[str, dict[str, int]]:
        # Return a copy of the items dict
        return dict(self.__items)

    def get_item_category(self, name: str) -> str | None:
        for key, value in self.__items.items():
            for item in value.keys():
                if item == name:
                    return key
        return None

    def get_category_for_amount(self, amount: int) -> str | None:
        if amount <= 0:
            return None
        if amount < 5:
            return "scarse"
        if amount < 11:
            return "moderate"
        return "abundant"

    def __update_item(
        self,
        item: str,
        old_amount: int,
        new_amount: int,
        old_category: str | None,
        new_category: str | None
    ) -> None:
        if old_category is not None and (
            old_category != new_category
            or new_amount == 0
        ):
            old_category_dict = self.__items.get(old_category)
            assert old_category_dict is not None
            old_category_dict.pop(item)
        if new_amount == old_amount:
            return
        if new_category is not None:
            new_category_dict = self.__items.get(new_category)
            assert new_category_dict is not None
            new_category_dict.update([(item, new_amount)])

    def add_item(self, item: str, amount: int) -> None:
        if amount < 0:
            raise ValueError("Error: cannot add a negative amount of items")
        old_category = self.get_item_category(item)
        old_amount = 0
        if old_category is not None:
            old_catergory_dict = self.__items.get(old_category)
            assert old_catergory_dict is not None
            old_amount = old_catergory_dict.get(item) or 0
            assert old_amount is not None
        new_amount = old_amount + amount
        new_category = self.get_category_for_amount(new_amount)
        self.__update_item(
            item,
            old_amount,
            new_amount,
            old_category,
            new_category
        )

    def remove_item(self, item: str, amount: int) -> None:
        if amount < 0:
            raise ValueError("Error: cannot remove a negative amount of items")
        old_category = self.get_item_category(item)
        old_amount = 0
        if old_category is not None:
            old_catergory_dict = self.__items.get(old_category)
            assert old_catergory_dict is not None
            old_amount = old_catergory_dict.get(item) or 0
            assert old_amount is not None
        new_amount = old_amount - amount
        if new_amount < 0:
            raise ValueError(
                f"Error: removing {amount} from item {item} with " +
                f"current amount {old_amount} " +
                "would result in a negative amount"
            )
        new_category = self.get_category_for_amount(new_amount)
        self.__update_item(
            item,
            old_amount,
            new_amount,
            old_category,
            new_category
        )

    def get_items_flat(self) -> dict[str, int]:
        flat_items: dict[str, int] = dict()
        for category in self.__items.values():
            for item, amount in category.items():
                flat_items.update([(item, amount)])
        return flat_items

    def get_unique_items(self) -> list[str]:
        unique_items: list[str] = []
        for item in self.get_items_flat().keys():
            if item not in unique_items:
                unique_items.append(item)
        return unique_items

    def get_most_scarse(self) -> tuple[str, int] | None:
        min: tuple[str, int] | None = None
        search: dict[str, int]
        if len(self.__items["scarse"]):
            search = self.__items["scarse"]
        elif len(self.__items["moderate"]):
            search = self.__items["moderate"]
        else:
            search = self.__items["abundant"]
        for item, amount in search.items():
            if min is None or amount < min[1]:
                min = (item, amount)
        return min

    def get_most_abundant(self) -> tuple[str, int] | None:
        max: tuple[str, int] | None = None
        search: dict[str, int]
        if len(self.__items["abundant"]):
            search = self.__items["abundant"]
        elif len(self.__items["moderate"]):
            search = self.__items["moderate"]
        else:
            search = self.__items["scarse"]
        for item, amount in search.items():
            if max is None or amount > max[1]:
                max = (item, amount)
        return max

    def get_item_names_by_amount(self, amount: int) -> list[str]:
        items: list[str] = []
        category = self.get_category_for_amount(amount)
        if category is None:
            raise ValueError(f"Error: invalid amout {amount}")
        category_dict = self.get_items().get(category)
        assert category_dict is not None
        for item, item_amount in category_dict.items():
            if item_amount == amount:
                items.append(item)
        return items

    def sample_lookup(self, item: str) -> bool:
        for category in self.get_items().keys():
            category_dict = self.get_items().get(category)
            assert category_dict is not None
            for key_item in category_dict.keys():
                if key_item == item:
                    return True
        return False


class InventoryManager:
    __inventory: Inventory

    def __init__(self):
        self.__inventory = Inventory()

    def get_inventory(self) -> Inventory:
        return self.__inventory

    def print_gobal_inventory_metrics(self):
        total_amount = 0
        for amount in self.get_inventory().get_items_flat().values():
            total_amount += amount
        print(
            "Total items in inventory:",
            f"{total_amount}"
        )
        print(
            "Unique item types:",
            f"{len(self.get_inventory().get_unique_items())}"
        )

    def print_current_inventory(self):
        print("\n=== Current Inventory ===")
        items_flat = self.__inventory.get_items_flat()
        items_total = 0
        for amount in items_flat.values():
            items_total += amount
        for item, amount in items_flat.items():
            print(
                f"{item}: {amount} units",
                f"({(amount * 100 / items_total):.1f}%)"
            )

    def print_inventory_statistics(self):
        print("\n=== Inventory Statistics ===")
        most_abundant = self.get_inventory().get_most_abundant()
        most_scarse = self.get_inventory().get_most_scarse()
        assert most_abundant is not None and most_scarse is not None
        print(f"Most abundant: {most_abundant[0]} ({most_abundant[1]} items)")
        print(f"Least abundant: {most_scarse[0]} ({most_scarse[1]} items)")

    def print_inventory_categories(self):
        print("\n=== Item Categories ===")
        for category in self.get_inventory().get_items().keys():
            category_dict = self.get_inventory().get_items().get(category)
            assert category_dict is not None
            if len(category_dict):
                print(
                    f"{category.capitalize()}:",
                    f"{self.get_inventory().get_items().get(category)}"
                )

    def print_management_suggestions(self):
        print("\n=== Management Suggestions ===")
        i = 0
        items_list = self.get_inventory().get_item_names_by_amount(1)
        items_list_len = len(items_list)
        items_list_str = ""
        for item in items_list:
            items_list_str += item
            if i != items_list_len - 1:
                items_list_str += ", "
            i += 1
        print(f"Restock needed: {items_list_str}")

    def print_dictionary_properties_demo(self):
        print("\n=== Dictionary Properties Demo ===")
        dictionnary_keys = self.get_inventory().get_items_flat().keys()
        dictionnary_keys_len = len(dictionnary_keys)
        dictionnary_keys_str = ""
        i = 0
        for key in dictionnary_keys:
            dictionnary_keys_str += key
            if i != dictionnary_keys_len - 1:
                dictionnary_keys_str += ", "
            i += 1
        print(f"Dictionary keys: {dictionnary_keys_str}")
        dictionnary_values = self.get_inventory().get_items_flat().values()
        dictionnary_values_len = len(dictionnary_values)
        dictionnary_values_str = ""
        i = 0
        for value in dictionnary_values:
            dictionnary_values_str += f"{value}"
            if i != dictionnary_values_len - 1:
                dictionnary_values_str += ", "
            i += 1
        print(f"Dictionary values: {dictionnary_values_str}")
        print(
            "Sample lookup - 'sword' in inventory:",
            f"{self.get_inventory().sample_lookup('sword')}"
        )


def main() -> None:
    print("=== Inventory System Analysis ===")

    inv_manager = InventoryManager()
    inv = inv_manager.get_inventory()

    inv.add_item("potion", 5)
    inv.add_item("armor", 3)
    inv.add_item("shield", 2)
    inv.add_item("sword", 1)
    inv.add_item("helmet", 1)

    inv_manager.print_gobal_inventory_metrics()
    inv_manager.print_current_inventory()
    inv_manager.print_inventory_statistics()
    inv_manager.print_inventory_categories()
    inv_manager.print_management_suggestions()
    inv_manager.print_dictionary_properties_demo()


if __name__ == "__main__":
    main()
