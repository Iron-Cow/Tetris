from pygame import draw
from model import Field, Block
block_field = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


def draw_bricks(block_field: list, surface, f: Field, b: Block) -> None:
    for i, row in enumerate(block_field):
        for j, el in enumerate(row):
            if el:
                draw.rect(surface,
                          color=(255, 50, 50),
                          rect=[f.get_v_boarder() + j*b.get_w(),
                                f.get_h_boarder() + i*b.get_h(),
                                b.get_w(),
                                b.get_h()])
                draw.rect(surface,
                          (255, 255, 255),
                          [f.get_v_boarder() + j * b.get_w(),
                                f.get_h_boarder() + i * b.get_h(),
                                b.get_w(),
                                b.get_h()], 1)


def add_square(block_field: list, block):
    block_field[block.get_y() // block.get_h()][block.get_x() // block.get_w()] = 1


def check_lines(block_field: list):
    for i, row in enumerate(block_field):
        if 0 not in row:
            block_field.pop(i)
            t = []
            a = [t.append(0) for _ in range(12)]
            block_field.insert(0, a)
            break

