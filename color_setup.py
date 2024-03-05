'''
color_setup.py - color setup for DisplayBuffer with MPDisplay
Usage:
    from color_setup import ssd
    <your code here>
'''
from displaybuf import DisplayBuffer as SSD
from board_config import display_drv

# format = SSD.GS4_HMSB  # 4-bit (16 item) lookup table of 16-bit RGB565 colors; w*h/2 buffer
# format = SSD.GS8  # 256 8-bit RGB332 colors; w*h buffer
format = SSD.RGB565  # all 65,536 16-bit RGB565 colors; w*h*2 buffer

ssd = SSD(display_drv, format)
