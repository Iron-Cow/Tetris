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

