import pygame
from random import randint

pygame.init()

GREEN = (0, 200, 0)
BLUE = (0, 0, 255)
BLACK = (36, 32, 33)
WHITE = (255,255,255)

clock = pygame.time.Clock()


WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

TUBE_WIDTH = 50
TUBE_VELOCITY = 3
TUBE_GAP = 200

tube1_x = 400
tube2_x = 600
tube3_x = 800

tube1_height = randint(100, 400)
tube2_height = randint(100, 400)
tube3_height = randint(100, 400)

tube1_pass = False
tube2_pass = False
tube3_pass = False

BIRD_X = 50
BIRD_WIDTH = 30
BIRD_HEIGHT = 30
GRAVITY = 0.5

bird_y = 300
bird_drop_velocity = 0

score = 0
font = pygame.font.SysFont("sans", 20)

running = True
paussing = False

background = pygame.image.load('background.png')
bird_image = pygame.image.load("redbird.png")
bird_image = pygame.transform.scale(bird_image, (BIRD_WIDTH, BIRD_HEIGHT))
tube_image = pygame.image.load("tube_inv.png")
tube_image_inv = pygame.image.load("tube.png")


while running:
	clock.tick(60)
	screen.fill(GREEN)
	screen.blit(background, (0,0))

	# Draw tube
	#tube1 = pygame.draw.rect(screen, BLUE, (tube1_x, 0, TUBE_WIDTH, tube1_height))
	# tube2 = pygame.draw.rect(screen, BLUE, (tube2_x, 0, TUBE_WIDTH, tube2_height))
	# tube3 = pygame.draw.rect(screen, BLUE, (tube3_x, 0, TUBE_WIDTH, tube3_height))

	tube1 = screen.blit(pygame.transform.scale(tube_image, (TUBE_WIDTH, tube1_height)), (tube1_x,0)) 
	tube2 = screen.blit(pygame.transform.scale(tube_image, (TUBE_WIDTH, tube2_height)), (tube2_x,0)) 
	tube3 = screen.blit(pygame.transform.scale(tube_image, (TUBE_WIDTH, tube3_height)), (tube3_x,0)) 

	# Draw tube inverse
	# tube1_inv = pygame.draw.rect(screen, BLUE, (tube1_x, tube1_height + TUBE_GAP, TUBE_WIDTH, HEIGHT - tube1_height - TUBE_GAP))
	# tube2_inv = pygame.draw.rect(screen, BLUE, (tube2_x, tube2_height + TUBE_GAP, TUBE_WIDTH, HEIGHT - tube2_height - TUBE_GAP))
	# tube3_inv = pygame.draw.rect(screen, BLUE, (tube3_x, tube3_height + TUBE_GAP, TUBE_WIDTH, HEIGHT - tube3_height - TUBE_GAP))

	tube1_inv = screen.blit(pygame.transform.scale(tube_image_inv, (TUBE_WIDTH, HEIGHT - tube1_height - TUBE_GAP)), (tube1_x,tube1_height+TUBE_GAP))  
	tube2_inv = screen.blit(pygame.transform.scale(tube_image_inv, (TUBE_WIDTH, HEIGHT - tube1_height - TUBE_GAP)), (tube2_x,tube2_height+TUBE_GAP)) 
	tube3_inv = screen.blit(pygame.transform.scale(tube_image_inv, (TUBE_WIDTH, HEIGHT - tube1_height - TUBE_GAP)), (tube3_x,tube3_height+TUBE_GAP)) 
	
	# Draw move tube
	tube1_x = tube1_x - TUBE_VELOCITY
	tube2_x = tube2_x - TUBE_VELOCITY
	tube3_x = tube3_x - TUBE_VELOCITY

	# Draw new tube
	if tube1_x < -TUBE_WIDTH:
		tube1_x = 550
		tube1_height = randint(100, 300)
		tube1_pass = False
	if tube2_x < -TUBE_WIDTH:
		tube2_x = 550
		tube2_heihgt = randint(100, 300)
		tube2_pass = False
	if tube3_x < -TUBE_WIDTH:
		tube3_x = 550
		tube3_height = randint(100, 300	)
		tube3_pass = False


	# Bird falls
	bird_y += bird_drop_velocity
	bird_drop_velocity += GRAVITY

	# Draw bird
	bird_rect = screen.blit(bird_image, (BIRD_X, bird_y ))


	# Update score
	if tube1_x < BIRD_X and tube1_pass == False:
		score += 1
		tube1_pass = True
	if tube2_x < BIRD_X and tube2_pass == False:
		score += 1
		tube2_pass = True
	if tube3_x < BIRD_X and tube3_pass == False:
		score += 1
		tube3_pass = True

	# Draw text score
	score_txt = font.render("Score : " + str(score), True, WHITE)
	screen.blit(score_txt, (5, 5))

	# check collision
	for check in [tube1, tube2, tube3, tube1_inv, tube2_inv, tube3_inv]:
		if bird_rect.colliderect(check):
			TUBE_VELOCITY = 0 
			bird_drop_velocity = 0
			paussing = True
			print_score_txt = font.render("Score : " + str(score), True, WHITE)
			screen.blit(print_score_txt, (150, 100))
			continute_txt = font.render("Press space to continute ", True, WHITE)
			screen.blit(continute_txt, (150, 150))

  

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		# press space
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				if paussing:
					tube1_x = 400
					tube2_x = 600
					tube3_x = 800
					TUBE_VELOCITY = 3
					score = 0
					bird_y = 400
					paussing = False

				bird_drop_velocity = -10



	pygame.display.flip()

pygame.quit()
