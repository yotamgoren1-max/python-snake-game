# 🐍 Python Snake Game

A classic Snake game built from scratch using Python and Pygame. This project demonstrates core concepts of Object-Oriented Programming (OOP), game loop architecture, asynchronous event handling, and dynamic scaling.

## 🚀 Features
* **Custom Object-Oriented Design:** Clean separation of concerns with `Snake` and `Apple` classes.
* **Dynamic Difficulty:** The game progressively increases the frame rate (FPS) based on the player's score.
* **Grid-Based Physics:** Mathematical alignment ensures all movements and random apple spawns strictly snap to a precise 20x20 pixel grid.
* **Robust Input Handling:** Prevents illegal moves (e.g., instant 180-degree turns that would cause immediate self-collision).

## 📂 Project Structure
* `main.py`: The entry point containing the main game loop, event listening, and rendering logic.
* `game_objects.py`: Contains the OOP models for the `Snake` and `Apple`, handling movement, growth, and grid alignment.
* `config.py`: A centralized configuration file for constants (colors, screen dimensions, speeds), eliminating "magic numbers" from the logic.

## 🧠 Architecture & Logic Flow

### Event Handling Logic
```text
               ┌─────────────────────────────────────────┐
               │  New Event in pygame.event.get() queue  │
               └────────────────────┬────────────────────┘
                                    │
                    ┌───────────────┴───────────────┐
                    ▼                               ▼
          [event.type == QUIT]            [event.type == KEYDOWN]
                    │                               │
                    ▼                               ▼
             running = False                Which key was pressed?
                                                    │
                 ┌──────────────────┬───────────────┴───────────────┬──────────────────┐
                 ▼                  ▼                               ▼                  ▼
              [K_UP]             [K_DOWN]                        [K_LEFT]           [K_RIGHT]
                 │                  │                               │                  │
                 ▼                  ▼                               ▼                  ▼
          if not moving      if not moving                   if not moving      if not moving
              DOWN:               UP:                            RIGHT:              LEFT:
          direction = UP     direction = DOWN               direction = LEFT   direction = RIGHT