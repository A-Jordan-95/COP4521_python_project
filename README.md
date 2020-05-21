# COP4521_python_project

Team Members:
-Alexander Jordan
-Paul Santora
-Jacob Petrillo


current ideas:
-2D graphics based game
    -python Arcade library seems to be a good choice for game design
    -gameplay ideas:
      -"Escape the Evil Hacker's Lair"
        -Mario style adventure game
        -cave setting
        -players collect pieces of a computer on each level(hard drive, monitor, keyboard, mouse etc)
        -avoid evil AI robots roaming around the caves.
        -once all pieces found can use the computer to open the "vault" or something similar to the next level.
        -maybe have player use computer to answer a computer sciencey question to "unlock" next level?
          -i.e. what is proper syntax for python for loop, etc.
        -two possible styles of gameplay:
            -1. Mario 2d style with scrolling screen, players can jump and run left to right
                -cons:
                    -programming physics for jumping + screen scrolling may be fairly complicated
                      -edit: arcade library offers a simple physics engine
                        as well as a more complicated physics engine called
                        PyMunk, both seem to be fairly straightforward and useful for building platformer style games.
                -pros:
                    -the final product would be more entertaining/advanced and generally look better
            -2. Minesweeper-ish style 2d where the whole map is viewed from above not the side
                -cons:
                    -slightly less advanced/entertaining final product.
                -pros:
                    -don't have to program jump or screen scrolling physics, could still achieve
                        a gameplay that represents the original idea above w/ computer pieces to find
                        and robots to avoid. maybe the computer pieces are hidden under rocks but some rocks
                        set off a switch that lets in more robots to avoid?
WORKLOAD:
  -necessary tasks to split up:
    -1. gathering/drawing graphics for the following sprites:
      -player/s
      -enemy/ies
      -ground/walls of map setting
      -other obstacles
      -hidden pieces
      -vault/door/lock to next level
    -2. build above graphics into game once gathered
    -3. build menu/transition screens
    -4. gameplay design:
      -choose layout <side view platformer/top view static map>
      -choose physics engine to use <built in arcade physics_engine/pymunk>
      -choose how to advance to next level <gen programming/python>
      -<build in extras like guns/shields/extra lives etc.>
    -5. implementation of game physics once above have been decided
    -6. streeeeeeeetch goals:
        <connect game with a SQL backend using python libraries and
        deploy as a web application with a site that tracks details
        such as high scores, and allows user profiles etc.>
          -(Alex): I have some experience with the database part of this (not a lot) and really haven't looked into the web application part at all so this is more if we get more team members than we currently have and have the time/capability to pull it off.
            -could be a really good resume project at this point and
            possibly even generate ad revenue on the website?(probably miniscule profits but could cover server hosting costs maybe?).
