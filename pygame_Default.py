# -*- coding: utf-8 -*-
import pygame as pg
from os import path

class BasicAttributes:
    WIDTH = 720 # 遊戲畫面寬
    HEIGHT = 480 # 遊戲畫面高
    FPS = 60 # 遊戲畫面幀數

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)
    CYAN = (255, 0, 255)
    MAGENTA = (0, 255, 255)
    
    image_dir = path.join(path.dirname(__file__), "image")
    # fonts_dir = path.join(path.dirname(__file__), "Text_Fonts")

    text_attributes = {
    "font":"Text_Fonts/NotoSansCJKtc-Medium.otf",
    "text":"Good morning 早安",
    "size":36,
    "color":RED,
    "xy":(360, 120)}

# text_attributes = {
# "font":"Text_Fonts/NotoSansCJKtc-Medium.otf",
# "text":"a",
# "size":0,
# "color":(0, 0, 0),
# "xy":(0, 0)}
class DrawText:
    def __init__(self, surface, text_attributes):
        self.font = pg.font.Font(text_attributes["font"], text_attributes["size"])
        self.text_surface = self.font.render(text_attributes["text"], True, text_attributes["color"])
        self.text_rect = self.text_surface.get_rect()
        self.text_rect.midtop = text_attributes["xy"]
        surface.blit(self.text_surface, self.text_rect)

class InterfaceMainPicture(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((670, 280))
        self.image.fill(BasicAttributes.GREEN)
        self.rect = self.image.get_rect()
        self.rect.top = 20
        self.rect.left = 25
        
class GameRun(BasicAttributes):
    pg.init() # pygame初始化
    pg.mixer.init() # pygame的音效初始化
    screen = pg.display.set_mode((BasicAttributes.WIDTH, BasicAttributes.HEIGHT)) # 依設定顯示視窗
    pg.display.set_caption("自走冒險") # 設定視窗標題
    clock = pg.time.Clock()
    
    all_sprites = pg.sprite.Group()
    interface_main_picture = InterfaceMainPicture()
    all_sprites.add(interface_main_picture)

    running = True
    while running:
        clock.tick(BasicAttributes.FPS) # 計算幀數
        for event in pg.event.get(): # 按下關閉視窗的判斷
            if event.type == pg.QUIT:
                running = False # 結束遊戲循環

        all_sprites.update() # 每幀更新一次

        screen.fill(BasicAttributes.BLACK)
        all_sprites.draw(screen) # 繪製範圍，通常是視窗內。
        DrawText(screen, BasicAttributes.text_attributes)
        pg.display.flip() # 每次更新繪製或渲染一次
    pg.quit()
        
GameRun()