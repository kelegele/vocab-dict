
import json

def convert_old_to_new(old_json_path, new_json_path):
    with open(old_json_path, 'r', encoding='utf-8') as old_file:
        old_data = [json.loads(line) for line in old_file]

    new_data = []

    for entry in old_data:
        new_entry = {
            "wordRank": entry.get("wordRank", 0),
            "word": entry.get("headWord", ""),
            "wordId": entry.get("content", {}).get("word", {}).get("wordId", ""),
            "content": {
                "usphone": entry.get("content", {}).get("word", {}).get("content", {}).get("usphone", ""),
                "usspeech": entry.get("content", {}).get("word", {}).get("content", {}).get("usspeech", ""),
                "ukphone": entry.get("content", {}).get("word", {}).get("content", {}).get("ukphone", ""),
                "ukspeech": entry.get("content", {}).get("word", {}).get("content", {}).get("ukspeech", ""),
                "sentences": entry.get("content", {}).get("word", {}).get("content", {}).get("sentence", {}).get("sentences", []),
                "trans": entry.get("content", {}).get("word", {}).get("content", {}).get("trans", []),
                "phrases": entry.get("content", {}).get("word", {}).get("content", {}).get("phrase", {}).get("phrases", [])
            },
            "bookId": entry.get("bookId", "")
        }
        new_data.append(new_entry)

    with open(new_json_path, 'w', encoding='utf-8') as new_file:
        json.dump(new_data, new_file, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    old_json_path = input("请输入旧格式JSON文件路径：")
    new_json_path = input("请输入转换后的新格式JSON文件路径：")

    convert_old_to_new(old_json_path, new_json_path)
    print("转换完成！")
