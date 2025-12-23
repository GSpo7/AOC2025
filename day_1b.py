# password Cracking logic
position = 50
count = 0
with open('dial_password.txt', 'r') as file:
    for line in file:
        line = line.strip()  # Remove whitespace
        if not line:
            continue
        direction = line[0]
        distance = int(line[1:])
        # Determine the step direction: +1 for right, -1 for left
        step = 1 if direction == 'R' else -1
        # Simulate each click in the rotation
        for _ in range(distance):
            position = (position + step) % 100  # Move one click and wrap around
            if position == 0:
                count += 1  # Count every time it hits 0 during or after the move
print("Password is:", count)
input("Press Enter to continue...")