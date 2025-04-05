import tkinter as tk
import random

# Constants
WIDTH = 600
HEIGHT = 400
SEG_SIZE = 20
SPEED = 100  # Speed of the snake (in ms)

class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake Game")
        
        self.canvas = tk.Canvas(self.root, width=WIDTH, height=HEIGHT, bg="black")
        self.canvas.pack()

        self.snake = [(100, 100), (80, 100), (60, 100)]  # Initial snake
        self.snake_direction = "Right"
        self.food = None
        self.game_over = False
        
        self.create_food()
        self.update_snake()
        self.bind_keys()
        self.run_game()

    def create_food(self):
        """ Create food at a random location. """
        x = random.randint(0, (WIDTH - SEG_SIZE) // SEG_SIZE) * SEG_SIZE
        y = random.randint(0, (HEIGHT - SEG_SIZE) // SEG_SIZE) * SEG_SIZE
        self.food = (x, y)
        self.canvas.create_rectangle(x, y, x + SEG_SIZE, y + SEG_SIZE, fill="red", tags="food")

    def update_snake(self):
        """ Draw the snake on the canvas. """
        self.canvas.delete("snake")  # Clear the previous snake
        for segment in self.snake:
            self.canvas.create_rectangle(segment[0], segment[1], segment[0] + SEG_SIZE, segment[1] + SEG_SIZE,
                                          fill="green", tags="snake")

    def move_snake(self):
        """ Move the snake in the current direction. """
        head_x, head_y = self.snake[0]
        
        if self.snake_direction == "Up":
            head_y -= SEG_SIZE
        elif self.snake_direction == "Down":
            head_y += SEG_SIZE
        elif self.snake_direction == "Left":
            head_x -= SEG_SIZE
        elif self.snake_direction == "Right":
            head_x += SEG_SIZE

        new_head = (head_x, head_y)

        # Check if snake collides with the wall
        if head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT:
            self.game_over = True
            return

        # Check if snake collides with itself
        if new_head in self.snake:
            self.game_over = True
            return

        # Add new head to the snake
        self.snake = [new_head] + self.snake[:-1]

        # Check if snake eats food
        if new_head == self.food:
            self.snake.append(self.snake[-1])  # Add a new segment to the snake
            self.canvas.delete("food")  # Remove the food
            self.create_food()  # Create new food

    def bind_keys(self):
        """ Bind the arrow keys to change snake's direction. """
        self.root.bind("<Left>", lambda event: self.change_direction("Left"))
        self.root.bind("<Right>", lambda event: self.change_direction("Right"))
        self.root.bind("<Up>", lambda event: self.change_direction("Up"))
        self.root.bind("<Down>", lambda event: self.change_direction("Down"))

    def change_direction(self, direction):
        """ Change the snake's direction. """
        if self.game_over:
            return

        if direction == "Left" and self.snake_direction != "Right":
            self.snake_direction = "Left"
        elif direction == "Right" and self.snake_direction != "Left":
            self.snake_direction = "Right"
        elif direction == "Up" and self.snake_direction != "Down":
            self.snake_direction = "Up"
        elif direction == "Down" and self.snake_direction != "Up":
            self.snake_direction = "Down"

    def run_game(self):
        """ Main game loop. """
        if not self.game_over:
            self.move_snake()
            self.update_snake()
            self.root.after(SPEED, self.run_game)
        else:
            self.canvas.create_text(WIDTH // 2, HEIGHT // 2, text="Game Over", fill="white", font=("Arial", 24))

# Initialize the game
def main():
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
