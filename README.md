I TASK 
Write a python script that creates an SQLite database according to the specified scheme. 
Primary key - text field weapon / ship / hull / engine respectively.

II TASK 
Create a script that will randomly fill values in the created database. The names: Ship-1, 
Ship-2, Weapon-1, etc. are quite suitable.  
The number of records for each table: 
  ships: 200 
  weapons: 20 
  hulls: 5 
  engines: 6 
  Value range for integer parameters: 1-20

III TASK 
Develop a session-scope fixture that gets the current state of the database and creates 
a temporary new database where the values are randomised: 
A. For each ship, one of the components is changed to a random one: hull, 
gun, or engine. 

IV TASK 
Implement automated tests that compare the data from the original database with the 
resulting randomized data: 
A. There should be three tests for each ship, checking its gun, hull and engine. 
B. The test should fall with assert: 
  B.1 When the value of a component parameter does not match its pre-randomizer. 
  B.2 When the gun, hull, or engine is changed. 
Output both the previous and current content.
