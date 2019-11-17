import pygame


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
        pygame.draw.rect(surface=surface, rect=[self.__x, self.__y, self.__w, self.__h], color=self.__color)

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
    def __init__(self, surface, x: float, y: float,  name: str, config: list, color: tuple, field: Field,
                 block_field, block_w: float = 50, block_h: float = 50, ):
        self.__surface = surface
        self.__x = x
        self.__y = y
        self.__name = name
        self.__config = config
        self.__color = color
        self.__field = field
        self.__block_w = block_w
        self.__block_h = block_h
        self.__block_field = block_field

        """[[0, 0, 0],
            [1, 0, 0], 
            [1, 1, 1]]"""

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
        for block in self.__generate_block_list():
            try:
                # if block under current if empty - block can be dropped
                if self.__block_field[block.get_y() // block.get_h() + 1][block.get_x() // block.get_w()] == 0:
                    pass
                # else: block reached filled block and should be marked as filled also + initiate new block
                else:
                    # add_square(self.__field, block)
                    block = Block(260, 60, 50, 50, (255, 255, 255), self.__surface)

            except IndexError:  # block reached ground
                return
        self.__y += self.__block_h
            # block.draw_block(self.__surface)

    def move_left(self) -> None:
        for block in self.__generate_block_list():
            if block.get_x() <= self.__field.get_v_boarder():
                return
        self.__x -= self.__block_w

    def move_right(self) -> None:
        for block in self.__generate_block_list():
            if block.get_x() >= self.__field.get_w() + self.__field.get_v_boarder() - self.__block_w:
                return
        self.__x += self.__block_w

