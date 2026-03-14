import os
import shutil
from deep_translator import GoogleTranslator

source_folder = "en"
target_folder = "es"

translator = GoogleTranslator(source='en', target='es')

# copiar carpeta
if not os.path.exists(target_folder):
    shutil.copytree(source_folder, target_folder)

for root, dirs, files in os.walk(target_folder):
    for file in files:
        if file.endswith(".html"):
            path = os.path.join(root, file)

            with open(path, "r", encoding="utf-8") as f:
                content = f.read()

            try:
                translated = translator.translate(content)

                with open(path, "w", encoding="utf-8") as f:
                    f.write(translated)

                print("Translated:", path)

            except Exception as e:
                print("Error:", path)
