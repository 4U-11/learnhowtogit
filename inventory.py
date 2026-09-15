items = ["医疗包", "维修工具"]


def show_inventory():
    print("当前背包：")

    if items:
        for item in items:
            print(f"- {item}")
    else:
        print("背包是空的")