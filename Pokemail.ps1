# Written By Luke Brady
# Thanks to azai91 for the Pokemon name list!

# Read the list of Pokemon names and choose a random Pokemon.
$pokeList = Get-Content $PSScriptRoot\Configuration\pokemon_list.txt
$rand = Get-Random -Minimum 0 -Maximum $pokeList.Length

# Get the random pokemon that has been encountered.
$name = $pokeList[$rand]
$pokemon = $pokeList[$rand].ToLower()

# Now get the Pokemon's information from the PokeAPI.
$pokeInfo = Invoke-RestMethod -Method Get -Uri "https://pokeapi.co/api/v2/pokemon/$pokemon"

# Get the information needed to craft the email.
$sprite = $pokeInfo.sprites.front_default
$html =  '<h3>A wild ' + $name + ' has appeared.</h3><div id="poke" onclick="catchPokemon()"><img src= "'+$sprite+'"/></div>'

Send-MailMessage -BodyAsHtml -Body $html -From "pokemail@lukebrains.com" `
                            -To  -Subject "Something is rustling in the tall grass..." -SmtpServer "smtp.gmail.com"