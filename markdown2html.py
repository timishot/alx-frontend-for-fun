import sys
import os

def convert_markdown_to_html(markdown_file, output_file):
    # Check if the Markdown file exists
    if not os.path.isfile(markdown_file):
        print(f"Missing {markdown_file}", file=sys.stderr)
        sys.exit(1)

    # Placeholder for the conversion logic (you can use a Markdown to HTML library here)
    # For demonstration purposes, let's assume we're just copying the content for now
    with open(markdown_file, 'r') as md_file:
        markdown_content = md_file.read()

    # Write the Markdown content to the output HTML file
    with open(output_file, 'w') as html_file:
        html_file.write(markdown_content)

    sys.exit(0)

if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py <MarkdownFile> <OutputFile>", file=sys.stderr)
        sys.exit(1)

    # Get the input Markdown file and output HTML file from command-line arguments
    input_md_file = sys.argv[1]
    output_html_file = sys.argv[2]

    # Call the function to convert Markdown to HTML
    convert_markdown_to_html(input_md_file, output_html_file)

