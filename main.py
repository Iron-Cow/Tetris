import pygame
from model import Block, Field
from gui import field, draw_bricks, add_square, check_lines

if __name__ == "__main__":
    pygame.init()

    # list of filled/blank blocks
    block_field = field

    # Initiating field. For current project it is 10px frame and 12x12 field made by 50x50px blocks
    screen = Field(600, 600, 10, 10, (0, 0, 0), (255, 255, 255))
    window = pygame.display.set_mode((screen.get_w() + screen.get_v_boarder()*2,
                                      screen.get_h() + screen.get_h_boarder()*2))

    # Block size initiating
    block = Block(260, 60, 50, 50, (255, 255, 255), screen)

    clock = pygame.time.Clock()
    tick_counter = 0

    run = True
    while run:
        clock.tick(40)  # frames per second
        tick_counter += 1
        screen.draw_field(window)

        for event in pygame.event.get():  # key mapping of the game
            # print(event)
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                try:
                    if event.key == pygame.K_RIGHT:
                        if not block_field[(block.get_y()-screen.get_h_boarder())//block.get_h()][(block.get_x()-screen.get_v_boarder())//block.get_w() + 1]:
                            block.move_right()

                    elif event.key == pygame.K_LEFT:
                        if not block_field[(block.get_y()-screen.get_h_boarder())//block.get_h()][(block.get_x()-screen.get_v_boarder())//block.get_w() - 1]:
                            block.move_left()
                except IndexError:
                    pass

        if tick_counter == 10:  # each 10th frame the movement down will be initiated
            try:
                # if block under current if empty - block can be dropped
                if block_field[block.get_y() // block.get_h() + 1][block.get_x() // block.get_w()] == 0:
                    block.drop_block()
                # else: block reached filled block and should be marked as filled also + initiate new block
                else:
                    add_square(block_field, block)
                    block = Block(260, 60, 50, 50, (255, 255, 255), screen)

            except IndexError:  # block reached ground
                add_square(block_field, block)
                block = Block(260, 60, 50, 50, (255, 255, 255), screen)
            tick_counter = 0

        draw_bricks(block_field, window, f=screen, b=block)  # draw filled bricks
        block.draw_block(window)  # draw current dropping brick
        check_lines(block_field)  # check if fully filled line on the field and deletes it

        pygame.display.update()

