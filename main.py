import pygame
import sys

# --- 配置常量 (模拟 config.py) ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# 颜色常量
COLOR_WHITE = (255, 255, 255)
COLOR_RED = (255, 0, 0)
COLOR_GREEN = (0, 255, 0)
COLOR_BLACK = (0, 0, 0)


class JeopardyGame:
    """
    游戏主类：负责管理游戏状态、循环和组件协调
    """

    def __init__(self):
        # 1. 初始化 Pygame
        pygame.init()

        # 2. 设置窗口
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Jeopardy! Project Framework")
        self.clock = pygame.time.Clock()

        # 3. 游戏状态变量 (封装在类内部)
        self.running = True
        self.player_rect = pygame.Rect(100, 100, 50, 50)
        self.player_color = COLOR_RED
        self.fps = FPS

        # 4. 资源预加载 (字体只需加载一次)
        self.font = pygame.font.SysFont("Arial", 24)

    def handle_events(self):
        """处理用户输入事件"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self._toggle_color()  # 调用内部辅助方法
                elif event.key == pygame.K_ESCAPE:
                    self.running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # 左键
                    self._move_player(event.pos)

    def _toggle_color(self):
        """辅助方法：切换颜色"""
        print("空格键被按下！颜色改变。")
        self.player_color = COLOR_GREEN if self.player_color == COLOR_RED else COLOR_RED

    def _move_player(self, pos):
        """辅助方法：移动玩家"""
        print(f"鼠标左键点击在: {pos}")
        self.player_rect.center = pos

    def update(self):
        """
        更新游戏逻辑
        注意：这里适合放随时间变化的逻辑（如倒计时、自动动画）
        而不是瞬间的按键反应
        """
        pass

    def draw(self):
        """渲染画面"""
        # 1. 清空屏幕
        self.screen.fill(COLOR_WHITE)

        # 2. 绘制游戏对象
        pygame.draw.rect(self.screen, self.player_color, self.player_rect)

        # 3. 绘制 UI 文本
        text_surface = self.font.render("Press SPACE to change color | Click to move", True, COLOR_BLACK)
        self.screen.blit(text_surface, (10, 10))

    def run(self):
        """主游戏循环"""
        while self.running:
            self.handle_events()
            self.update()
            self.draw()

            # 刷新显示
            pygame.display.flip()
            self.clock.tick(self.fps)

        self.cleanup()

    def cleanup(self):
        """清理资源"""
        pygame.quit()
        sys.exit()


def main():
    # 实例化并运行游戏
    # 类定义在外部，这里非常干净
    game = JeopardyGame()
    game.run()

