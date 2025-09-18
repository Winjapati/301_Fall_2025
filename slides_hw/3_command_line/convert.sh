# 1) Make a tiny Markdown source
echo "# Hello" > demo.md
echo "This is *italic* and **bold**." >> demo.md

# 2) Convert MD → HTML (plain text file you can open/read)
pandoc demo.md -o demo.html

# 3) Convert MD → DOCX and → ODT (packaged/binary-ish formats)
pandoc demo.md -o demo.docx
pandoc demo.md -o demo.odt

# 4) Compare what the OS thinks these are
file demo.html demo.docx demo.odt  # if 'file' is available
# Expect: demo.html = text/html; demo.docx/.odt = Zip archive data

# 5) Peek inside the DOCX/ODT packages (they're ZIPs!)
unzip -l demo.docx | head
unzip -l demo.odt  | head

# 6) Print the *actual* document XML stored inside
unzip -p demo.docx word/document.xml | head -n 20
unzip -p demo.odt  content.xml        | head -n 20

# 7) Show that HTML is directly readable text
head -n 20 demo.html

# 8) Use Pandoc to flatten all three to plain text
pandoc demo.html -t plain -o from_html.txt
pandoc demo.docx -t plain -o from_docx.txt
pandoc demo.odt  -t plain -o from_odt.txt

# 9) Compare sizes (packaged formats are typically larger)
ls -lh demo.* from_*.txt