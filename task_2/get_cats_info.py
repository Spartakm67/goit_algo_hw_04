from pathlib import Path

def get_cats_info(path: str) -> list[dict[str, str]]:
    file_path = Path(path)

    if not file_path.is_absolute():
        file_path = Path(__file__).parent / file_path

    if not file_path.exists():
        print(f"File not found: {file_path}")
        return []
    
    cats_list = []
        
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for cat in file:
                cat_line = cat.strip()

                if not cat_line:
                    continue

                cat = cat_line.split(",")

                if len(cat) != 3:
                    print(f"Incorrect data format")
                    continue
                
                id, name, age = cat

                cats_list.append({
                    "id": id,
                    "name": name,
                    "age": age
                })

        return cats_list

    except Exception as e:
        print(e)
        return []
    
print(get_cats_info("cats_file.txt"))