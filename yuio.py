import random

# Define the grid
rows = 15
cols = 15
grid = [[0 for _ in range(cols)] for _ in range(rows)]

# Define the words
words = {
    "python": "a high-level programming language",
    "variable": "a container for a value",
    "function": "a reusable block of code",
    # add more words and definitions here
}

# Generate the puzzle
for word in words.keys():
    # randomly place the word in the grid
    direction = random.choice(["across", "down"])
    if direction == "across":
        row = random.randint(0, rows-1)
        col = random.randint(0, cols-len(word))
        for i, letter in enumerate(word):
            grid[row][col+i] = 1
    else:
        row = random.randint(0, rows-len(word))
        col = random.randint(0, cols-1)
        for i, letter in enumerate(word):
            grid[row+i][col] = 1

# Print the puzzle
for row in grid:
    for cell in row:
        if cell == 0:
            print(".", end="")
        else:
            print("*", end="")
    print()

# Generate the clues
for i, (word, definition) in enumerate(words.items()):
    print(f"{i+1}. {direction.capitalize()} - {definition}")
