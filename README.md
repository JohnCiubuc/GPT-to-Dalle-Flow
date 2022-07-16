# GPT-to-Dalle-Flow
For circle. Generate a GPT prompt, toss it to Dalle, get an image, make it wallpaper-able, and 'apply'.

This doesn't apply the wallpaper, but you could likely do so by adding this at the end:


```py
import ctypes
ctypes.windll.user32.SystemParametersInfoW(20, 0, "absolute path" , 0)
```

# Examples

DALLE Prompt: This digital art depicts a light immortal in a xianxia setting. The light immortal is surrounded by a glowing aura, and is floating in the air.

DALLE Prompt: She had always been fascinated by the stories of the great immortals. They were said to be powerful and beautiful, and they lived in a world that was full of color and light. She wanted to be one of them. One day, she found a doorway to their world. It was guarded by a great dragon, but she was not afraid. She boldly stepped through the door and found herself in a beautiful garden.

DALLE Prompt: A rushing waterfall pours over a cliff into a frothing pool far below. The setting sun casts a pink and orange glow on thescene, making the water look like it is on fire.

DALLE Prompt: The eternally young and beautiful creature known as the " Rainbow Immortal " lives in a world of fantasy and magic. She is said to bring good luck and happiness to all who cross her path. Her bright and colorful appearance is a symbol of hope and joy, and her presence is said to bring light and happiness into the lives of those she meets.

DALLE Prompt: This dark hero is clad in steampunk armor, complete with brass goggles and a breathing mask. He carries a largesword at his side, and his trusty robotic companion by his feet. In the background is a steampunk city, filled with airships and dirigibles.
