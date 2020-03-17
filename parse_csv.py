
def parse_csv(parse_filename, output_filename, flag):
    '''
    If flag is lens:
        Parses csv output from app Delver Lens
        the csv is in format "Card Name", "Quantity"
            Ex: "Abandoned Sarcophagus","1"

    If flag is deckbox:
        Parses csv output from website deckbox.org, csv has to be pretreated to remove all columns except quantity and cardname
        the csv is in format Quantity, Card Name
            Ex: 1,Abandoned Sarcophagus
        If there is a comma in the card name, then the card name will be in quotations
            Ex: 1,"Nicol Bolas, God-Pharaoh"

    the output is in format Quantity Card Name, works for TCG
        Ex: 1 Abandoned Sarcophagus
    '''

    parse = open(parse_filename, 'r')
    output = open(output_filename, 'w')

    first_line = True

    if flag == 'lens':
        for line in parse:

            #the first line of the csv is the column names
            if first_line:
                first_line = False
                continue

            stripped = line.strip()

            # we can't split by just commas because some card names have commas
            card_start = line.find('"')
            card_end = line.find('"', card_start + 1)

            quantity_start = line.find('"', card_end + 1)
            quantity_end = line.find('"', quantity_start + 1)

            card = line[card_start+1:card_end]
            quantity = line[quantity_start+1:quantity_end]

            output.write(quantity + ' ' + card + '\n')

    elif flag == 'deckbox':
        for line in parse:

            #the first line of the csv is the column names
            if first_line:
                first_line = False
                continue

            stripped = line.strip()

            comma = stripped.find(',')
            quantity = stripped[:comma]

            #check if card name is surrounded by quotations
            if stripped[comma + 1] == '"':
                card = stripped[comma+2:-1]
            else:
                card = stripped[comma+1:]


            output.write(quantity + ' ' + card + '\n')
    else:
        print('Use flag deckbox or lens for input type')

    parse.close()
    output.close()


def combine(owned_filename, new_filename, output_filename):
    '''
    Combines two textfiles that I have generated in TCG format Quantity Card Name
        Ex: 1 Abandoned Sarcophagus

    Will detect whether there are repeats of cards and add to the quantity in owned.
    '''
    owned = open(owned_filename, 'r')
    new = open(new_filename, 'r')

    owned_dict = {}

    for line in owned:
        stripped = line.strip()
        space = stripped.find(' ')

        quantity = int(stripped[:space])
        card = stripped[space+1:]

        owned_dict[card] = quantity

    for line in new:
        stripped = line.strip()
        space = stripped.find(' ')

        quantity = int(stripped[:space])        
        card = stripped[space+1:]

        if card in owned_dict:
            owned_dict[card] += quantity
        else:
            owned_dict[card] = quantity

    owned.close()
    new.close()
    
    output = open(output_filename, 'w')

    #iterate through the owned dictionary
    for key in owned_dict:
        output.write(str(owned_dict[key]) + ' ' + key + '\n')


def add_ones(filename):
    '''
    Given a file from Cube Cobra with just card names
        Ex: Evolving Wilds
    Make it into a file that has a quantity of 1
        Ex: 1 Evolving Wilds
    '''

    f = open(filename, 'r')
    cards = []
    for line in f:
        stripped = line.strip()

        cards.append(stripped)

    f.close()

    f = open(filename, 'w')

    for card in cards:
        f.write('1 ' + card + '\n')



if __name__ == "__main__":
    #parse_csv('rares.csv', 'rares.txt', 'deckbox')

    #combine('mar14.txt', 'old_cube.txt', 'owned.txt')
    
    add_ones('new_cube.txt')