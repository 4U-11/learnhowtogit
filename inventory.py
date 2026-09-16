items = ["维修工具"]


def add_item(item):
    items.append(item)


def show_inventory():
    print("当前背包：")

    if items:
        for item in items:
            print(f"- {item}")
    else:
        print("背包是空的")


def use_item(item):
    if item in items:
        items.remove(item)
        return True

    return False