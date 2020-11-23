from mdutils.mdutils import MdUtils
from typing import List, Dict
import os

class TableItem:
    def __init__(self, id: str, title: str, difficulty: str, languages: List[str], tags: List[str]):
        self.id = id
        self.title = title
        self.difficulty = difficulty
        self.languages = languages
        self.tags = tags

def scan(mdFile: MdUtils):
    # scan python code
    cwd = os.getcwd()
    difficulties = [{'difficulty': element, 'path': os.path.join(cwd, element)} for element in ['easy', 'medium', 'hard']]
    difficulties = list(filter(lambda x: os.path.isdir(x['path']), difficulties))
    dict = {}
    for ele in difficulties:
        difficulty = ele['difficulty']
        path = ele['path']
        # modify dict in place
        scan_difficulty(path, difficulty, 'python', dict)

    # scan java code
    difficulties = [{'difficulty': element, 'path': os.path.normpath(os.path.join(cwd, '../src/main/java',element))} for element in
                    ['easy', 'medium', 'hard']]
    difficulties = list(filter(lambda x: os.path.isdir(x['path']), difficulties))
    for ele in difficulties:
        difficulty = ele['difficulty']
        path = ele['path']
        # modify dict in place
        scan_difficulty(path, difficulty, 'java', dict)

    easy, medium, hard = groupby_orderby(dict)
    # write statistic
    write_statistic(mdFile, easy, medium, hard)

    # write table
    write_table(mdFile, easy, medium, hard)


def groupby_orderby(dict: Dict[str, TableItem]):
    easy = []
    medium = []
    hard = []

    for s in dict.values():
        if s.difficulty == 'easy':
            easy.append(s)
        elif s.difficulty == 'medium':
            medium.append(s)
        else:
            hard.append(s)
    # sort
    easy.sort(key=lambda x: x.id)
    medium.sort(key=lambda x: x.id)
    hard.sort(key=lambda x: x.id)

    return easy, medium, hard

def write_statistic(mdFile: MdUtils, easy, medium, hard):
    total = len(easy) + len(medium) + len(hard)
    mdFile.new_header(1, 'Statistic')

    list_of_strings = ["Difficulty", "Num", "Percentage"]
    list_of_strings.extend(["Easy", str(len(easy)), '{:.0f}'.format(len(easy)/total * 100) + '%'])
    list_of_strings.extend(["Medium", str(len(medium)), '{:.0f}'.format(len(medium) / total * 100) + '%'])
    list_of_strings.extend(["Hard", str(len(hard)), '{:.0f}'.format(len(hard) / total * 100) + '%'])
    mdFile.new_table(columns=3, rows=4, text=list_of_strings, text_align='right')
    mdFile.new_line(f'Total : {total}')

def write_table(mdFile: MdUtils, easy, medium, hard):
    mdFile.new_header(1, 'Solutions')
    mdFile.new_line()
    list_of_strings = ["Num", "Title", "Languages", "Difficulty", "Tags"]

    result = []
    result.extend(easy)
    result.extend(medium)
    result.extend(hard)

    for ele in result:
        list_of_strings.extend(
            [ele.id, ele.title if len(ele.title) > 0 else ' ', ', '.join(ele.languages), ele.difficulty,
             ', '.join(ele.tags)])

    mdFile.new_table(columns=5, rows=len(result) + 1, text=list_of_strings)

def scan_difficulty(path: str, difficulty: str, language: str, dict: Dict[str, TableItem]) -> Dict[str, TableItem]:
    solutions = [f for f in os.scandir(path) if f.is_dir() and f.name != '__pycache__']
    for solution in solutions:
        table_item = parse_folder(solution, difficulty, language)
        id = table_item.id

        if id not in dict:
            dict[id] = table_item
        else:
            # append language id the same id found
            dict[id].languages.append(language)

    return dict

def parse_folder(f, difficulty: str, language: str) -> TableItem:
    name = f.name
    # extract id
    end = name.find('_', 1)
    id = name[1:end] if end > 0 else name[1:len(name)]
    # extract name
    title = name[end + 1: len(name)].replace('_', ' ') if end > 0 else ''

    # extract tag
    tags = []
    source_code = os.path.join(f, 'solution.py')
    if os.path.isfile(source_code):
        with open(source_code) as file:
            first_line = file.readline()
            mark = "# tags:"
            if mark in first_line:
                tag_str = first_line.replace(mark, "").strip()
                tags.extend(tag_str.split(','))

    return TableItem(id, title, difficulty, [language], tags)


def create_readme():
    mdFile = MdUtils(file_name='README.md', title='My leetcode solution collection')
    # create table
    scan(mdFile)
    # end create table
    mdFile.create_md_file()

if __name__ == '__main__':
    create_readme()