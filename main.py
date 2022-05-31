from ursina import *

game = Ursina()

board = Entity(model='plane', texture='boardtex')
board.position = (0,0,0)
board.scale = 25

camera.orthographic = True
camera.position = (0,1,0)
camera.look_at(board)
camera.fov = 30

lobbyButton = Button(text='Enter')
playerCount = InputField(name='playerfield')
playerCountCheck = WindowPanel(
    title='Players of Current Session',
    content=
    (
        Text("Enter the amount of players (Max 4)"),
        playerCount,
        lobbyButton
    )
)
lobbyButton.on_click = playerCountCheck.close

def update():
    print(playerCount)

game.run()
