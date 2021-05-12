from pynput.mouse import Button as m_Button
from pynput.mouse import Controller as m_Controller

from pynput.keyboard import Key as k_Key
from pynput.keyboard import Controller as k_Controller

'''
Mouse part
'''
mouse = m_Controller()

# Read pointer position
print('The current pointer position is {0}'.format(mouse.position))

# Set pointer position
mouse.position = (1094, 401)
print('Now we have moved it to {0}'.format(mouse.position))

# # Press and release
mouse.press(m_Button.left)
mouse.release(m_Button.left)

# # Double click; this is different from pressing and releasing
# # twice on macOS
# mouse.click(m_Button.left, 2)

'''
Keyboard part
'''
keyboard = k_Controller()

keyboard.type('hello world\b\b')

