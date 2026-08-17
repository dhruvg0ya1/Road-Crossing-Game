# Road Crossing

A Frogger-style crossing game built with Python's `turtle` graphics module.

[![Python](https://img.shields.io/badge/python-3.10%2B-blue?style=flat-square&logo=python&logoColor=white)](https://www.python.org/) [![Turtle](https://img.shields.io/badge/turtle-graphics-2ea44f?style=flat-square)](https://docs.python.org/3/library/turtle.html)

---

## Play

```bash
git clone https://github.com/dhruvg0ya1/Road-Crossing-Game.git
cd Road-Crossing-Game
python Main.py
```

Press `Up` to advance. Reach the far side to clear the level; every level the
traffic moves faster.

## How it is built

```
Main.py                  game loop, level progression, collision detection
Resources/
├── Player.py            movement and reset-to-start on collision
├── Car.py               spawning, random lanes and colours, speed scaling
└── Scoreboard.py        level counter and game-over screen
```

Cars spawn at random y-positions and travel right to left. Clearing a level
increases the car speed, so difficulty scales continuously rather than in steps.

## Requirements

Python 3.10+. `turtle` is part of the standard library.
