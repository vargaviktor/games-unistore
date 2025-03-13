echo "Creating list of jsons in entries folder and its subfolders."
find . -name 'game.json' -type f -exec ls -halF {} \; | cut -d"/" -f2- | sed 's/game.json//g' | sort > jsondirlist.txt