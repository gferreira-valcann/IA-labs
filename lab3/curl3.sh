OLDDIR=$(pwd)
cd /home/gabriel-valcann/strands/lab3

IMG_BASE64=$(base64 -w 0 img1.png)

curl -X POST \
  -H "Content-Type: multipart/form-data" \
  -F "file=@./img1.png" \
  http://localhost:8080/invocations

cd "$OLDDIR"

