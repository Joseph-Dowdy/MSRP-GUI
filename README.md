# MSRP-GUI
Car Price Navigator using data from a CSV that contains over 400 cars from 2021. The application utilizes the python csv and tkinter libraries. Formal project write up:

Joseph Dowdy
Final Project – Car Price Navigator
I. Background
Manufacturer’s suggested retail price, MSRP, is often used as a starting point to determine what consumers will pay for a car; However, just because a car has an MSRP does not mean that it will always sell for that price. Demand in the car market is generally elastic meaning that price and quantity demanded have a strong negative correlation; This implies that, in general, as prices go down the corresponding demand goes up. Ultimately, this is only one of many factors that is taken into consideration when retailers list cars for sale. Other factors include public hype behind certain makes and models, changing consumer preferences, availability of cars, performance, and other various consumer spending trends; As a result, car prices can fluctuate significantly in a short period of time. Amid a chaotic market, it can be hard to tell if a car is listed for a fair price. Although comparing car price solely to MSRP is only a partial solution to a very dynamic and challenging market, it can serve as a strong fundamental tool during the initial search. The aim of application is to give the user a tool that compares a car’s sale prices to its “baseline” price, or MSRP, and allows the user to keep record of their search in a CSV file. This application can be beneficial in helping businesses and individuals evaluate car pricing before making their next purchase.
II. The Application
As previously aforementioned this program allows a user to compare the listed price of a car compared to its MSRP. The application attempts to help answer the question “Is this a good price?” while shopping for a car. From a technical side, including comments and spacing, the application consists of 261 lines of code. It features the use of eight distinct functions which serve to both run analysis as well as increase user friendliness. The dataset that the application is based on is a CSV file. The reading and handling of files in the script is entirely done by the csv library. From the user’s side, the application’s face is a GUI created from the tkinter library. The GUI consists of five labels, two entry boxes, two combo boxes, and two buttons. For increased user friendliness, one of the combo boxes serves as a dropdown option menu that has multiple options for additional functionality. The application is programmed to have several instances where a message box is created to give the user additional feedback.
III. The Output
The primary output is to a csv file titled “main_record.csv”. This output is a csv file that features 6 columns: Seller, Car Make and Model, Year, MSRP, User Found Price, and Good Deal.
The Seller column serves as a reference for the user to look back at and see where any given entered car was listed at. The Car Make and Model column serves as reference to what car that row corresponds to. The Year column represents the year the car was made. For this application all the cars that can be analyzed are from 2021. The MSRP column signifies the corresponding
 
MSRP for the car make and model selected. User Found Price reflects the entered price for the car from the user. The Good Deal column represents if the entered price reflects a good deal compared to the vehicles MSRP.
IV. Limitations of the Application
For the most part this application is primitive and limited by the nature of the assignment. The MSRP data only includes vehicles that were produced in 2021. Furthermore, the dataset is limited to only 452 various makes and models. The data was originally gathered in November 2021 which leaves the possibility that some of the application MSRP prices do not accurately reflect the vehicles current MSRP price. Finally, this application is intended to be a tool that assists in the car buying process, but it is not the quintessential element. It is always recommended that one does appropriate outside research before buying a car.
V. What’s Included
The submitted zip file contains this word document and the program package. Within the program package are the following files:
1. main.py – essential
2. ascii_logo.txt – essential
3. msrp_data.csv – essential
4. main_record.csv – nonessential, if not included the program will automatically generate
this file.
VI. First Time Use
Welcome to the Car Price Navigator Application. Before running the application, please ensure that the project has all three of the essential files listed above. Upon starting the application, you will be presented the GUI shown below:
(Note this image is from MacOS, running on any other operating system will result in some graphical changes but the functionality is the same)
VII. In Depth User Guide
 
 Feature # 1:
This is the car make and model that you would like to analyze. The combo box allows for you to type an input or select a drop-down option. This field is required. It should be noted that the entry is case sensitive and all entries are treated as strings. If an analysis is run and the entered make and model is not currently supported, a message box will be created to inform you.
Feature # 2:
This is the price listed for the car found. This entry box is required and only accepts positive integers or float values. If you enter a non-integer/float data type or a negative value, a message box is created to inform you of the error.
Feature # 3 (Optional):
This is the person or place where you found the car for sale. This entry box is optional and all entered values are treated as strings. If this field is left blank, the application will write “No seller entered” into the corresponding seller column on “main_record.csv”.
Feature # 4:
This button will run the analysis on the inputted entries. The corresponding output will be one of three message boxes. The first is an informational box telling you the result of the analysis. The second is an error message informing you that only positive integers/floats are accepted in the price field. The third is an error message informing you that the entered car make and model is not currently supported.
    
Congratulations you just worked through the main feature of the application. The following two features on the application are completely optional and solely serve as quality-of-life features for the user.
Feature # 5:
This feature allows you to select through a variety of additional options. The default option is the view records option. When selected this opens a new window that contains a preview of the “main_record.csv”. This feature serves as a handy way for users to check on their inputs in the middle of a session. The second feature is a clear records option. When selected this option will clear “main_record.csv” leaving just the corresponding headers. This serves as a great quality of life feature for users to be able to quickly erase their inputs and start over. The last option is a close application option. As the name suggests this option will terminate the application.
Feature # 6:
This feature serves as the button to activate the selected option from the option menu. Nothing too fancy here.
VIII. Example Output
Here are the filled-out entries:
   
The corresponding response:
And finally, when selecting View Records:
(The bottom row is from the example entries provided. The other rows were generated beforehand for display purposes.)
IX. References
Here is the link to the dataset:
https://www.kaggle.com/datasets/lauracw/cars-msrp?resource=download
This helped me create and write the additional pop-up window with the csv data:
https://stackoverflow.com/questions/71034460/display-csv-with-tkinter
Link to the ASCII art done by David Palmer:
https://www.asciiart.eu/vehicles/cars
     
