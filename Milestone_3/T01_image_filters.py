""" ==========================================================================
                           ECOR 1042 Fall 2020
Team: T01

Name 1: Michael Whitford (Team Lead)
Student Number: 101151720

Name 2: Rakan Al-Wadi 
Student Number: 101161281

Name 3: Ndifor Akemche 
Student Number: 101091541 

Name 4: Mohammed Alsafi
Student Number: 101162698

Milestone 3, Image Filters Module (Slightly Modified from Milestone 2)

Last edited: Dec. 11, 2020
==========================================================================="""

from Cimpl import choose_file, load_image, copy, create_color, set_color,\
                  show, Image, get_color, save_as, create_image, get_width, \
                  get_height

#==============================P3 Filters====================================#
def red_channel(original_image: Image) -> Image:
    """Written by: Mohammed Alsafi
    
    Returns a copy of an image displaying just the red RGB components of 
    the original image 
    
    >>> red_image = red_channel( load_image('p2-original.png') )
    >>> show(red_image)
    """
    new_imageR = copy(original_image)
    
    for pixel1 in original_image:
	    x, y, (r, g, b) = pixel1
	    new_colourR = create_color(r, 0, 0 )  # Red
	    set_color (new_imageR, x, y, new_colourR)
    return new_imageR

def green_channel(image: Image) -> Image:
    """Written by: Rakan Al-Wadi
    
    Returns a copy of an image displaying just the green RGB components of 
    the original image
    
    >>> green_image = green_channel( load_image('p2-original.png') )
    >>> show(green_image)
    """
    copy_image = copy(image)
    
    for x,y, (r,g,b) in copy_image:
        color = create_color(0,g,0) #green
        set_color(copy_image,x,y,color)
    return copy_image

def blue_channel(image:Image) -> Image:
    """Written by: Ndifor Akemche 
    
    Returns a copy of an image displaying just the blue RGB components of 
    the original image
    
    >>> blue_image = blue_channel( load_image('p2-original.png') )
    >>> show(blue_image)
    """
    new_image = copy(image)

    # Select the pixels and display only the blue component. 
    for x,y, (r,g,b) in image:
        blue = create_color(0, 0, b)
        set_color(new_image, x,y, blue)

    return new_image

def combine(red_image: Image, green_image: Image, blue_image: Image) -> Image:
    """Written by: Michael Whitford
    
       Returns a copy of an image that takes the red, green, and blue 
       filter images and merges them back together to the original image.
   
    >>> combined_image = combine( load_image('red_image.png'), 
                                  load_image('green_image.png'),
                                  load_image('blue_image.png') )
    >>> show(combined_image)
    """
    new_image = copy(red_image)
    
    #Can iterate this way as each image will be the same size
    for x, y, (r, g, b) in new_image:

        #Get the new RGB components for each pixel by taking the red component, 
        #green component, and blue component of each of the 3 filters 
        #passed in respectively. This will "merge" the colours back to their 
        #original state.
        
        #Gets green component of RGB Tuple at pixel x,y returned from get_color
        #function for green_image
        green = get_color(green_image, x, y)[1]
        
        #Gets blue component of RGB Tuple at pixel x,y returned from get_color
        #function for blue_image     
        blue = get_color(blue_image, x, y)[2]
        
        #Create new RGB tuple. No need to "get" the red component as new_image 
        #is a copy of red_image, therefore the red component is already correct
        combined_color = create_color(r, 
                                      green, 
                                      blue)
        set_color(new_image, x, y, combined_color)      
    return new_image

#==============================P4 Filters====================================#
def two_tone(image: Image, colour_1: str, colour_2: str) -> Image:
    """Written by: Michael Whitford
    
       Returns a copy of an image that has a two tone filter applied to it.
   
    >>> two_tone_image =  two_tone(load_image('p2-original.png'),
                                    "black", "white")
    >>> show(two_tone_image)
    """

    colours = [ ("black", (0,0,0)),
                ("white", (255,255,255)),
                ("red", (255,0,0)),
                ("lime", (0,255,0)),
                ("blue", (0,0,255)),
                ("yellow", (255,255,0)),
                ("cyan", (0,255,255)),
                ("magenta", (255,0,255)),
                ("gray", (128,128,128))]
    
    new_image = copy(image)
    
    #Can iterate this way as each image will be the same size
    for x, y, (r, g, b) in new_image:
        brightness = (r + g + b) // 3
        
        #Initialize to 1st colour
        colour_str = colour_1.lower()
        
        #Swap to 2nd colour if required
        if (brightness >= 128):
            colour_str = colour_2.lower()
        
        #Need to initilize to avoid scope issue, initialize to value that 
        #should never occur
        new_color = create_color(1,1,1) 
                       
        for elem in range(len(colours)):
            colour, rgb_tuple = colours[elem]
            r,b,g = rgb_tuple
            if (colour == colour_str):
                new_color = create_color(r,g,b) 

        set_color(new_image, x, y, new_color)      
    return new_image

def three_tone(image: Image, colour_1: str, 
               colour_2: str, colour_3: str) -> Image:
    """Written by: Michael Whitford
    
       Returns a copy of an image that has a three tone filter applied to it.
   
    >>> three_tone_image =  three_tone(load_image('p2-original.png'),
                                    "black", "white", "gray")
    >>> show(three_tone_image)
    """

    colours = [ ("black", (0,0,0)),
                ("white", (255,255,255)),
                ("red", (255,0,0)),
                ("lime", (0,255,0)),
                ("blue", (0,0,255)),
                ("yellow", (255,255,0)),
                ("cyan", (0,255,255)),
                ("magenta", (255,0,255)),
                ("gray", (128,128,128))]
    
    new_image = copy(image)
    
    #Can iterate this way as each image will be the same size
    for x, y, (r, g, b) in new_image:
        brightness = (r + g + b) // 3
        
        #Initialize to 1st colour
        colour_str = colour_1.lower() 
        
        #Swap to 2nd or 3rd colour if required
        if ( (brightness >= 85) and
             (brightness <= 170) ):
            colour_str = colour_2.lower()
        elif (brightness >= 171):
            colour_str = colour_3.lower()
        
        #Need to initilize to avoid scope issue, initialize to value that 
        #should never occur
        new_color = create_color(1,1,1) 
                       
        for elem in range(len(colours)):
            colour, rgb_tuple = colours[elem]
            r,b,g = rgb_tuple
            if (colour == colour_str):
                new_color = create_color(r,g,b) 

        set_color(new_image, x, y, new_color)      
    return new_image

def extreme_contrast(image: Image) -> Image:
    """Written by: Ndifor Akemche
    
    Returns a copy of an image that has an extreme contrast filter applied 
    to it
    
    >>> filtered_image = extreme_contrast(load_image('p2-original.png'))
    >>> show(filtered_image)
    """

    new_image = copy(image)

    for x, y, (r, g, b) in new_image:
        # set new value of r depending on its previous values
        if (r <= 127):
            r = 0
        else: 
            r = 255

        # set new value of g depending on its previous values
        if (g <= 127):
            g = 0
        else: 
            g = 255

        # set new value of b depending on its previous values
        if (b <= 127):
            b = 0
        else:
            b = 255
        
        new_color = create_color(r,g,b)
        set_color(new_image, x, y, new_color)
        
    return new_image

def sepia(image: Image) -> Image:
    """Written by: Mohammed Alsafi
    
    Returns a copy of an image that has a sepia filter applied 
    to it
        
    >>> image = sepia(load_image('p2-original.png'))
    >>> show(image)
    """
    new_image = copy(image)
    new_image = grayscale(new_image)
    
    for x, y, (r, g, b) in new_image:
        
        if (r + g + b) // 3 < 63: 
            decrease = 0.9
            increase = 1.1
       
        elif (r + g + b) // 3 <= 191:
            decrease = 0.85
            increase = 1.15
        
        else:
            decrease = 0.93
            increase = 1.08
        
        new_color = create_color(r * increase, g, b * decrease)
        set_color (new_image, x, y, new_color)
        
    return new_image

def grayscale(image: Image) -> Image:
    """Written by: ECOR 1042. Taken from simple_Cimple_filters.py
    
    Returns a grayscale copy of image. 
   
    >>> image = load_image(choose_file())
    >>> gray_image = grayscale(image)
    >>> show(gray_image)
    """
    new_image = copy(image)
    for x, y, (r, g, b) in image:

        # Use the pixel's brightness as the value of RGB components for the 
        # shade of gray. These means that the pixel's original colour and the
        # corresponding gray shade will have approximately the same brightness.
        
        brightness = (r + g + b) // 3
        
        # or, brightness = (r + g + b) / 3
        # create_color will convert an argument of type float to an int
        
        gray = create_color(brightness, brightness, brightness)
        set_color(new_image, x, y, gray)      
    return new_image


def _adjust_component(color: int) -> int:
    """Written by: Rakan Al-Wadi
    
    Returns the midpoint of a quadrant for an RGB value. Used as a helper
    function for posterize.
        
    >>> test1 = _adjust_component(63)
    >>> test1
        31
    
    >>> test2 = _adjust_component(75)
    >>> test2
        95
    
    >>> test3 = _adjust_component(150)
    >>> test3
        159
    
    >>> test4 = _adjust_component(255)
    >>> test4
        223
    """
    
    if color < 64:
        return 31
    elif color < 128:
        return 95
    elif color < 192:
        return 159
    
    return 223

def posterize(image: Image) -> Image:
    """Written by: Rakan Al-Wadi
    
    Returns a copy of an image that has a posterized filter applied 
    to it
    
    >>> filtered_image = posterize(load_image('p2-original.png'))
    >>> show(filtered_image)
    """

    copy_of_image = copy(image)
    for x, y, (r, g, b) in copy_of_image:
        set_color(copy_of_image, x, y, create_color(_adjust_component(r), 
                  _adjust_component(g), _adjust_component(b)))
    
    return copy_of_image

#==============================P5 Filters====================================#

def detect_edges(image: Image, threshold: int) -> Image:
    """Written by: Michael Whitford
    
       Returns a copy of an image that has a basic edge detection
       filter applied to it.
   
    >>> detect_edges_image =  detect_edges(load_image('p2-original.png'),
                                           25)
    >>> show(detect_edges_image)
    """
    
    WHITE = create_color(255,255,255)
    BLACK = create_color(0,0,0)
    
    new_image = copy(image)
    
    IMAGE_HEIGHT = get_height(new_image)
    
    #Used for the difference between the actual height and x,y index
    DIFF_INDEX = 1
    
    #Can iterate this way as each image will be the same size
    for x, y, (r, g, b) in new_image:
        
        #Base Case: Bottom edge
        if (y == (IMAGE_HEIGHT - DIFF_INDEX)): 
            set_color(new_image, x, y, WHITE)
        
        #General Case
        else:
            brightness_1 = (r + g + b) // 3
            
            colour_2 = get_color(new_image, x, y+1)
            r_2, g_2, b_2 = colour_2
            brightness_2 = (r_2 + g_2 + b_2) // 3
            
            contrast = abs(brightness_1 - brightness_2)
            
            if (contrast > threshold):
                set_color(new_image, x, y, BLACK)
            else:
                set_color(new_image, x, y, WHITE)
                 
    return new_image

def detect_edges_better(image: Image, threshold: int) -> Image:
    """Written by: Ndifor Akemche. Modified by Michael Whitford.
    
       Returns a copy of an image that has an improved edge detection
       filter applied to it.
   
    >>> detect_edges_image = detect_edges_better(load_image('p2-original.png'),
                                                  25)
    >>> show(detect_edges_image)
    """
    
    WHITE = create_color(255,255,255)
    BLACK = create_color(0,0,0)
    
    new_image = copy(image)
    
    IMAGE_HEIGHT = get_height(new_image)
    IMAGE_WIDTH =  get_width(new_image)
    
    #Used for the difference between the actual height and x,y index
    DIFF_INDEX = 1    
    
    #Can iterate this way as each image will be the same size
    for x, y, (r, g, b) in new_image:
        
        #Base Case: Bottom edge
        if ( (y == (IMAGE_HEIGHT - DIFF_INDEX)) or 
             (x == (IMAGE_WIDTH -  DIFF_INDEX)) ): 
            set_color(new_image, x, y, WHITE)
        
        #General Case
        else:
            brightness_1 = (r + g + b) // 3
            
            #Get Pixel beneath original pixel and its brightness
            colour_2 = get_color(new_image, x, y+1)
            r_2, g_2, b_2 = colour_2
            brightness_2 = (r_2 + g_2 + b_2) // 3
            
            #Calculate 1st contrast
            contrast_1 = abs(brightness_1 - brightness_2)
            
            #Get Pixel to right of original pixel and its brightness
            colour_3 = get_color(new_image, x+1, y)
            r_3, g_3, b_3 = colour_3
            brightness_3 = (r_3 + g_3 + b_3) // 3 
            
            #Calculate 2nd contrast
            contrast_2 = abs(brightness_1 - brightness_3)
            
            if ( (contrast_1 > threshold) or 
                 (contrast_2 > threshold) ):
                set_color(new_image, x, y, BLACK)
            else:
                set_color(new_image, x, y, WHITE)
                 
    return new_image

def flip_vertical(image: Image) -> Image:
    """Written by: Mohammed Alsafi. 
    
    Returns a copy of an image that has been flipped through a 
    horizontal line
    
    >>> new_image = flip_vertical(load_image('p2-original.png'))
    >>> show(new_image)
    """
    new_image = copy(image)
    
    IMAGE_WIDTH = get_width(image)
    IMAGE_HEIGHT = get_height(image)
    
    #Used for the difference between the actual height and x,y index 
    DIFF_INDEX = 1
    
    for x in range(IMAGE_WIDTH):
        for y in range(IMAGE_HEIGHT):
            color = get_color(image, x, y) 
            set_color(new_image, x, IMAGE_HEIGHT-DIFF_INDEX-y, color) 
                
    return new_image 

def flip_horizontal(image: Image) -> Image:
    """Written by: Rakan Al-Wadi. Modified by Michael Whitford.
    
    Returns a copy of an image that has been flipped through a 
    vertical line
    
    >>> new_image = flip_horizontal(load_image('p2-original.png'))
    >>> show(new_image)
    """    
    
    new_image = copy(image)
    
    IMAGE_WIDTH = get_width(image)
    IMAGE_HEIGHT = get_height(image)
    
    #Used for the difference between the actual height and x,y index 
    DIFF_INDEX = 1
    
    for x in range(IMAGE_WIDTH):
        for y in range(IMAGE_HEIGHT):
            color = get_color(image, x, y) 
            set_color(new_image, IMAGE_WIDTH - DIFF_INDEX - x, y, color) 
                
    return new_image
