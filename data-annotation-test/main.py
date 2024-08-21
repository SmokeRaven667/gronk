
def get_rows(url):
    import requests 
    from bs4 import BeautifulSoup
    
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    rows = soup.table.find_all('tr')
    data = []
    for count, row in enumerate(rows):
        if count == 0:
            continue
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        row_data = [ele for ele in cols if ele]
        # append data in x, y, character order for readability
        data.append([int(row_data[0]), int(row_data[2]), row_data[1]])
    return data

def decode_secret():
    # url = 'https://docs.google.com/document/d/e/2PACX-1vRMx5YQlZNa3ra8dYYxmv-QIQ3YJe8tbI3kqcuC7lQiZm-CSEznKfN_HYNSpoXcZIV3Y_O3YoUB1ecq/pub'
    url = 'https://docs.google.com/document/d/e/2PACX-1vSHesOf9hv2sPOntssYrEdubmMQm8lwjfwv6NPjjmIRYs_FOYXtqrYgjh85jBUebK9swPXh_a5TJ5Kl/pub'
        
    # get row data from webpage
    coordinates = get_rows(url)

    # initialize grid for data output
    max_x = max(x for x, _, _ in coordinates)
    max_y = max(y for _, y, _ in coordinates)
    grid = [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]
    print(grid)

    # populate grid
    for x, y, char in coordinates:
        grid[y][x] = char

    # create and display grid
    for row in reversed(grid):
        print(''.join(row))

decode_secret()
