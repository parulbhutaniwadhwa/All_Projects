Project: FLAMES - A Chasing Game

Brief description of the project.

## Python Code Files

- snake_game_human.py (game to be played by human)
- game.py (automated logic of game)
- model.py (Q-learning Model implementation)
- agent.py (environment for running the code)
- runningWithGPU.py (to be run with GPU)

## snake_game_human.py

- If a human wants to run the game then the user can directly run this script without any changes.

## game.py

- This is the automated version of the game logic that includes all the movements, actions and states a user can create. 
Basically, it covers all the permutations and combinations of the game.
All the classes and functions of this code is called in agent.py. Hence, no changes to be made in this code.

## model.py

- It includes model parameters. It calls all the model related functions. 
All the classes and functions of this code is called in agent.py. Hence, no changes to be made in this code.

## agent.py

- This is the main code which runs all the functions and logic.
- If the user is running the project on CPU, then directly run this script.

## runningWithGPU.py

-this includes code related to GPU packages of tensorflow.
If the user wants to run the project with GPU, then run this script directly.

## Steps to run the project

1. Unzip the folder 'ReinforcementCode_FLAME'.
2. Run either agent.py or runningWithGPU.py.

## Contribution

- Parul Bhutani Wadhwa - Building Game and Agent
- Vatsal Shah - Building Model and setting environment
- Snehal Kathiriya - Researching content and making presentation
- Kiranpal Sidhu - Researching content and creating document
- Arvind Pal Singh - Support with documentation
- Amandeep Kaur - supporting with content and pictures.
