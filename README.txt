===================================================
Software Name: T01 Photo Editor
Version 1.0,	Date: Sep. 8th, 2021

===================================================
Contact Information
===================================================

Lead Developer: Michael Whitford
Email: 	  mike.whitford23@gmail.com
Phone Number:   613-883-6523

===================================================
DESCRIPTION
===================================================
- This application applies up to 9 filters one at a time
to an image chosen by the user. The image is displayed
after each filter is applied 

- The user can save the image when satisfied with the 
combination of filters

-There is also the option of writing the commands
into a batch file, and loading the commands (Batch UI)

The available filters include:
-Two Tone
-Three Tone
-Extreme Contrast
-Sepia Tint
-Posterize
-Edge Detect
-Improved Edge Detect
-Vertical Flip
-Horizontal Flip  

===================================================
Installation 
===================================================
Files to Download as Part of Application:

T01_interactive_ui.py 
T01_image_filters.py
T01_batch_ui.py

Additional Software Requirements:

Python 3 (Python 3.7 -64-bit- recommended)
Cimpl.py (Required library)
Pillow (Latest Version)

===================================================
Usage
===================================================

----------------INTERACTIVE UI---------------------

-When the program is first run, the main menu will 
appear:

---------------------------------------------
>>>[evaluate T01_interactive_ui.py]
Cimpl 1.04; October 6, 2017

Welcome to the T01 Photo Editor!

L)oad image     S)ave-as
2)-tone 3)-tone X)treme contrast T)int sepia P)osterize
E)dge detect I)mproved edge detect V)ertical flip H)orizontal flip
Q)uit

: 
---------------------------------------------

- The user will then input commands one by one in order to load an image,
apply the desired filters, and save the image. The user can then 
decide to load a new image and repeat the process, or quit.

Notes: 
-The program is not case sensitive. 
-"L" must be the first command run in order to load an image.
-Once an image has been loaded, the commands can be run in any order.
-The filters are cumulative  

Command Definitions:

- "L": Opens an external window for the user to select an image
- "S": Opens an external window for the user to save the altered image
- "Q": Terminates program

- "2": Returns and displays a two tone filter applied with lime and magenta 
- "3": Returns and displays a three tone filter applied with blue, yellow, and gray 
- "X": Returns and displays an image with an extreme contrast filter applied.
- "T": Returns and displays an image with a sepia filter applied.
- "P": Returns and displays an image with a posterize filter applied.
- "E": Returns and displays an image with an Edge Detect filter applied.
       Will also prompt the user to enter a threshold value, which must be an integer 
       in between 0 and 255 inclusive
- "I": Returns and displays an image with an Improved Edge Detect filter applied.
       Will also prompt the user to enter a threshold value, which must be an integer 
       in between 0 and 255 inclusive
 
- "V": Returns and displays an image with a vertical flip filter applied.
- "H": Returns and displays an image with a horizontal flip filter applied.

Example Usage:

>>>[evaluate T01_interactive_ui.py]
Cimpl 1.04; October 6, 2017

Welcome to the T01 Photo Editor!

L)oad image     S)ave-as
2)-tone 3)-tone X)treme contrast T)int sepia P)osterize
E)dge detect I)mproved edge detect V)ertical flip H)orizontal flip
Q)uit

: l

L)oad image     S)ave-as
2)-tone 3)-tone X)treme contrast T)int sepia P)osterize
E)dge detect I)mproved edge detect V)ertical flip H)orizontal flip
Q)uit

: 2

L)oad image     S)ave-as
2)-tone 3)-tone X)treme contrast T)int sepia P)osterize
E)dge detect I)mproved edge detect V)ertical flip H)orizontal flip
Q)uit

: h

L)oad image     S)ave-as
2)-tone 3)-tone X)treme contrast T)int sepia P)osterize
E)dge detect I)mproved edge detect V)ertical flip H)orizontal flip
Q)uit

: s

L)oad image     S)ave-as
2)-tone 3)-tone X)treme contrast T)int sepia P)osterize
E)dge detect I)mproved edge detect V)ertical flip H)orizontal flip
Q)uit

: q

----------------BATCH UI---------------------

-When the program is first run, the main menu will 
appear:

---------------------------------------------
>>>[evaluate T01_batch_ui.py]
Cimpl 1.04; October 6, 2017

Welcome to the T01 Photo Editor!

Please input the name of the batch file:
---------------------------------------------

-The user must then input the name of a pre-written
batch file in the same folder as the application

-Each line of the batch file must be as follows:

<image_to_be_loaded> <final_image_name> <filter commands>

-The program will then load the <image_to_be_loaded>,
apply the filter commands to the image, and save it
with the <final_image_name>.

Example Usage:

---------------------------------------------
>>>[evaluate T01_batch_ui.py]
Cimpl 1.04; October 6, 2017

Welcome to the T01 Photo Editor!

Please input the name of the batch file: sample_batch.txt

Program Complete!
---------------------------------------------

-Contents of sample_batch.txt:

p2-original.png test1.png 2 X P 
p2-original.png test2.png  V H E I
p2-original.png test3.png 3 T P

-This will load p2-original.png, and apply the respective
filters on each line to test1.png, test2.png, 
and test3.png

===================================================
CREDITS
===================================================

Interactive User Interface Developers:

- Michael Whitford -> Main Script, apply_command 
- Ndifor Akemche -> Print Menu 
- Rakan Al-Wadi -> Get Input 

Batch User Interface Developers:

- Michael Whitford -> Main Script, read_file 
- Mohammed Alsafi -> apply_command 

Filter Developers:

- Michael Whitford -> Edge Detection, 2_tone, 3_tone 
- Ndifor Akemche -> Extreme Contrast, Improved Edge Detection 
- Mohammed Alsafi -> Vertical Flip, Sepia Tinting 
- Rakan Al-Wadi -> Posterizing, _adjust_component, Horizontal Flip, 

==============================================================================
License:

Copyright (c) [2021] [Michael Whitford]

Permission is hereby granted, to any person obtaining a copy
of this software and associated documentation files 
(T01_interactive_ui.py, T01_image_filters.py, T01_batch_ui.py), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
==============================================================================
