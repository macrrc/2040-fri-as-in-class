"""
User interaction & file I/O. Implement guards (validation) + try/except here.

Guidance:
- Prompt for input filename (reject empty; re-prompt).
- Read text with UTF-8; handle FileNotFoundError, PermissionError, UnicodeDecodeError.
- Prompt for output filename (default to 'output.txt').
- If output exists, confirm overwrite (y/n; re-prompt on invalid).
- Write lines; handle PermissionError/OSError.
- Never crash on user mistakes; re-prompt or exit gracefully with a helpful message.

Note:
- Keep function responsibilities small and names descriptive.
- No heavy text-processing logic belongs here.
"""

# TODO: define small helpers such as:
# def prompt_nonempty(prompt_text: str) -> str: ...
# def read_text_file(path: str) -> str: ...
# def confirm_overwrite(path: str) -> bool: ...
# def write_lines(path: str, lines: list[str]) -> bool: ...

def read_text_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file_in:
        return file_in.read()
    
def build_output_lines(text_stats_dict):
    return [
        f"Word count: {text_stats_dict["word_count"]}",
        f"Unique words: {text_stats_dict["unique_word_count"]}",
        f"Characters (with spaces): {text_stats_dict["characters_with_spaces"]}",
        f"Characters (no spaces): {text_stats_dict["characters_no_spaces"]}",
        f"Average word length: {text_stats_dict["average_word_length_str"]}",
        text_stats_dict["most_common_line"],
    ]

def output_text_stats_summary(text_stats_dict):
    output_lines = build_output_lines(text_stats_dict)
    
    # --- Print to console ---
    line_index = 0
    while line_index < len(output_lines):
        print(output_lines[line_index])
        line_index += 1

    # --- Write to output.txt ---
    with open("output.txt", "w", encoding="utf-8") as file_out:
        line_index = 0
        while line_index < len(output_lines):
            file_out.write(output_lines[line_index] + ("\n" if line_index < len(output_lines) - 1 else ""))
            line_index += 1