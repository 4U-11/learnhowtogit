import random

player_hp = 10
energy = 3
rooms = ["控制室", "货舱", "反应堆"]

print("=== 失控空间站 ===")
print("输入 explore 探索，输入 status 查看状态，输入 quit 退出。")

while True:
    command = input("\n> ").strip().lower()

    if command == "explore":
        room = random.choice(rooms)
        event = random.choice(["发现补给", "遭遇故障", "一切平静"])

        print(f"\n你来到了：{room}")
        print(f"事件：{event}")

        if event == "发现补给":
            player_hp = min(10, player_hp + 2)
            print("你恢复了 2 点生命值。")
        elif event == "遭遇故障":
            player_hp -= 2
            energy -= 1
            print("你受到损伤，生命值 -2，能源 -1。")

        if player_hp <= 0:
            print("空间站吞噬了你，游戏结束。")
            break

    elif command == "status":
        print(f"\n生命值：{player_hp}/10")
        print(f"能源：{energy}")

    elif command == "quit":
        print("你离开了空间站。")
        break

    else:
        print("未知指令，可用指令：explore、status、quit")