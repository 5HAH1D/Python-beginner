import requests
from bs4 import BeautifulSoup


def show_scores():
    list_of_dict = []
    url = 'https://www.espncricinfo.com/live-cricket-score'
    html_text = requests.get(url).content
    soup = BeautifulSoup(html_text, features='lxml')
    main_div = soup.find_all('div', class_='ds-text-compact-xxs')
    for tag in main_div:
        status = tag.find('span', class_='ds-text-tight-xs ds-font-bold ds-uppercase ds-leading-5')
        team1 = tag.find('p', class_='ds-text-tight-m ds-font-bold ds-capitalize ds-truncate')
        score_team1 = tag.find('strong', class_='')
        team2 = None if team1 is None else team1.find_next('p', class_='ds-text-tight-m ds-font-bold ds-capitalize ds-truncate')
        score_team2 = None if score_team1 is None else score_team1.find_next('strong', class_='')
        final_result = tag.find('p', class_='ds-text-tight-s ds-font-regular ds-truncate ds-text-typo-title')
        details = tag.find('div', class_='ds-text-tight-xs ds-truncate ds-text-ui-typo-mid')
        if status == 'Live':
            continue
        elif status.text.capitalize() == 'Result':
            sum_up = {'Status': status.text, 'Details': details.text, 'Team1': team1.text, 'Team2': team2.text, 'Score1': score_team1.text, 'Score2': score_team2.text, 'Result': final_result.text}
            list_of_dict.append(sum_up)
    return list_of_dict


if __name__ == '__main__':
    show = show_scores()
    for item in show:
        print(f"\nShowing {item['Status']} for {item['Details']}\n{item['Team1']}\t{item['Score1']}\n{item['Team2']}\t{item['Score2']}\n{item['Result']}\n")
