# Connect 4 Game Implementation

A fully playable Python implementation of the classic Connect Four game, featuring both command-line and GUI versions with intelligent game mechanics and user-friendly interfaces.

## Project Overview

This project delivers a complete Connect 4 gaming experience through two distinct interfaces: a streamlined terminal version for quick gameplay and a rich GUI version with visual animations and enhanced user interaction. Built with modern Python libraries, the implementation focuses on clean code architecture and optimal user experience.

### Key Achievements
- **Dual Interface Design** - Terminal and GUI versions for different user preferences
- **Intelligent Game Logic** - Robust win detection and game state management

## Architecture

```
Game Engine → Interface Layer → User Interaction → Visual Rendering
```

## Technology Stack

**Core Development:**
- Python (NumPy for game logic optimization)
- Object-oriented programming principles

**GUI Implementation:**
- Pygame (graphics rendering and event handling)
- PyAutoGUI (enhanced user interaction)

**Terminal Interface:**
- Native Python I/O
- ASCII-based visual representation

## Game Features

### Core Gameplay
- **Classic Connect 4 Rules**: Standard 7x6 grid with gravity-based piece placement
- **Win Detection**: Horizontal, vertical, and diagonal pattern recognition
- **Turn Management**: Alternating player system with visual indicators
- **Input Validation**: Robust error handling for invalid moves

### GUI Version (main.py)
- **Visual Game Board**: Graphical representation with colored pieces
- **Mouse Interaction**: Click-to-play column selection
- **Game Status Display**: Current player and win/draw notifications

### Terminal Version (terminal_only.py)
- **ASCII Art Board**: Clean text-based visual representation
- **Keyboard Input**: Numeric column selection
- **Instant Feedback**: Immediate move validation and board updates
- **Lightweight Design**: Minimal resource usage for quick gameplay

## Technical Implementation

### Game Logic Architecture
- **Board State Management**: NumPy arrays for efficient game state representation
- **Win Detection Algorithm**: Optimized pattern matching across all directions
- **Move Validation**: Comprehensive checking for valid column placement

### Performance Optimizations
- **NumPy Integration**: Vectorized operations for fast board calculations
- **Efficient Algorithms**: O(1) move validation and O(n) win detection
- **Memory Management**: Optimized data structures for minimal overhead

## Getting Started

### Prerequisites
```bash
pip install numpy pygame pyautogui
```

### Running the Game

**GUI Version:**
```bash
python main.py
```

**Terminal Version:**
```bash
python terminal_only.py
```

## Project Structure

```
├── main.py                    # GUI version with Pygame interface
├── terminal_only.py           # Command-line version
├── README.md                  # Project documentation
```

## Gameplay Instructions

### GUI Version
1. Launch the application with `python main.py`
2. Click on any column to drop your piece
3. Pieces fall to the lowest available position
4. First player to connect 4 pieces wins

### Terminal Version
1. Run `python terminal_only.py`
2. Enter column number (1-7) when prompted
3. View updated board after each move
4. Game announces winner or draw condition

## Technical Highlights

### Code Quality Features
- **Modular Design**: Clear separation between game logic and interface
- **Error Handling**: Comprehensive input validation and exception management
- **Scalability**: Architecture supports easy feature additions

### Algorithm Efficiency
- **Smart Win Detection**: Checks only necessary positions after each move
- **Optimized Data Structures**: NumPy arrays for fast board operations
- **Memory Efficient**: Minimal memory footprint for game state

## Technical Skills Demonstrated

- **Python Programming**: Advanced use of Python features and libraries
- **Game Development**: Understanding of game loops and state management
- **GUI Development**: Creating responsive user interfaces with Pygame
- **Algorithm Design**: Efficient win detection and game logic
- **Code Architecture**: Clean, maintainable code structure
- **User Experience**: Intuitive interface design for both terminal and GUI

---

**Contact**: [https://www.linkedin.com/in/danieldema/] | [danieldema42@gmail.com]

**Repository**: [https://github.com/danieldema/connect4]
