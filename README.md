# Mastermind Game

Welcome to the Mastermind Game! This is a simple command-line implementation of the classic code-breaking game where you must guess the secret code generated by the computer.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Code Explanation](#code)
- [Installation](#installation)

## Introduction

Mastermind is a puzzle game that challenges your logic and deduction skills. The objective is to guess a secret combination of colors within a limited number of attempts. After each guess, feedback is provided in terms of correct color and position matches.

## Features

Every Colour is fully customizable in the settings file.

## Code Explanation

Breakdown of Components
Flask Web Application (flask_app.py):

Imports and Setup: The Flask framework is imported, along with utility functions for serving data.
Endpoints:
/get-results: This endpoint reads from a text file (results.txt) to retrieve the game results. It collects the results and dates, returning them as JSON.
/ (index): This serves the main HTML page (index.html), which displays the results.
Error Handling: It gracefully handles a FileNotFoundError if the results file doesn't exist, returning an empty result list instead.
Main Execution: The application runs in debug mode, which is useful for development.
Game Logic (game.py):

Imports: Utilizes Pygame for graphical rendering, the settings.py for constants, and the rest.py file for managing results.
Game Class: Contains methods to manage the game state, including:
Initialization: Sets up the display and game clock.
Game Loop: The run method contains the main game loop, handling events and rendering.
Drawing: The draw method handles rendering the game board and current game state.
Event Handling: The events method processes user inputs, including mouse and keyboard interactions. It checks for game conditions and updates results.
Win/Loss Checking: check_win and update_or_create_file manage checking win conditions and appending results to the file.
Game Board Logic: The Board class handles the game board, including pin placements and clue management.
Game Board and Pins (board.py):

Pins: The Pin and CluePin classes represent colored pins on the game board. They manage their drawing and state (revealed or hidden).
Board Class: Manages the entire board, including:
Creation of the game board and the color selection area.
Logic for checking user guesses against the hidden code and providing clues.
Drawing the board and handling user interactions for selecting colors and placing pins.
HTML Template (index.html):

Structure: A simple HTML document that displays a results table.
Styling: Basic CSS for a clean layout and responsive design.
JavaScript: Fetches results from the Flask backend using the fetch API and populates the results table. It also counts and displays the number of wins and losses based on the fetched data.
Game Flow
Starting the Server: The Flask application starts up, serving the main page and handling result requests.
Playing the Game: The game initializes and runs in a loop, handling user input and rendering the game state.
User Interactions: Players select colors, place pins, and the game checks if the guesses are correct. Results are updated based on the game's outcome.
Logging Results: When a game ends, results are logged in results.txt.
Viewing Results: The web interface fetches and displays the results, providing a summary of wins and losses.
Methodology & Programming Style
Modularity: The codebase is well-structured with clear separations of concerns. Each class and function has a specific purpose, enhancing readability and maintainability.
Object-Oriented Design: The use of classes (e.g., Game, Board, Pin) allows for encapsulation of functionality and easier management of game state.
Event-Driven Programming: The game loop responds to events (mouse clicks, key presses) in a non-blocking manner, which is essential for interactive applications.
Error Handling: The Flask app includes basic error handling for file operations, which is important for robustness.
Suggestions for Improvement
Testing: Implement unit tests to verify the functionality of key components, especially the game logic and result logging.
Code Comments: Adding comments and docstrings can help future developers (or yourself) understand the logic faster.
Configurable Settings: Instead of hardcoding values in the settings.py, consider allowing these to be configurable via a JSON or YAML file for easier adjustments.
Dynamic Results: Enhance the web interface to allow real-time updates of results without needing a page refresh using WebSockets or long polling.

## Installation

To get started with this project, clone this repository using:
```bash
git clone https://github.com/jasp123/mastermind-game.git
