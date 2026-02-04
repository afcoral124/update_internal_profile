import os
import json

input_folder = "outputs"
output_file = "concatenado.json"

big_json = {}
errors = []


def print_json_error(filename, raw, error):
    lines = raw.splitlines()
    line = lines[error.lineno - 1] if error.lineno <= len(lines) else ""

    print("\n❌ ERROR DE SINTAXIS JSON")
    print(f"Archivo : {filename}")
    print(f"Línea   : {error.lineno}")
    print(f"Columna : {error.colno}")
    print(f"Mensaje : {error.msg}")
    print("\nContexto:")
    print(line)
    print(" " * (error.colno - 1) + "^")
    print()


for filename in sorted(os.listdir(input_folder)):
    file_path = os.path.join(input_folder, filename)

    if not (os.path.isfile(file_path) and filename.endswith(".json")):
        continue

    with open(file_path, "r", encoding="utf-8") as infile:
        raw = infile.read()

    try:
        data = json.loads(raw)

        if not isinstance(data, dict):
            raise ValueError("El JSON raíz no es un objeto")

        # Avisar si hay colisión de claves
        for key in data:
            if key in big_json:
                print(f"⚠️ Clave duplicada '{key}' en {filename} (sobrescribiendo)")

        big_json.update(data)
        print(f"✅ {filename} procesado correctamente")

    except (json.JSONDecodeError, ValueError) as e:
        print_json_error(filename, raw, e)
        errors.append(filename)
        continue


with open(output_file, "w", encoding="utf-8") as outfile:
    json.dump(big_json, outfile, ensure_ascii=False, indent=2)


print("\n📦 Resultado final")
print(f"✔ Claves totales consolidadas: {len(big_json)}")
print(f"❌ Archivos con error: {len(errors)}")
if errors:
    for f in errors:
        print(f"   - {f}")

print(f"\n✅ JSON final guardado en '{output_file}'")
