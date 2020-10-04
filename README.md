# Hundo Leaderboard

This repository contains the github actions and static site hosting the Recipies @ Home project's leaderboard. For more information, see [this video](https://youtu.be/kpn30v5Y_YQ) by TASMalleo, or the main client's repository [here](https://github.com/SevenChords/CipesAtHome).

# Implementation

1. Use a github action to call a python script every hour.
2. That python script fetches the current table's information, formats it, and writes it out to a file. It also archives the previous file into the `historical` folder.
3. `loadData.js` reads the .json file and renders it out to a table. 
4. Github Pages hosts the site.

# TODO

1. Styling for the index page.
2. Load old historical data via query parameter.
3. Maybe some global stats?
4. Typescript support for the client side JS

# Special Thanks

* TASMalleo for doing the actual TASing that this project supports, as well as spearheading the overall project.
* Cubik, SevenChords, and Amphitryon for working on the client, without which this leadboard would be very empty.
* The TTYD speedrunning community for contributing their computing resources to this project.
* Speculative, for providing the inspiration for this method of caching historical data with their [hodllive project](https://github.com/Speculative/hodllive).

# Other links

* [Video explaining the project background](https://youtu.be/kpn30v5Y_YQ)
* [Client repository](https://github.com/SevenChords/CipesAtHome)
* [TTYD Discord, check the #hundo-tas-recipes channel](https://discord.gg/YB23azC)

# License

MIT License.