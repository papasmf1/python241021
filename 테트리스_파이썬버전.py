import pygame
import random

# 색상 정의
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLORS = [
    (0, 255, 255),
    (255, 255, 0),
    (128, 0, 128),
    (0, 255, 0),
    (255, 0, 0),
    (0, 0, 255),
    (255, 127, 0)
]

# 게임 설정
BLOCK_SIZE = 30
FIELD_WIDTH = 10
FIELD_HEIGHT = 20
GAME_WIDTH = FIELD_WIDTH * BLOCK_SIZE
GAME_HEIGHT = FIELD_HEIGHT * BLOCK_SIZE

# 테트로미노 모양
SHAPES = [
    [[1, 1, 1, 1]],
    [[1, 1], [1, 1]],
    [[1, 1, 1], [0, 1, 0]],
    [[1, 1, 1], [1, 0, 0]],
    [[1, 1, 1], [0, 0, 1]],
    [[1, 1, 0], [0, 1, 1]],
    [[0, 1, 1], [1, 1, 0]]
]

class Tetromino:
    def __init__(self):
        self.shape = random.choice(SHAPES)
        self.color = random.choice(COLORS)
        self.x = FIELD_WIDTH // 2 - len(self.shape[0]) // 2
        self.y = 0

    def rotate(self):
        self.shape = list(zip(*self.shape[::-1]))

class Tetris:
    def __init__(self):
        self.field = [[0] * FIELD_WIDTH for _ in range(FIELD_HEIGHT)]
        self.current_piece = Tetromino()
        self.score = 0

    def new_piece(self):
        self.current_piece = Tetromino()
        if self.collision():
            return False
        return True

    def collision(self):
        for y, row in enumerate(self.current_piece.shape):
            for x, cell in enumerate(row):
                if cell and (
                    x + self.current_piece.x < 0
                    or x + self.current_piece.x >= FIELD_WIDTH
                    or y + self.current_piece.y >= FIELD_HEIGHT
                    or self.field[y + self.current_piece.y][x + self.current_piece.x]
                ):
                    return True
        return False

    def merge(self):
        for y, row in enumerate(self.current_piece.shape):
            for x, cell in enumerate(row):
                if cell:
                    self.field[y + self.current_piece.y][x + self.current_piece.x] = self.current_piece.color

    def remove_lines(self):
        lines = 0
        for i in range(FIELD_HEIGHT):
            if all(self.field[i]):
                del self.field[i]
                self.field.insert(0, [0] * FIELD_WIDTH)
                lines += 1
        self.score += lines ** 2 * 100

    def move(self, dx, dy):
        self.current_piece.x += dx
        self.current_piece.y += dy
        if self.collision():
            self.current_piece.x -= dx
            self.current_piece.y -= dy
            if dy > 0:
                self.merge()
                self.remove_lines()
                if not self.new_piece():
                    return False
        return True

    def rotate(self):
        old_shape = self.current_piece.shape
        self.current_piece.rotate()
        if self.collision():
            self.current_piece.shape = old_shape

def main():
    pygame.init()
    screen = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
    pygame.display.set_caption("테트리스")
    clock = pygame.time.Clock()
    game = Tetris()
    fall_time = 0
    fall_speed = 0.5  # 초당 한 칸씩 떨어짐

    while True:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    game.move(-1, 0)
                elif event.key == pygame.K_RIGHT:
                    game.move(1, 0)
                elif event.key == pygame.K_DOWN:
                    game.rotate()
                elif event.key == pygame.K_UP:
                    game.current_piece.rotate()
                    game.current_piece.rotate()
                    game.current_piece.rotate()

        fall_time += clock.get_rawtime()
        clock.tick()

        if fall_time / 1000 > fall_speed:
            if not game.move(0, 1):
                print(f"게임 오버! 점수: {game.score}")
                return
            fall_time = 0

        for y, row in enumerate(game.field):
            for x, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(screen, cell, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
                    pygame.draw.rect(screen, WHITE, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 1)

        for y, row in enumerate(game.current_piece.shape):
            for x, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(screen, game.current_piece.color,
                                     ((x + game.current_piece.x) * BLOCK_SIZE,
                                      (y + game.current_piece.y) * BLOCK_SIZE,
                                      BLOCK_SIZE, BLOCK_SIZE))
                    pygame.draw.rect(screen, WHITE,
                                     ((x + game.current_piece.x) * BLOCK_SIZE,
                                      (y + game.current_piece.y) * BLOCK_SIZE,
                                      BLOCK_SIZE, BLOCK_SIZE), 1)

        pygame.display.flip()

if __name__ == "__main__":
    main()