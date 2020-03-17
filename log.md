# March 14

parse_csv.py now has 3 different functions

- parse_csv() is for csv files from Delver Lens and Deckbox.org depending on the flag that you own

- combine() is for when you have two files in the tcg format and you want to combine the quantities

- add_ones() is for files from cubecobra and it's a big list of card names with no quantities and adds a 1 in front of them so that it matches the TCG format

main.py has the filter function

- filter() takes the list of cards that you own in the TCG format and a list and then writes two files, cards that need to be bought and cards that you already own

