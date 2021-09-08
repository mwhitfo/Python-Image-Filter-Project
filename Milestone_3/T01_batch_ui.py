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

Milestone 3, Batch UI

Last edited: Dec. 11, 2020
==========================================================================="""

from T01_image_filters import * #Cimpl will be imported as well with this

def apply_command(user_input: str, commands:dict, image:Image) -> Image:
    """
    Written by: Mohammed Alsafi. Modified by Michael Whitford
    
    A function that applies a command read from the batch file
    
    >>> image = load_image('p2-original.png')
    >>> image = apply_command("2", {"2": two_tone}, image)
    >>> show(image)
    >>> image = apply_command("H", {"H": flip_horizontal}, image)
    >>> show(image)
    """
    
    #Applies Edge Detection filter
    if (user_input == "E"):
        image = detect_edges(image, 15)
    
    #Applies Improved Edge Detection Filter
    elif (user_input == "I"):
        image = detect_edges_better(image, 15)
    
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
        
    return image

def read_file(filename: str, commands: dict) -> None:
    """
    Written by: Michael Whitford
    
    A function that reads in the batch file.
    """
    #Open File
    infile = open(filename, "r")

    for line in infile:
        #Create list of words that have been read in
        command_list = line.split()
        
        #Load original image
        image = load_image(command_list[0].strip())
        
        #Capture the new file name for after commands are run
        new_filename = command_list[1].strip()
    
        #Apply filters
        for i in range(2,len(command_list)):
            filt = command_list[i]
            image = apply_command(filt, commands, image)

        #Line is finished, save image as file with new file name
        save_as(image, new_filename)
        
    #Close file
    infile.close()
    
#Main Script, written by Michael Whitford

#Dictionary of valid commands and filters
commands = {
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

image = ""

print("\nWelcome to the T01 Photo Editor!\n")
filename = input("Please input the name of the batch file: ")

read_file(filename, commands)

print("\nProgram Complete!")