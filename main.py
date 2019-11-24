import pygame
from model import Field, Figure, BlockField, Score
from gui import draw_bricks, check_lines
from random import randint

if __name__ == "__main__":
    pygame.init()

    figure_list = [
        [[0, 0, 0],
         [1, 0, 0],
         [1, 1, 1]],

        [[1],
         [1],
         [1]],

        [[1, 1],
         [1, 1]],

        [[1, 1, 0],
         [0, 1, 1]],

        [[0, 1, 1],
         [1, 1, 0]],

        [[0, 1, 0],
         [1, 1, 1]],

        [[1, 1, 1, 1]]
    ]

    score = Score(0, 30, 30)

    # Initiating field. For current project it is 10px frame and 12x12 field made by 50x50px blocks
    screen = Field(600, 700, 10, 10, (0, 0, 0), (255, 255, 255))
    window = pygame.display.set_mode((screen.get_w() + screen.get_v_boarder() * 2,
                                      screen.get_h() + screen.get_h_boarder() * 2))

    # list of filled/blank blocks
    block_field = BlockField(config=[[0 for _ in range(screen.get_w()//50)] for __ in range(screen.get_h()//50)])


    def figure_create():
        return Figure(surface=window,
                      x=260,
                      y=10,
                      color=(255, 255, 255),
                      config=figure_list[randint(0, len(figure_list)-1)],
                      field=screen,
                      block_field=block_field
                      )


    figure = figure_create()

    clock = pygame.time.Clock()
    tick_counter = 0

    run = True
    while run:
        clock.tick(30)  # frames per second
        tick_counter += 1
        screen.draw_field(window)

        for event in pygame.event.get():  # key mapping of the game
            # print(event)
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                try:
                    if event.key == pygame.K_RIGHT:
                        figure.move_right()

                    elif event.key == pygame.K_LEFT:
                        figure.move_left()

                    elif event.key == pygame.K_DOWN:
                        figure.fall()

                    elif event.key == pygame.K_SPACE:
                        figure.set_config(figure.rotated_figure())

                except IndexError:
                    pass

        if tick_counter == 10:  # each 10th frame the movement down will be initiated
            if not figure.fall():
                figure = figure_create()
            tick_counter = 0
        score.draw_score(window)
        draw_bricks(block_field.get_block_field(), window, f=screen, b=figure)  # draw filled bricks
        check_lines(block_field.get_block_field(), score)  # check if fully filled line on the field and deletes it
        figure.draw_figure()
        if 1 in block_field.get_block_field()[1]:
            run = False

