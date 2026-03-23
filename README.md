# Homebrew Hub GBA games database FORK

The purpose of this fork to convert the https://gbadev.org/ Homebrew database to the format of ".unistore".
In this format the Universal Updater can download the entries. 

# How to use?

Steps:
1. Update the repository on github (to add new items from the main, if there was an update), and pull it localy.
   1.1 "Sync fork" button > "Update branch" button
   1.2 On your PC: git pull
2. Run on Linux the 1_createlist.sh
   This creates the list of the directories of game.json files.
3. Run the gbxunistore.py with the command: 'python3 gbxunistore.py'
   This creates the .unistore JSON file, and also convert the first image to a PNG icon of every game.
   (Check the Python script's first line to have "gba" value set.) 
4. Copy the 'iconversion' directory to a Windows machine and run the '3_convert.cmd' script.
   This converts the PNG icons and the index list to a sprite sheet good for 3DS.
5. Copy the result gba.t3x file back to the repository root
6. Commit and pull   

## Download GBA database with QR code
1. Start Universal Updater on the 3DS
2. In the Universal Updater go to the Settings (Cogwheel) > Unistore selection.
3. Choose the New icon (+ in a circle) (last one)
4. Select either the QR icon (first) and scan the following QR code, or the keyboard icon (second) and enter the address: vargaviktor.hu/gba.unistore

![QR kód](gba_qrcoden.png)

## License

The *Homebrew Hub* project is licensed under the GPLv3 license. 

Each game, homebrew, demo and their related asset, file, screenshot or source code is released under different license terms and copyright holders. Please refer to the single entries for details.

If you are the copyright holder for any of the material hosted here, please open an Issue or email us at `hh a t gbdev.io`.
