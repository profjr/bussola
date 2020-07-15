graus = 0

def on_forever():
    global graus
    graus = input.compass_heading()
    if graus < 45:
        basic.show_string("N ")
    elif graus < 135:
        basic.show_string("L ")
    elif graus < 225:
        basic.show_string("S ")
    elif graus < 315:
        basic.show_string("O ")
        
basic.forever(on_forever)
