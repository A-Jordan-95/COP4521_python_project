# COP4521_python_project

Team Members:
- Alexander Jordan
- Paul Santora
- Jacob Petrillo
- Nicholas Ford
- Nathan Granger


- current ideas:
-  2D graphics based game
    - python Arcade library seems to be a good choice for game design
    - gameplay ideas:
      - "Escape the Evil Hacker's Lair"
        - Mario style adventure game
        - cave setting
        - players collect pieces of a computer on each level(hard drive, monitor, keyboard, mouse etc)
        - avoid evil AI robots roaming around the caves.
        - once all pieces found can use the computer to open the "vault" or something similar to the next level.
        - maybe have player use computer to answer a computer sciencey question to "unlock" next level?
          - i.e. what is proper syntax for python for loop, etc.

WORKLOAD:
  - necessary tasks to split up:
    - 1. gathering/drawing graphics for the following sprites:
      - player/s
      - enemy/ies
      - ground/walls of map setting
      - other obstacles
      - hidden pieces
      - vault/door/lock to next level
    - 2. build above graphics into game once gathered
    - 3. build menu/transition screens
    - 4. gameplay design:
      - platformer with multiple levels
      - initial goal of five total levels for the game
    - 5. implementation of game physics/flow rules
    - 6. stretch goals:
        - connect game with a SQL backend using python libraries and
          deploy as a web application with a site that tracks details
          such as high scores, and allows user profiles etc.
            - research feasibility of using flask for this task and decide
