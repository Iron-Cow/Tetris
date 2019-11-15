import pygame
from model import Block, Field
from gui import block_field, draw_bricks, add_square, check_lines

if __name__ == "__main__":
    pygame.init()
    screen = Field(600, 600, 10, 10, (0, 0, 0), (255, 255, 255))
    window = pygame.display.set_mode((screen.get_w() + screen.get_v_boarder()*2, screen.get_h() +screen.get_h_boarder()*2))
    run = True
    block = Block(60, 60, 50, 50, (255, 255, 255), screen)
    last_key = 0
    clock = pygame.time.Clock()
    tick_counter = 0

    while run:
        clock.tick(100)
        tick_counter += 1
        screen.draw_field(window)
        for event in pygame.event.get():
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
        if tick_counter == 10:
            try:
                if block_field[block.get_y() // block.get_h() + 1][block.get_x() // block.get_w()] == 0:
                    block.drop_block()
                else:
                    add_square(block_field, block)
                    block = Block(60, 60, 50, 50, (255, 255, 255), screen)

            except IndexError:
                add_square(block_field, block)
                block = Block(60, 60, 50, 50, (255, 255, 255), screen)
            tick_counter = 0
        draw_bricks(block_field, window, f=screen, b=block)

        block.draw_block(window)
        check_lines(block_field)
        pygame.display.update()

