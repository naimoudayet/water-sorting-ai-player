from android_player import AndroidPlayer
from solver import Solver, Solution
from android_reader import AndroidReader
from scanner import Scanner, LevelRepresentation


if __name__ == '__main__':

    DEBUG_MODE = False

    print("Reading level")
    level_image = AndroidReader(DEBUG_MODE).read_level_image()

    print("Scanning level")
    level: LevelRepresentation = Scanner(DEBUG_MODE).scan_level(level_image)

    print("Solving level")
    solution: Solution = Solver(DEBUG_MODE).solve_level(level.tubes)

    print("Executing solution")
    AndroidPlayer().play(solution.solution_steps, level.touch_locations)

    print("Done")
