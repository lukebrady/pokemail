import smtplib, ssl


# send_pokemon sends a random pokemon to the list of subscribers.
def send_pokemon(pokemon, users):
    # Create the SMTP client that will send pokemail.
