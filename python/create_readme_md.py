from mdutils.mdutils import MdUtils
from typing import List
import os

class TableItem:
    def __init__(self, id: int, title: str, difficulty: str, languages: List[str], tags: List[str]):
        self.id = id
        self.title = title
        self.difficulty = difficulty
        self.languages = languages
        self.tags = tags

def scan(mdFile: MdUtils):
    cwd = os.getcwd()
    difficulties = [{'difficulty': element, 'path': os.path.join(cwd, element)} for element in ['easy', 'medium', 'hard']]
    difficulties = list(filter(lambda x: os.path.isdir(x['path']), difficulties))
    result = []
    for ele in difficulties:
        difficulty = ele['difficulty']
        path = ele['path']
        table_items = scan_difficulty(path, difficulty)
        result.extend(table_items)

    mdFile.new_line()
    list_of_strings = ["Num", "Title", "Languages", "Difficulty", "Tags"]
    for ele in result:
        list_of_strings.extend([ele.id, ele.title, ', '.join(ele.languages), ele.difficulty, ', '.join(ele.tags)])

    mdFile.new_table(columns=5, rows=len(result) + 1, text=list_of_strings)

def scan_difficulty(path: str, difficulty: str) -> List[TableItem]:
    solutions = [f.name for f in os.scandir(path) if f.is_dir()]
    result = []
    for solution in solutions:
        # extract id
        end = solution.find('_', 1)
        id = solution[1:end]
        # extract name
        title = solution[end+1: len(solution)].replace('_', ' ')
        result.append(TableItem(id, title, difficulty, ['python'], []))

    return result


def create_readme():
    mdFile = MdUtils(file_name='README.md', title='My leetcode solution collection')
    # create table
    scan(mdFile)
    # end create table
    mdFile.create_md_file()

if __name__ == '__main__':

    create_readme()