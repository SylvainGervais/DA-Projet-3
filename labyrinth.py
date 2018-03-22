import json
import random

import config


class Labyrinth:
    def __init__(self, map):
        """initialyze labyrinth from file"""
        self.load(map)

    def load(self, mapFile):
        """load a json file in Labyrinth object"""
        try:
            with open(mapFile, "r") as f:
                self.map = json.load(open(mapFile))
                print("Loading map : ", mapFile, ".......OK")

        except OSError as e:
            print("Problem with file :", e)

    def print(self):
        """print labyrinth in terminal"""
        print()
        for line in self.map:
            for cell in line:
                print(cell, end="")
            print()
        print()

    def get_positions(self, content):
        """return coordinates list of cells containing argument"""
        positions = []
        for i, line in enumerate(self.map):
            for j, cell in enumerate(line):
                if cell == content:
                    positions.append([i, j])
        return positions

    def replace_cell(self, cell_line, cell_column, content):
        """replace cell at position [line, column] with argument"""
        for i, line in enumerate(self.map):
            if i == cell_line:
                for j, column in enumerate(line):
                    if j == cell_column:
                        line[j] = content

    def place_item(self, nb_item):
        """place items randomly and return items positions list"""
        free_cells = self.get_positions(config.FREE_SPACE)
        item_cells = random.sample(free_cells, k=nb_item)
        for cell in item_cells:
            item_line = cell[0]
            item_column = cell[1]
            self.replace_cell(item_line, item_column, config.ITEM)
        return item_cells

    def cell_content(self, position):
        """return cell's content in labyrinth position in argument"""
        line_position = position[0]
        column_position = position[1]

        for i, line in enumerate(self.map):
            if i == line_position:
                content = line[column_position]
        return content
