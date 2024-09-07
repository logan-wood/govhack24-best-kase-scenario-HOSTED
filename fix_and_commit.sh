echo "grabbing updates..." 
git pull
echo "checking in updates..."
git add .
git commit
echo "pushing updates back to github..."
git push
