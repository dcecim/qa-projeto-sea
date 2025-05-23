import requests
import json

# Substitua pelo token pessoal do Figma
FIGMA_TOKEN = 'YOUR_PERSONAL_ACCESS_TOKEN'
FILE_ID = 'gGePjuPTHdH7pISofjrzxB'
HEADERS = {
    'X-Figma-Token': FIGMA_TOKEN
}

def get_file_json(file_id):
    url = f'https://api.figma.com/v1/files/{file_id}'
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()
    return response.json()

def extract_elements(node, elements=[]):
    if 'name' in node and 'type' in node:
        elements.append({
            'name': node['name'],
            'type': node['type'],
            'visible': node.get('visible', True)
        })

    for child in node.get('children', []):
        extract_elements(child, elements)

    return elements

def main():
    print("Baixando estrutura do Figma...")
    file_json = get_file_json(FILE_ID)

    pages = file_json['document']['children']
    all_elements = []

    for page in pages:
        page_name = page['name']
        print(f"📄 Página: {page_name}")
        elements = extract_elements(page)
        for elem in elements:
            elem['page'] = page_name
        all_elements.extend(elements)

    with open('figma_elements_report.json', 'w', encoding='utf-8') as f:
        json.dump(all_elements, f, indent=2, ensure_ascii=False)

    print(f"✅ Extração completa. Total de elementos: {len(all_elements)}")
    print("Resultado salvo em figma_elements_report.json")

if __name__ == '__main__':
    main()
