from pygame.locals import *
import pygame

BLACK = Color(0, 0, 0)
YELLOW = Color(255, 255, 0)
FPS = 30
POS_CHANGE = 3


class Up:
    def update_axis(self, obj):
        obj.y -= 1

    def update_pos(self, obj):
        obj.robot_y -= POS_CHANGE

    def keep_moving(self, obj):
        return obj.robot_y > obj.window.img_pos_axis_epsilon(obj.y)


class Right:
    def update_axis(self, obj):
        obj.x += 1

    def update_pos(self, obj):
        obj.robot_x += POS_CHANGE

    def keep_moving(self, obj):
        return obj.robot_x < obj.window.img_pos_axis_epsilon(obj.x)

class Down:
    def update_axis(self, obj):
        obj.y += 1

    def update_pos(self, obj):
        obj.robot_y += POS_CHANGE

    def keep_moving(self, obj):
        return obj.robot_y < obj.window.img_pos_axis_epsilon(obj.y)


class Left:
    def update_axis(self, obj):
        obj.x -= 1

    def update_pos(self, obj):
        obj.robot_x -= POS_CHANGE

    def keep_moving(self, obj):
        return obj.robot_x > obj.window.img_pos_axis_epsilon(obj.x)

class Window:
    def __init__(self, windowSize):
        self.windowSize = windowSize

    def size(self):
        return self.windowSize

    def rect(self):
        return (self.windowSize, self.windowSize)

    def img_size_within_square(self):
        return int(self.windowSize / 3 * 0.6)

    def img_pos_within_square(self, x, y):
        return self.img_pos_axis_epsilon(x), self.img_pos_axis_epsilon(y)

    def img_pos_axis_epsilon(self, x):
        return int(x * self.windowSize / 3 + self.windowSize / 3 * 0.2)

    def img_pos_axis(self, x):
        return int(x * self.windowSize / 3)

class Robot:
    def __init__(self, window, display_surf):
        self.window = window
        self.display_surf = display_surf
        self.image_surf = pygame.image.load("droid2.png").convert()
        self.robot_size = window.img_size_within_square()
        self.image_surf = pygame.transform.scale(self.image_surf, (self.robot_size, self.robot_size))
        self.x, self.y = 0, 0
        self.robot_x, self.robot_y = window.img_pos_within_square(self.x, self.y)
        self.display_surf.blit(self.image_surf, (self.robot_x, self.robot_y))

    def move(self, refresh, m):
        m.update_axis(self)
        while m.keep_moving(self):
            pygame.draw.rect(self.display_surf, BLACK, (
                self.robot_x, self.robot_y, self.robot_x + self.robot_size, self.robot_y + self.robot_size))
            m.update_pos(self)
            self.display_surf.blit(self.image_surf, (self.robot_x, self.robot_y))
            refresh()
            pygame.display.update()
            pygame.time.delay(100)

class App:
    def __init__(self):
        self.window = Window(300)
        self.running = False

    def on_init(self):
        pygame.init()
        self.display_surf = pygame.display.set_mode(self.window.rect(), pygame.HWSURFACE)
        self.refresh()
        pygame.display.flip()
        pygame.display.set_caption('Robot moving')
        self.robot = Robot(self.window, self.display_surf)

    def refresh(self):
        pygame.draw.line(self.display_surf, YELLOW, (self.window.img_pos_axis(1), 0), (self.window.img_pos_axis(1), self.window.size()))
        pygame.draw.line(self.display_surf, YELLOW, (self.window.img_pos_axis(2), 0), (self.window.img_pos_axis(2), self.window.size()))
        pygame.draw.line(self.display_surf, YELLOW, (0, self.window.img_pos_axis(1)), (self.window.size(), self.window.img_pos_axis(1)))
        pygame.draw.line(self.display_surf, YELLOW, (0, self.window.img_pos_axis(2)), (self.window.size(), self.window.img_pos_axis(2)))

    def on_event(self, event):
        if event.type == QUIT:
            self.running = False

    def on_loop(self):
        pass

    def on_render(self):
        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self, moves):
        self.on_init()
        self.running = True
        start = False
        while not start:
            pygame.time.delay(1000)
            for event in pygame.event.get():
                if event.type == KEYUP:
                    start = True
        for m in moves:
            for event in pygame.event.get():
                self.on_event(event)
            self.robot.move(self.refresh, m)
        pygame.time.delay(2000)
        self.on_cleanup()


if __name__ == "__main__":
    app = App()
    app.on_execute([Down(), Down(), Right(), Right()])
