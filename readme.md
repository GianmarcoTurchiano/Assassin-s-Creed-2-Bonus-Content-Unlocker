# AC2's bonus content unlocker

This script automatically modifies the Assassin's Creed II save file in order to unlock the bonus contents. Please refer to [this](https://steamcommunity.com/sharedfiles/filedetails/?id=2841221628) thread for details.

## Warning

**This program comes with no warranty. Please read the instructions and backup your save files before using it.**

I did not personally test this script (I do not even own the game), I made it for a friend of mine.

## What does it do?

This script locates the smaller file between `1.save` and `2.save` in the save files directory and then sets some predefined bytes to 1. 

## Usage

1. Install [Python](https://www.python.org/).
2. Find the directory containing your save files.
3. **Backup the contents of this directory.**
4. Run the script.

```
python fippo.py save/files/directory
Successfully updated the save file.
The modified file is "save/files/directory/2.save".
```

If you are using cloud saving, add the `--cloud-save` argument.

```
python fippo.py save/files/directory --cloud-save
Successfully updated the save file.
The modified file has been saved as "save/files/directory/2.save.upload".
```

5. Restart your game.
