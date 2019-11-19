from pygame import draw
from model import Field, Block, Figure

# 12x12 field
# field = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
field = [[0 for _ in range(12)] for __ in range(12)]

def draw_bricks(block_field: list, surface, f: Field, b: Figure) -> None:
    """Draws all dropped bricks on the field"""
    for i, row in enumerate(block_field):
        for j, el in enumerate(row):
            if el:
                draw.rect(surface,
                          color=(255, 50, 50),
                          rect=[f.get_v_boarder() + j*b.get_block_w(),
                                f.get_h_boarder() + i*b.get_block_h(),
                                b.get_block_w(),
                                b.get_block_h()])
                # frame just for contrast
                draw.rect(surface,
                          (255, 255, 255),
                          [f.get_v_boarder() + j * b.get_block_w(),
                                f.get_h_boarder() + i * b.get_block_h(),
                                b.get_block_w(),
                                b.get_block_h()],
                                1)


def add_square(block_field: list, block: Block) -> None:
    """Changes field list from 0 to 1 for filled brick"""
    block_field[block.get_y() // block.get_h()][block.get_x() // block.get_w()] = 1


def check_lines(block_field: list):
    """ check if fully filled line on the field and deletes it"""
    for i, row in enumerate(block_field):
        if row == [1 for _ in range(12)]:
            block_field.pop(i)
            a = [0 for _ in range(12)]
            block_field.insert(0, a)
            print(block_field)
            break
