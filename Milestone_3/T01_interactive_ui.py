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

Milestone 3, Interactive UI

Last edited: Dec. 11, 2020
==========================================================================="""

from T01_image_filters import * #Cimpl will be imported as well with this

def print_menu() -> None:
    """
    Written by: Ndifor Akemche
    
    A function that prints the user menu
    
    >>> print_menu()
    """
    print("L)oad image     S)ave-as")
    print("2)-tone 3)-tone X)treme contrast T)int sepia P)osterize")
    print("E)dge detect I)mproved edge detect V)ertical flip H)orizontal flip")
    print("Q)uit")
    print("")

def get_input(image_loaded: bool, commands:dict) -> bool:
    """
    Written by: Rakan Al-Wadi. Modified by Michael Whitford
    
    A function that gets returns the command the user would like to have 
    executed
    """
    
    valid_input = False
    
    #Loop until user has given a valid input
    while not valid_input:
        print_menu()
        #Get input
        command = input(": ").upper().strip()
    
        #Check dict keys to make sure command is valid
        if (command not in commands.keys()):
            print("\nNo such command.\n")
        #Make sure image is loaded, and user doesn't want to quit
        elif (command != "L" and not image_loaded and command != "Q"):
            print("\nNo image loaded.\n")        
        else:
            valid_input = True #can exit loop as input was valid
            
    return command

def apply_command(user_input: str, commands:dict, image:Image) -> Image:
    """
    Written by: Michael Whitford
    
    A function that applies a valid user command
    
    >>> image = load_image('p2-original.png')
    >>> image = apply_command("2", {"2": two_tone}, image)
    >>> image = apply_command("H", {"H": flip_horizontal}, image)
    """
    
    #To load image
    if (user_input == "L"):
        image = load_image(choose_file())
    #To save image
    elif (user_input == "S"):
        save_as(image)
    #If input is an edge detection filter, user must input threshold
    elif (user_input == "E" or user_input == "I"):
        threshold = int(input("\nPlease input a threshold: "))
        
        #Assume a number is input, but this checks bounds for threshold
        if (threshold < 0):
            threshold = 0
    
        elif (threshold > 255):
            threshold = 255
    
        #Get filter name from dict, and apply filter
        filter_name = commands[user_input]
        image = filter_name(image,threshold)
    
    #Applies 2-tone filter
    elif (user_input == "2"):
        image = two_tone(image, "lime", "magenta")
    
    #Applies 3-tone filter
    elif (user_input == "3"):
        image = three_tone(image, "blue", "yellow", "gray")    
    
    else:
        #No special handling. Get filter name from dict, and apply filter
        filter_name = commands[user_input] 
        image = filter_name(image)
    
    show(image)
    return image
    
#Main Script, written by Michael Whitford

#Dictionary of valid commands, and corresponding filters (if applicable)
commands = {"L": None, "S": None, "Q": None,
            #P4 Filters
            "2": two_tone,
            "3": three_tone, 
            "X": extreme_contrast,
            "T": sepia,
            "P": posterize,
            #P5 Filters
            "E": detect_edges,
            "I": detect_edges_better,
            "H": flip_horizontal,
            "V": flip_vertical}

user_input = ""
image_loaded = False
image = ""

print("\nWelcome to the T01 Photo Editor!\n")

#Continue until user input 
while (user_input != "Q"): 
    user_input = get_input(image_loaded, commands)
    
    #get_input function forces an image to be loaded unless input is 
    #to Quit
    image_loaded = True
    
    #Only apply command if user doesn't want to quit
    if (user_input != "Q"):
        image = apply_command(user_input, commands, image)
 


    