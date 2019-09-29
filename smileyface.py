import arcade
# Set constants for the screen size.
screen_width = 600
screen_height = 600

# Open the window. Set th window title and dimensions (width and height)
arcade.open_window(screen_width, screen_height, "Smiley Face")

# Set the background color to white
# You can find more named colors at http://arcade.academy/arcade.color.html

arcade.set_background_color(arcade.color.BABY_BLUE)

# Starting the render process
arcade.start_render()

# Drawing the face by setting constants

x = 300
y = 300
radius = 200

arcade.draw_circle_filled(x, y, radius, arcade.color.WHITE)

# Draw the right eye
x = 370
y = 350
radius = 20
arcade.draw_circle_filled(x, y, radius, arcade.color.BLACK)

# Draw the left eye

x = 230
y = 350
radius = 20
arcade.draw_circle_filled(x, y, radius, arcade.color.BLACK)

# Draw the smile
x = 300
y = 280
width = 120
height = 100
start_angle = 190
end_angle = 350
arcade.draw_arc_outline(x, y, width, height, arcade.color.BLACK, start_angle, end_angle, 10)

# Finish the drawing and display the result
arcade.finish_render()

# Keep the window open until the user hits the 'close' button
arcade.run()