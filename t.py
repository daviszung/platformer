# screen [0, 1, 2, 3, 4, etc.]

# will resolve to screen 2
scroll = 3300

screen = round(scroll / 1600)
print(round(3200 / 1600))

# location where you blit the frame
print(screen * 1600)