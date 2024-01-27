pdf_dir="./data"
tika_jar="./tika-app-2.9.1.jar"


# Iterate over each PDF file in the directory
for pdf_file in "$pdf_dir"/*.pdf; do
  # Check if the file is a regular file

  txt_file="${pdf_file%.pdf}.txt"

  if [ -f "$pdf_file" ]; then
    echo "Processing: $pdf_file",  "$txt_file"

    # Run Apache Tika to extract text content from the PDF file
    java -jar "$tika_jar" -t "$pdf_file" > "$txt_file"

    echo "------------------------------------------"
  fi
done
