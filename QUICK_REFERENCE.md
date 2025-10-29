# 快速参考卡

## 文件一览

| 文件 | 用途 | 行数 |
|------|------|------|
| `gomoku_game.py` | 游戏逻辑和规则 | 171 |
| `gomoku_gui.py` | 图形用户界面 | 387 |
| `run_game.bat` | Windows 快速启动 | - |
| `requirements.txt` | Python 依赖库 | - |
| `README.md` | 项目说明 | - |
| `REFACTOR_NOTES.md` | 重构详解和扩展指南 | - |

## 文件职责

### gomoku_game.py
**职责**：管理游戏状态和规则

```python
# 创建游戏实例
game = GomokuGame(board_size=15)

# 放置棋子
success, result = game.make_move(7, 7)
if success:
    if result == "WIN":
        print(f"玩家 {game.winner.name} 获胜！")

# 悔棋
success, msg = game.undo_move()

# 查询状态
board = game.get_board()
history = game.get_move_history()
state = game.get_game_state()
```

### gomoku_gui.py
**职责**：提供用户界面和交互

```python
# 创建 GUI
root = tk.Tk()
gui = GomokuGUI(root)

# 内部使用 self.game 对象
gui.game.make_move(row, col)

# GUI 负责
# - 绘制棋盘和棋子
# - 处理鼠标事件
# - 显示游戏信息
# - 更新界面
root.mainloop()
```

## 常见操作

### 启动游戏
```bash
# 方法 1：双击 run_game.bat

# 方法 2：命令行
python gomoku_gui.py

# 方法 3：Python IDE
运行 gomoku_gui.py
```

### 添加新功能（以 AI 为例）

#### 步骤 1：创建 gomoku_ai.py
```python
from gomoku_game import GomokuGame, Player

class GomokuAI:
    def __init__(self, game):
        self.game = game
    
    def get_best_move(self):
        # 实现 AI 逻辑
        pass
```

#### 步骤 2：在 gomoku_gui.py 中导入并使用
```python
from gomoku_ai import GomokuAI

class GomokuGUI:
    def __init__(self, root):
        # ...
        self.game = GomokuGame()
        self.ai = GomokuAI(self.game)
    
    def ai_move(self):
        row, col = self.ai.get_best_move()
        self.game.make_move(row, col)
```

## 关键方法速查

### GomokuGame
```python
make_move(row, col)           # 放置棋子
undo_move()                   # 撤销上一步
check_win(row, col, player)   # 检查是否获胜
reset()                       # 重置游戏
get_board()                   # 获取棋盘状态
get_move_history()            # 获取移动历史
get_game_state()              # 获取完整游戏状态
```

### GomokuGUI
```python
draw_board()                  # 重绘棋盘
draw_piece(row, col, player)  # 绘制棋子
on_canvas_click(event)        # 处理点击事件
update_ui()                   # 更新 UI
reset_game()                  # 重置游戏
undo_move()                   # 悔棋
```

## 调试技巧

### 查看游戏状态
```python
from gomoku_game import GomokuGame

game = GomokuGame()
game.make_move(7, 7)
game.make_move(7, 8)

# 打印棋盘
print(game.get_board())

# 查看移动历史
print(game.get_move_history())

# 获取完整状态
state = game.get_game_state()
print(f"当前玩家: {state['current_player']}")
print(f"移动次数: {state['move_count']}")
print(f"游戏结束: {state['game_over']}")
```

### 运行测试
```python
# 创建 test_gomoku.py
import unittest
from gomoku_game import GomokuGame, Player

class TestGomokuGame(unittest.TestCase):
    def test_make_move(self):
        game = GomokuGame()
        success, result = game.make_move(7, 7)
        self.assertTrue(success)
        self.assertEqual(result, "OK")
    
    def test_win_detection(self):
        game = GomokuGame()
        # 放置 5 个黑子
        for i in range(5):
            game.make_move(7, 7 + i)
            if game.current_player == Player.BLACK:
                break
        self.assertTrue(game.game_over)

# 运行测试
if __name__ == '__main__':
    unittest.main()
```

## 项目信息

- **总代码行数**: 558 行
- **文件数**: 6 个
- **主要依赖**: numpy, tkinter（内置）
- **Python 版本**: 3.7+
- **开发时间**: 2025-10-29
- **版本**: 2.1（重构版）

---

**需要帮助？** 查看 REFACTOR_NOTES.md 了解更多细节。
