import pygame
from random import randint
from numpy import rot90, array


class Field:
    def __init__(self, w: int, h: int, v_boarder: int, h_boarder: int, bg_color: tuple, frame_color: tuple):
        self.__w = w
        self.__h = h
        self.__v_boarder = v_boarder
        self.__h_boarder = h_boarder
        self.__bg_color = bg_color
        self.__frame_color = frame_color

    def get_w(self):
        return self.__w

    def get_h(self):
        return self.__h

    def get_v_boarder(self):
        return self.__v_boarder

    def get_h_boarder(self):
        return self.__h_boarder

    def draw_field(self, window):
        window.fill(self.__bg_color)
        pygame.draw.rect(window,
                         self.__frame_color,
                         [self.__v_boarder, self.__h_boarder, self.__w, self.__h],
                         1)


class BlockField:
    """List with empty/filled blocks"""
    def __init__(self, config: list):
        self.__config = config

    def get_block_field(self):
        return self.__config

    def set_block_field(self, config: list):
        self.__config = config


class Block:
    def __init__(self, x: float,
                 y: float,
                 w: float,
                 h: float,
                 color: tuple,
                 field: Field):
        self.__x = x
        self.__y = y
        self.__w = w
        self.__h = h
        self.__color = color
        self.__field = field

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def get_w(self):
        return self.__w

    def get_h(self):
        return self.__h

    def draw_block(self, surface):
        pygame.draw.rect(surface=surface, rect=[self.__x, self.__y, self.__w, self.__h],
                         color=self.__color)
        pygame.draw.rect(surface, (randint(0, 255), randint(0, 255), randint(0, 255)),
                         [self.__x, self.__y, self.__w, self.__h], 1)

    def drop_block(self):
        self.__y += self.__h
        # if self.__y > self.__field.get_h() + self.__field.get_h_boarder() - self.__h:
        #     self.__y = self.__field.get_v_boarder()

    def move_left(self):
        if self.__x > self.__field.get_v_boarder():
            self.__x -= self.__w

    def move_right(self):
        if self.__x < self.__field.get_w() + self.__field.get_v_boarder() - self.__w:
            self.__x += self.__w


class Figure:
    """Multiblock figure like in real tetris"""
    def __init__(self, surface, x: float, y: float, config: list, color: tuple, field: Field,
                 block_field: BlockField, block_w: float = 50, block_h: float = 50, ):
        self.__surface = surface
        self.__x = x
        self.__y = y
        self.__config = config
        self.__color = color
        self.__field = field
        self.__block_w = block_w
        self.__block_h = block_h
        self.__block_field = block_field

    def __generate_block_list(self) -> list:
        """Generates list of Block objects"""
        block_list = []
        for i, row in enumerate(self.__config):
            for j, el in enumerate(row):
                if el:
                    b = Block(x=self.__x + j * self.__block_w,
                              y=self.__y + i * self.__block_h,
                              w=self.__block_w,
                              h=self.__block_h,
                              color=self.__color,
                              field=self.__field)
                    block_list.append(b)
        return block_list

    def draw_figure(self) -> None:
        for block in self.__generate_block_list():
            block.draw_block(self.__surface)

    def fall(self):
        """Figure fall down by TIME (not button)"""
        for block in self.__generate_block_list():
            try:
                # if block under current if empty - block can be dropped
                if self.__block_field.get_block_field()[block.get_y() // block.get_h() + 1][block.get_x() //
                                                                                            block.get_w()] == 0:
                    pass
                # else: block reached filled block and should be marked as filled also + initiate new block
                else:
                    self.figure_stand()
                    return False
                    # block = Block(260, 60, 50, 50, (255, 255, 255), self.__surface)

            except IndexError:  # block reached ground
                self.figure_stand()
                return False
        self.__y += self.__block_h
        return True

    def move_left(self) -> None:
        for block in self.__generate_block_list():
            if block.get_x() <= self.__field.get_v_boarder():
                return
            left_block_check_index_x = block.get_x()//block.get_w() - 1
            left_block_check_index_y = block.get_y()//block.get_h()
            if self.__block_field.get_block_field()[left_block_check_index_y][left_block_check_index_x] == 1:
                return
        self.__x -= self.__block_w

    def move_right(self) -> None:
        for block in self.__generate_block_list():
            if block.get_x() >= self.__field.get_w() + self.__field.get_v_boarder() - self.__block_w:
                return
            left_block_check_index_x = block.get_x()//block.get_w() + 1
            left_block_check_index_y = block.get_y()//block.get_h()
            if self.__block_field.get_block_field()[left_block_check_index_y][left_block_check_index_x] == 1:
                return
        self.__x += self.__block_w

    def figure_stand(self) -> None:
        """Transforms current figure to static blocks and creates new one """
        for block in self.__generate_block_list():
            """Changes field list from 0 to 1 for filled brick"""
            a = self.__block_field.get_block_field()
            a[block.get_y() // block.get_h()][block.get_x() // block.get_w()] = 1
            self.__block_field.set_block_field(a)

    def get_block_w(self):
        return self.__block_w

    def get_block_h(self):
        return self.__block_h

    def rotated_figure(self):
        a = array(self.__config)
        b = rot90(a, 1)
        for i, fig_row in enumerate(b):
            for j, el in enumerate(fig_row):
                if el == 1:
                    if self.__block_field.get_block_field()[int(self.__y // self.__block_h + i)][int(self.__x // self.__block_w + j)] == 1:
                        return a
        return list(b)

    def set_config(self, con):
        self.__config = con
