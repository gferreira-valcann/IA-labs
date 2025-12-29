
curl -X POST http://localhost:8080/invocations \
-H "Content-Type: application/json" \
-d '{"prompt": "em qual diretorio vc esta? analise as imagens em /home/gabriel-valcann/strands/lab3/img1.png /home/gabriel-valcann/strands/lab3/img2.png /home/gabriel-valcann/strands/lab3/img3.webp"}'
# -d '{"prompt": "analise e descreva as imagens presentes em img1.png img2.png e img3.webp"}'