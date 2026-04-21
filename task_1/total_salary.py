from pathlib import Path

def total_salary(path: str) -> tuple[int, float]:
    file_path = Path(path)

    if not file_path.is_absolute():
        file_path = Path(__file__).parent / file_path

    if not file_path.exists():
        return (0, 0)
    
    total = 0
        
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            developers_list = file.readlines()
        
        dev_number = len(developers_list)
        total = 0

        for dev in developers_list:
            _, salary = dev.strip().split(",")
            total +=int(salary)

        average = total / dev_number if dev_number > 0 else 0
                                 
        return (total, average)
    
    except Exception as e:
        print(e)
        return (0, 0)
    
total, average = total_salary("salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
