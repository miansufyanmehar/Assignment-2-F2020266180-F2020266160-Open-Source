<!-- # How to run
```
cd code_directory
python -m venv venv
source venv/bin/activate

python main.py # if default name of input file is moves.txt

python -m unittest tests.py
```
 ## Output File
* Output file can be accessed in output folder after run ```python main.py``` successfully -->


# Knight's Adventure Game

This project implements a simple text-based adventure game involving knights, items, and battles. Knights move across a board, acquire items, and engage in battles.

## Project Structure

The project is organized into several files:

1. **board.py**: Defines the `Board` class, which represents the game board.

2. **coordinates.py**: Contains the `Position` class, representing the position of game elements.

3. **scores.py**: Defines the `Score` class, which represents the attack and defense scores.

4. **item.py**: Contains the `Item` class, representing items that knights can acquire.

5. **state.py**: Defines the `State` enum, representing the state of a knight (e.g., Live, Dead, Drowned).

6. **knight.py**: Implements the `Knight` class, representing the knights in the game.

7. **main.py**: The main entry point of the game. Reads input instructions, processes them, and produces the final state.

8. **tests.py**: Unit tests for various scenarios and functionalities.

9. **requirements.txt**: Lists the dependencies for the project.

## How to Run

1. Clone the repository:

    ```bash
    git clone https://github.com/abdulrehman160/Open-Source-F2020266160-F2020266180
    ```

2. Navigate to the project directory:

    ```bash
    cd code_directory
    ```

3. Create a virtual environment:

    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment:

    - On Windows:

        ```bash
        .\venv\Scripts\activate
        ```

    - On macOS/Linux:

        ```bash
        source venv/bin/activate
        ```

5. Run the game:

    ```bash
    python main.py --infile input/moves.txt --outfile output/final_state.json
    ```

6. Deactivate the virtual environment when you're done:

    ```bash
    deactivate
    ```

## Testing

Run the unit tests using:

```bash
python -m unittest tests.py
