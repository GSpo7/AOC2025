# password Cracking logic
position = 50
count = 0
with open("dial_password.txt", "r") as file:
    for line in file:
        line = line.strip()
        if not line:
            continue
        direction = line[0]
        distance = int(line[1:])
        if direction == 'L':
            position = (position - distance) % 100
        elif direction == 'R':
            position = (position + distance) % 100
        if position == 0:
            count += 1
print("The password is:", count)
input("Press Enter to exit")