import random

from inventory import add_item, show_inventory, use_item


MAX_HP = 10
player_hp = MAX_HP
energy = 8
repairs = 0

rooms = ["控制室", "货舱", "反应堆"]


print("=== 失控空间站 ===")
print("目标：找到系统零件，修复反应堆 3 次后逃离空间站。")
print("输入 help 查看指令。")


while True:
    command = input("\n> ").strip().lower()

    if command == "explore":
        if energy <= 0:
            print("能源耗尽，无法继续探索。")
            continue

        energy -= 1
        room = random.choice(rooms)
        event = random.choice(
            ["发现补给", "遭遇故障", "找到系统零件", "一切平静"]
        )

        print(f"\n你来到了：{room}")
        print(f"事件：{event}")

        if event == "发现补给":
            add_item("医疗包")
            print("你获得了一个医疗包。")

        elif event == "遭遇故障":
            player_hp -= 2
            print("你受到损伤，生命值 -2。")

        elif event == "找到系统零件":
            add_item("系统零件")
            print("你获得了一个系统零件。")

        else:
            print("这里暂时没有异常。")

        if player_hp <= 0:
            print("你的生命值归零，游戏结束。")
            break

    elif command == "inventory":
        show_inventory()

    elif command == "heal":
        if player_hp == MAX_HP:
            print("你的生命值已经满了。")
        elif use_item("医疗包"):
            player_hp = min(MAX_HP, player_hp + 4)
            print("你使用了医疗包，生命值恢复 4 点。")
        else:
            print("背包中没有医疗包。")

    elif command == "repair":
        if use_item("系统零件"):
            repairs += 1
            print(f"反应堆修复成功，目前进度：{repairs}/3")

            if repairs >= 3:
                print("反应堆修复完成，你成功逃离了空间站！")
                break
        else:
            print("背包中没有系统零件。")

    elif command == "status":
        print(f"\n生命值：{player_hp}/{MAX_HP}")
        print(f"能源：{energy}")
        print(f"反应堆修复进度：{repairs}/3")

    elif command == "help":
        print("\n可用指令：")
        print("explore   探索空间站")
        print("inventory 查看背包")
        print("heal      使用医疗包")
        print("repair    使用系统零件修复反应堆")
        print("status    查看状态")
        print("quit      退出游戏")

    elif command == "quit":
        print("你离开了空间站。")
        break

    else:
        print("未知指令，请输入 help 查看帮助。")