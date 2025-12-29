#curl -X POST http://35.180.152.157:8080/invocations \
#!/bin/bash

IMG1=$(base64 -w0 img4.jpg)
IMG2=$(base64 -w0 img5.webp)

cat > payload.json <<EOF
{
  "prompt": "analise e descreva essas imagens",
  "images": [
    {
      "filename": "img4.jpg",
      "data": "$IMG1"
    },
    {
      "filename": "img5.webp",
      "data": "$IMG2"
    }
  ]
}
EOF

curl -X POST http://localhost:8080/invocations \
  -H "Content-Type: application/json" \
  --data-binary @payload.json
