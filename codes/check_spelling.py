import os

import openai
from dotenv import load_dotenv
from replace_sentences import extract_replacements

load_dotenv()
openai.api_key = os.getenv("OPENAPI_API_KEY")
openai.organization = os.getenv("OPENAPI_ORGANIZATION")


def use_gpt(text_from_terms: str) -> str:
    role_text = f"""
    あなたはプロの文章校訂者です。
次の文章の内容をチェックして不自然な表現や適切な表現があれば書き換えてください。。
書き換えは次のようにしてください。

#例
「女の働き方改革」→「女性の働き方改革」
「の捉え方はで捉え方のレベルが異なっていて、」→「の捉え方はレベルが異なっていて、」

#注意事項
- 「女の働き方改革」→「女性の働き方改革」 は必ず１行にして改行はしないでください。
- 修正箇所がない場合は、"nothing"と入力してください。
- 文章を冷静に読んで、すくなくとも３回は読んでから回答してください。
"""
    #     role_text = f"""
    #     あなたはプロの哲学研究者です。
    # 次の文章の内容をチェックして明らかな間違いがあれば指摘してください。
    # - エラーがない場合は、"nothing"と入力してください。
    # - 文中に疑問形があれば、それに答えてください。
    # - 文章を冷静に読んで、すくなくとも３回は読んでから回答してください。
    # """
    #     role_text = f"""
    #     あなたはプロの文章の校訂者です。
    # 次の文章の誤字脱字、スペルミスを修正してください。
    # - 説明は不要です。
    # - エラーがない場合は、"nothing"と入力してください。
    # - ミスの修正のみ行い、文章を追加や変更はしないでください。
    # """
    #     role_text = f"""
    # 次の文章の誤字脱字、スペルミスをおしえて
    # 例：mashine　→　machine

    # - Explanations are not necessary.
    # - if there is no error, please type "nothing".
    # """
    messages = [
        {"role": "system", "content": role_text},
        {"role": "user", "content": text_from_terms},
    ]
    try:
        response = openai.chat.completions.create(
            # model="gpt-3.5-turbo",
            model="gpt-4o",
            messages=messages,
            # temperature=1.0,
            temperature=0.8,
        )
        res = response.choices[0].message.content

        return res if res is not None and "nothing" not in res.lower() else "nothing"
    except Exception as e:
        print(e)
        return "over token limit"


def replace_and_copy_markdown_files(directory):
    counter = 0
    for root, _dirs, files in os.walk(directory):
        for i, file in enumerate(files):
            print(root, file)
            if file.endswith(".html"):
                file_path = os.path.join(root, file)
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()

                # parts = [content[i:i+5000] for i in range(0, len(content), 5000)]
                part = content
                # for j,part in enumerate(parts):
                updated_content = use_gpt(part)
                # print(12121,updated_content)

                print(counter, file)
                counter += 1
                # if updated_content == "over token limit":
                #     continue
                if updated_content == "nothing":
                    continue

                for txt1, txt2 in extract_replacements(updated_content):
                    updated_content = content.replace(txt1, txt2)

                # if "nothing" not in updated_content:
                # relative_path = os.path.relpath(root, directory)
                # output_file_path = os.path.join(output_dir, relative_path, file+str(j))
                # os.makedirs(os.path.dirname(output_file_path), exist_ok=True)
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(updated_content)
    print("Completed!!.")


if __name__ == "__main__":
    replace_and_copy_markdown_files("templates")
