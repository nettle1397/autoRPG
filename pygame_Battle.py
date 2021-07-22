# -*- coding: utf-8 -*-
import pygame as pg
from os import path

class BasicAttributes:
    WIDTH = 720 # 遊戲畫面寬
    HEIGHT = 480 # 遊戲畫面高
    FPS = 30 # 遊戲畫面幀數

    WHITE = (255, 255, 255, 255)
    BLACK = (0, 0, 0, 255)
    GRAY = (128, 128, 128, 255)
    RED = (255, 0, 0, 255)
    GREEN = (0, 255, 0, 255)
    BLUE = (0, 0, 255, 255)
    MEDIUM_BLUE = (0, 0, 205, 255)
    NAVY_BLUE = (0, 0, 128, 200)
    YELLOW = (255, 255, 0, 255)
    CYAN = (255, 0, 255, 255)
    MAGENTA = (0, 255, 255, 255)
    TRANSPARENT = (0, 0, 0, 0)

    image_dir = path.join(path.dirname(__file__), "image")
"""
繪製文字需要的資訊
text_attributes = {
"font":"Text_Fonts/NotoSansCJKtc-Medium.otf",
"text":"a",
"size":0,
"color":BLACK,
"xy":(0, 0)
}
"""
class DrawText:
    def __init__(self, text_attributes):
        self.font = pg.font.Font(text_attributes["font"], text_attributes["size"])
        self.text_surface = self.font.render(text_attributes["text"], True, text_attributes["color"])
        self.text_rect = self.text_surface.get_rect()
        self.text_rect.center = text_attributes["xy"]

class InterfaceMainPicture(pg.sprite.Sprite): # 主視窗，顯示敵人外貌，以及雙方資源。
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface(
                                (
                                BasicAttributes.WIDTH -
                                BasicAttributes.WIDTH // 18,
                                BasicAttributes.HEIGHT // 1.5 -
                                BasicAttributes.HEIGHT // 15
                                )
                                )
        self.image.fill(BasicAttributes.GREEN)
        self.rect = self.image.get_rect()
        self.rect.top = BasicAttributes.HEIGHT // 32
        self.rect.left = BasicAttributes.WIDTH // 36
        super().__init__()

class InterfaceMenu(pg.sprite.Sprite): # 選單視窗，戰鬥動作、資訊以及系統選單。
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface(
                                (
                                BasicAttributes.WIDTH // 3 -
                                BasicAttributes.WIDTH // 24,
                                BasicAttributes.HEIGHT // 3 -
                                BasicAttributes.HEIGHT // 30
                                )
                                )
        self.image.fill(BasicAttributes.CYAN)
        self.rect = self.image.get_rect()
        self.rect.top = BasicAttributes.HEIGHT // 1.5
        self.rect.left = BasicAttributes.WIDTH // 36
        super().__init__()

class InterfaceInfo(pg.sprite.Sprite): # 訊息視窗，顯示所選選單對應的訊息。
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface(
                                (
                                BasicAttributes.WIDTH // 1.5 -
                                BasicAttributes.WIDTH // 24,
                                BasicAttributes.HEIGHT // 3 -
                                BasicAttributes.HEIGHT // 30
                                )
                                )
        self.image.fill(BasicAttributes.MAGENTA)
        self.rect = self.image.get_rect()
        self.rect.top = BasicAttributes.HEIGHT // 1.5
        self.rect.right = BasicAttributes.WIDTH - BasicAttributes.WIDTH // 36

class MenuButton(InterfaceMenu): # 選單按鈕
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        super().__init__()
        IFM = self.rect.top
        self.image = pg.Surface(
                                (
                                self.rect[2] * 0.8,
                                self.rect[3] // 6.8
                                )
                                )
        self.image.fill(BasicAttributes.BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (x, IFM + y)

    def update(self):
        pass

class MenuButtonCursor(InterfaceMenu): # 選單按鈕
    def __init__(self, x, y, cursor_y):
        pg.sprite.Sprite.__init__(self)
        super().__init__()
        IFM = self.rect.top
        self.image = pg.Surface(
                                (
                                self.rect[2] * 0.8,
                                self.rect[3] // 6.8
                                ),
                                pg.SRCALPHA # 接受透明度
                                )
        self.image.fill(BasicAttributes.WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (x, IFM + y)
        self.cursor_y = cursor_y
        self.cursory = self.cursor_y[0]
        self.n = 0

    def update(self):
        C = pg.time.Clock()
        keystate = pg.key.get_pressed()
        if keystate[pg.K_UP]:
            if self.cursory == self.cursor_y[0]:
                self.cursory = self.cursor_y[-1]
                self.n = 4
            elif  self.cursory == self.cursor_y[self.n]:
                self.n = self.n - 1
                self.cursory = self.cursor_y[self.n]
            self.rect.centery = self.cursory
            C.tick(6)

        if keystate[pg.K_DOWN]:
            if self.cursory == self.cursor_y[-1]:
                self.cursory = self.cursor_y[0]
                self.n = 0
            elif  self.cursory == self.cursor_y[self.n]:
                self.n = self.n + 1
                self.cursory = self.cursor_y[self.n]
            self.rect.centery = self.cursory
            C.tick(6)

class Mob(InterfaceMainPicture): # 敵人圖像
    def __init__(self, x):
        pg.sprite.Sprite.__init__(self)
        super().__init__()
        self.image = pg.Surface(
                                (
                                self.rect[2] // 5.9,
                                self.rect[3] // 1.5
                                ),
                                pg.SRCALPHA # 接受透明度
                                )
        self.image.fill(BasicAttributes.BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (x, self.rect[3] // 1.5)

    def update(self):
        transparent = False
        if transparent:
            self.image.set_colorkey((0, 0, 0)) # 透明化

class MobEmptyHP(InterfaceMainPicture):
    def __init__(self, xy):
        pg.sprite.Sprite.__init__(self)
        super().__init__()
        self.image = pg.Surface(
                                (
                                self.rect[2] // 5.9,
                                self.rect[3] // 20
                                )
                                )
        self.image.fill(BasicAttributes.GRAY)
        self.rect = self.image.get_rect()
        self.rect.midtop = xy

    def update(self):
        pass

class MobSolidHP(InterfaceMainPicture):
    def __init__(self, xy):
        pg.sprite.Sprite.__init__(self)
        super().__init__()
        self.image = pg.Surface(
                                (
                                self.rect[2] // 5.9,
                                self.rect[3] // 20
                                )
                                )
        self.image.fill(BasicAttributes.RED)
        self.rect = self.image.get_rect()
        self.rect.midtop = xy

    def update(self):
        pass

class HeroEmptyHP(InterfaceMainPicture):
    def __init__(self, x):
        pg.sprite.Sprite.__init__(self)
        super().__init__()
        y = self.rect.bottom
        self.image = pg.Surface(
                                (
                                self.rect[2] // 3.5,
                                self.rect[3] // 20
                                )
                                )
        self.image.fill(BasicAttributes.GRAY)
        self.rect = self.image.get_rect()
        self.rect.midbottom = (x, y - self.rect.height)

class HeroSolidHP(InterfaceMainPicture):
    def __init__(self, x):
        pg.sprite.Sprite.__init__(self)
        super().__init__()
        y = self.rect.bottom
        self.image = pg.Surface(
                                (
                                self.rect[2] // 3.5,
                                self.rect[3] // 20
                                ),
                                pg.SRCALPHA
                                )
        self.image.fill(BasicAttributes.RED)
        self.rect = self.image.get_rect()
        self.rect.midbottom = (x, y - self.rect.height)

    def update(self):
        pass

class HeroEmptyMP(InterfaceMainPicture):
    def __init__(self, x):
        pg.sprite.Sprite.__init__(self)
        super().__init__()
        y = self.rect.bottom
        self.image = pg.Surface(
                                (
                                self.rect[2] // 3.5,
                                self.rect[3] // 20
                                )
                                )
        self.image.fill(BasicAttributes.GRAY)
        self.rect = self.image.get_rect()
        self.rect.midbottom = (x, y)

class HeroSolidMP(InterfaceMainPicture):
    def __init__(self, x):
        pg.sprite.Sprite.__init__(self)
        super().__init__()
        y = self.rect.bottom
        self.image = pg.Surface(
                                (
                                self.rect[2] // 3.5,
                                self.rect[3] // 20
                                )
                                )
        self.image.fill(BasicAttributes.MEDIUM_BLUE)
        self.rect = self.image.get_rect()
        self.rect.midbottom = (x, y)
    
    def update(self):
        pass

class GameRun(BasicAttributes):
    pg.init() # pygame初始化
    pg.mixer.init() # pygame的音效初始化
    screen = pg.display.set_mode((BasicAttributes.WIDTH, BasicAttributes.HEIGHT)) # 依設定顯示視窗
    pg.display.set_caption("Test_Game") # 設定視窗標題
    screen.fill(BasicAttributes.WHITE)
    screen.fill(BasicAttributes.BLACK)
    # screen_a = screen.convert_alpha()
    clock = pg.time.Clock()
    
    all_sprites = pg.sprite.Group()
    interface_main_picture = InterfaceMainPicture()
    interface_menu = InterfaceMenu()
    interface_info = InterfaceInfo()
    menu_button_1 = MenuButton( # 選單按鈕位置
                                interface_menu.rect.centerx,
                                
                                interface_menu.rect[3] // 6
                                )
    text_attributes_1 = {
                        "font":"Text_Fonts/NotoSansCJKtc-Medium.otf",
                        "text":"測試_Test_1",
                        "size":16,
                        "color":BasicAttributes.RED,
                        "xy":menu_button_1.rect.center
                        }
    menu_button_text_1 = DrawText(text_attributes_1)
    menu_button_2 = MenuButton(
                                interface_menu.rect.centerx,
                                
                                interface_menu.rect[3] // 3
                                )
    text_attributes_2 = {
                        "font":"Text_Fonts/NotoSansCJKtc-Medium.otf",
                        "text":"測試_Test_2",
                        "size":16,
                        "color":BasicAttributes.RED,
                        "xy":menu_button_2.rect.center
                        }
    menu_button_text_2 = DrawText(text_attributes_2)
    menu_button_3 = MenuButton(
                                interface_menu.rect.centerx,
                                interface_menu.rect[3] // 2
                                )
    text_attributes_3 = {
                        "font":"Text_Fonts/NotoSansCJKtc-Medium.otf",
                        "text":"測試_Test_3",
                        "size":16,
                        "color":BasicAttributes.RED,
                        "xy":menu_button_3.rect.center
                        }
    menu_button_text_3 = DrawText(text_attributes_3)
    menu_button_4 = MenuButton(
                                interface_menu.rect.centerx,
                                
                                interface_menu.rect[3] // 1.5
                                )
    text_attributes_4 = {
                        "font":"Text_Fonts/NotoSansCJKtc-Medium.otf",
                        "text":"測試_Test_4",
                        "size":16,
                        "color":BasicAttributes.RED,
                        "xy":menu_button_4.rect.center
                        }
    menu_button_text_4 = DrawText(text_attributes_4)
    menu_button_5 = MenuButton(
                                interface_menu.rect.centerx,
                                
                                interface_menu.rect[3] // 1.2
                                )
    text_attributes_5 = {
                        "font":"Text_Fonts/NotoSansCJKtc-Medium.otf",
                        "text":"測試_Test_5",
                        "size":16,
                        "color":BasicAttributes.RED,
                        "xy":menu_button_5.rect.center
                        }
    menu_button_text_5 = DrawText(text_attributes_5)
    button_cursor_y = [
            menu_button_1.rect.centery,
            menu_button_2.rect.centery,
            menu_button_3.rect.centery,
            menu_button_4.rect.centery,
            menu_button_5.rect.centery
            ]
    menu_button_cursor = MenuButtonCursor( # 選單按鈕位置
                                interface_menu.rect.centerx,
                                interface_menu.rect[3] // 6,
                                button_cursor_y
                                )

    mobs_1 = Mob(
                interface_main_picture.rect.left +
                interface_main_picture.rect[2] // 10
                )
    mobs_2 = Mob(
                interface_main_picture.rect.left +
                interface_main_picture.rect[2] // 3.35
                )
    mobs_3 = Mob(interface_main_picture.rect.centerx)
    mobs_4 = Mob(
                interface_main_picture.rect.left +
                interface_main_picture.rect[2] // 1.43
                )
    mobs_5 = Mob(
                interface_main_picture.rect.left +
                interface_main_picture.rect[2] // 1.11
                )

    heros_empty_HP_1 = HeroEmptyHP(
                                    interface_main_picture.rect.left +
                                    interface_main_picture.rect[2] // 6
                                    )
    heros_empty_HP_2 = HeroEmptyHP(
                                    interface_main_picture.rect.left +
                                    interface_main_picture.rect[2] // 2
                                    )
    heros_empty_HP_3 = HeroEmptyHP(
                                    interface_main_picture.rect.left +
                                    interface_main_picture.rect[2] // 1.2
                                    )

    heros_solid_HP_1 = HeroSolidHP(
                                    interface_main_picture.rect.left +
                                    interface_main_picture.rect[2] // 6
                                    )
    heros_solid_HP_2 = HeroSolidHP(
                                    interface_main_picture.rect.left +
                                    interface_main_picture.rect[2] // 2
                                    )
    heros_solid_HP_3 = HeroSolidHP(
                                    interface_main_picture.rect.left +
                                    interface_main_picture.rect[2] // 1.2
                                    )

    heros_empty_MP_1 = HeroEmptyMP(
                                    interface_main_picture.rect.left +
                                    interface_main_picture.rect[2] // 6
                                    )
    heros_empty_MP_2 = HeroEmptyMP(
                                    interface_main_picture.rect.left +
                                    interface_main_picture.rect[2] // 2
                                    )
    heros_empty_MP_3 = HeroEmptyMP(
                                    interface_main_picture.rect.left +
                                    interface_main_picture.rect[2] // 1.2
                                    )

    heros_solid_MP_1 = HeroSolidMP(
                                    interface_main_picture.rect.left +
                                    interface_main_picture.rect[2] // 6
                                    )
    heros_solid_MP_2 = HeroSolidMP(
                                    interface_main_picture.rect.left +
                                    interface_main_picture.rect[2] // 2
                                    )
    heros_solid_MP_3 = HeroSolidMP(
                                    interface_main_picture.rect.left +
                                    interface_main_picture.rect[2] // 1.2
                                    )

    mobs_empty_HP_1 = MobEmptyHP(mobs_1.rect.midtop)
    mobs_empty_HP_2 = MobEmptyHP(mobs_2.rect.midtop)
    mobs_empty_HP_3 = MobEmptyHP(mobs_3.rect.midtop)
    mobs_empty_HP_4 = MobEmptyHP(mobs_4.rect.midtop)
    mobs_empty_HP_5 = MobEmptyHP(mobs_5.rect.midtop)

    mobs_solid_HP_1 = MobSolidHP(mobs_1.rect.midtop)
    mobs_solid_HP_2 = MobSolidHP(mobs_2.rect.midtop)
    mobs_solid_HP_3 = MobSolidHP(mobs_3.rect.midtop)
    mobs_solid_HP_4 = MobSolidHP(mobs_4.rect.midtop)
    mobs_solid_HP_5 = MobSolidHP(mobs_5.rect.midtop)

    all_sprites.add(interface_main_picture)
    all_sprites.add(interface_menu)
    all_sprites.add(interface_info)

    all_sprites.add(menu_button_1)
    all_sprites.add(menu_button_2)
    all_sprites.add(menu_button_3)
    all_sprites.add(menu_button_4)
    all_sprites.add(menu_button_5)

    all_sprites.add(menu_button_cursor)

    all_sprites.add(mobs_1)
    all_sprites.add(mobs_2)
    all_sprites.add(mobs_3)
    all_sprites.add(mobs_4)
    all_sprites.add(mobs_5)

    all_sprites.add(heros_empty_HP_1)
    all_sprites.add(heros_empty_HP_2)
    all_sprites.add(heros_empty_HP_3)

    all_sprites.add(heros_solid_HP_1)
    all_sprites.add(heros_solid_HP_2)
    all_sprites.add(heros_solid_HP_3)

    all_sprites.add(heros_empty_MP_1)
    all_sprites.add(heros_empty_MP_2)
    all_sprites.add(heros_empty_MP_3)

    all_sprites.add(heros_solid_MP_1)
    all_sprites.add(heros_solid_MP_2)
    all_sprites.add(heros_solid_MP_3)

    all_sprites.add(mobs_empty_HP_1)
    all_sprites.add(mobs_empty_HP_2)
    all_sprites.add(mobs_empty_HP_3)
    all_sprites.add(mobs_empty_HP_4)
    all_sprites.add(mobs_empty_HP_5)

    all_sprites.add(mobs_solid_HP_1)
    all_sprites.add(mobs_solid_HP_2)
    all_sprites.add(mobs_solid_HP_3)
    all_sprites.add(mobs_solid_HP_4)
    all_sprites.add(mobs_solid_HP_5)

    running = True
    while running:
        clock.tick(BasicAttributes.FPS) # 計算幀數
        for event in pg.event.get(): # 按下關閉視窗的判斷
            if event.type == pg.QUIT:
                running = False # 結束遊戲循環

        all_sprites.update() # 每幀更新一次

        # screen.blit(screen_a,(0,0))
        all_sprites.draw(screen) # 繪製範圍，通常是視窗內。
        screen.blit(menu_button_text_1.text_surface,
                    menu_button_text_1.text_rect)
        screen.blit(menu_button_text_2.text_surface,
                    menu_button_text_2.text_rect)
        screen.blit(menu_button_text_3.text_surface,
                    menu_button_text_3.text_rect)
        screen.blit(menu_button_text_4.text_surface,
                    menu_button_text_4.text_rect)
        screen.blit(menu_button_text_5.text_surface,
                    menu_button_text_5.text_rect)
        
        pg.display.flip() # 每次更新繪製或渲染一次
    pg.quit()
        
GameRun()