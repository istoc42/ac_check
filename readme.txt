Instructions:

1. Create a folder in the same directory as the script and name it "output".
2. Put all PC asset numbers in the ip_list.txt file. One asset number per line.
3. Run the script. 
4. Enter your username and password for an account with admin priviliges (.a account) into the console.
5. When script is complete, you will have a csv file in the "output" folder with results of the search.

TODO: Output to Excel spreadsheet

1. Find library to open Excel spreadsheets.
2. Dump results into specific tab.
3. Conditional formatting / macro to check if a row has more than two consecutive entries of unreachable or dates older than 4 weeks. 

Change Log

- Tidy up of script timer in console. Returns minutes and seconds.
- Added file counter to end of script console message.
- Added date and time to filename to create a new file each time the script is run.
- Changed to ask for username and password before beginning.
