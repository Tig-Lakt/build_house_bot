import openpyxl
from database.database import get_all_apps

from config import FILE_PATH


async def write_apps_to_excel(apps):
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    if apps: 
        sheet.append(list(apps[0].keys())) 

    for record in apps:
        sheet.append(list(record.values())) 

    try:
        workbook.save(FILE_PATH) 
        print(f"Данные успешно записаны в файл '{FILE_PATH}'.")
        return True
    except PermissionError:
        print(f"Ошибка: Не удалось сохранить файл '{FILE_PATH}'. Возможно, он открыт в другой программе.")
        return False
    
    
async def get_all_apps_file():
    all_apps = await get_all_apps()
    rec_to_file = await write_apps_to_excel(all_apps)
    if rec_to_file:
        return True
    return False
    