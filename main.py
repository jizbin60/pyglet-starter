import pyglet # import the library
win = pyglet.window.Window() # create the window

#Create some text
text = pyglet.text.Label('Hello, world', x = 200, y = 200)
uno = pyglet.text.Label('Hola, world', font_size = 31, x = 300, y = 300)
dos = pyglet.text.Label('Bonjour, world', font_size = 48, x = 400, y = 400)


# Create a sprite
img = pyglet.image.load('assets/hero/Old hero.png')
door = pyglet.image.load('assets/hero/Old hero.png')
cat = pyglet.image.load('assets/hero/Old hero.png')
dog = pyglet.image.load('assets/hero/Old hero.png')
goat = pyglet.image.load('assets/hero/Old hero.png')


rat = pyglet.image.load('sheet.png')
rat = pyglet.sprite.Sprite(rat, x = -20, y = 380)
# spr = pyglet.sprite.Sprite(img, x=50, y=50)

keys = pyglet.window.key.KeyStateHandler()
# Start the event loop
def update(dt):
  rat.x += 1
if keys[key.SPACE]:
  print("Spacebar pressed!")
if keys[key.UP]:
  print("Up key pressed!")


@win.event
def on_draw():
    win.clear()
    text.draw()
    uno.draw()
    dos.draw()
    img.blit(0, 0)
    door.blit(555, 222)
    cat.blit(444, 123)
    dog.blit(110,100)
    goat.blit(198, 300)
    
    rat.draw()
    #img.blit(400, 100)
    # spr.draw()

pyglet.clock.schedule(update) 
pyglet.app.run()
