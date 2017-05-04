class Config(object):
	"""
	Number markers to know what tile contains what
	"""
	GROUND = 0
	WALL = 1
	BRICK = 2
	BOMB_UP = 3
	POWER_UP = 4
	LIFE_UP = 5
	TIME_UP = 6
	FPS = 30
	WIDTH = 840
	HEIGHT = 690
	TILE_SIZE = 40
	IMAGE_PATH = "resources/images/"
	AUDIO_PATH = "resources/sounds/"
	HIGHSCORES_PATH = "resources/highscores.txt"
	SINGLE = 'Single'
	MULTI = 'Multi'
	MAX_ENEMY_SPRITES = 9
	LOCALHOST = True
