import re


def extract_replacements(input_string):
    # 正規表現パターンの定義
    pattern = re.compile(r"「(.*?)」(?:->|→)「(.*?)」")
    # マッチするすべてのペアをリストに抽出
    replacements = pattern.findall(input_string)
    return replacements


input_string = """
「現存の記録の中で最古の人体解剖を行った人物。ヒポクラテスに影響を与えた。」→「現存の記録の中で最古の人体解剖を行った人物であり、ヒポクラテスに影響を与えた。」
「の捉え方はで捉え方のレベルが異なっていて、」→「の捉え方はレベルが異なっていて、」

"""

rep_list = extract_replacements(input_string)
print(rep_list)
