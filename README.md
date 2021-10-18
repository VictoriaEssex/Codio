# Creating a contact book in codio
Algorithms are a set of instructions that can be understood by human beings and are executed by a computer, when trying to solve a problem (Bullinaria, 2019). Algorithms incorporate data structures to help a computer effectively perform a certain task. The following algorithm is implemented using python and represents the functionality of a contact book application. 

### Contact book application functionality
Please follow the set of instructions to engage with the provided interface design:
a) Add three new contacts using the following format: Name : Number 
b) Make sure your contacts have been arranged in alphabetical order.
c) Delete a contact.
d) Search for an existing contact.
e) Validate the application functionality through user engagement within the terminal.

### Installation
You can use Github to install the project on your local device. 
This can be done by cloning the repository using the 'git clone' command and entering into the terminal of your chosen IDE, followed by the project URL. 


### Running your application
You can run the application by making use of the run button in codio. 
If you are using an external integrated development environment (IDE), you can run your project in the programs local terminal.

### Problems
1. Please ensure you enter your new contact in the correct format or the code will break.
2. Please do not add a space before supplying an answer to an action or question in the terminal. 
3. Please make sure there are at least five contacts before trying to delete or search for a desired contact.

### Decision Tree
Please refer to the following decision tree, created in Miro. The decision tree provides a visual way for the user to understand the algorithym. 
Decision tree:
https://miro.com/welcomeonboard/T3ZZYlJjQ0o1cVZVcHpJMzdIYU9pU2pBMzV2MDZvTWFvZzlaNnh1UHhJRU9BWjhGQzV3dkVwUGJvbU93cVZua3wzMDc0NDU3MzQ3MzM1MDAzNTky?invite_link_id=867728473592

### Test Results
The codio terminal should output the following information (dependendent on the contact information the user supplies) if executed correctly. 

Greetings! 
Please make use of my contact book by completing the following steps: 
a) Add three new contacts using the following format: Name : Number 
b) Make sure your contacts have been arranged in alphebetical order.
c) Delete a contact.
d) Search for an existing contact.
['Victoria', 'Andrew']
['0849993016', '0849879074']
[]
Please enter a name and number of an individual to create a new contact.
Megan: 0846789876
['Victoria : 0849993016', 'Andrew : 0849879074', 'Megan: 0846789876']
Please enter a name and number of an individual to create a new contact.
Julian: 083267890
['Victoria : 0849993016', 'Andrew : 0849879074', 'Megan: 0846789876', 'Julian: 083267890']
Please enter a name and number of an individual to create a new contact.
Mark: 0768963456
['Victoria : 0849993016', 'Andrew : 0849879074', 'Megan: 0846789876', 'Julian: 083267890', 'Mark: 0768963456']
['Andrew : 0849879074', 'Julian: 083267890', 'Mark: 0768963456', 'Megan: 0846789876', 'Victoria : 0849993016']
Which contact do you want to delete? Victoria
Index to delete: 4
['Andrew : 0849879074', 'Julian: 083267890', 'Mark: 0768963456', 'Megan: 0846789876']
Search contact: Andrew
Andrew : 0849879074

The application was also tested using Jupyter notebook: https://banjo-gemini-3000.codio-box.uk/notebooks/Testing.ipynb

### Authors
Victoria Thompson 

### References
1. Bullinaria, J. (2019) Data Structures and Algorithms. Birmingham, UK: School of Computer Science University of Birmingham. Available from: https://www.cs.bham.ac.uk/~jxb/DSA/dsa.pdf  [Accessed 1 October 2021].
2. Downey, A. (2015) Think Python: How to Think Like a Computer Scientist. 2nd ed.Needham, Massachusetts: Green Tea Press. Available from: https://greenteapress.com/thinkpython2/thinkpython2.pdf [Accessed 14 October 2021].
3. Glenn Brookshear, J. &  Brylow, D. (2019) Computer Science: An Overview. 13th ed. United Kingdom: Pearson Education Limited. Available via the Vitalsource Bookshelf. [Accessed 1 October 2021].
4. Lamrini, B., IntechOpen. (2020) Contribution to Decision Tree Induction with Python: A Review. Web of ScienceTM Core Collection (BKCI): 1-22. DOI: http://dx.doi.org/10.5772/intechopen.92438
5. Xinogalos, S. (2013) ‘Using flowchart-based programming environments for simplifying programming and software engineering processes’, 2013 IEEE Global Engineering Education Conference (EDUCON).The Technical University of Berlin, 13-15 March 2013. Greece: University of Macedonia. 1313-1322.
 

