import markdown
import webbrowser
import tempfile

def open_md_in_browser(md_file_path='./README.md'):
    with open(md_file_path, 'r', encoding='utf-8') as f:
        md_text = f.read()

    html = markdown.markdown(md_text)

    with tempfile.NamedTemporaryFile('w', delete=False, suffix='.html', encoding='utf-8') as tmp:
        tmp.write(html)
        webbrowser.open(f'file://{tmp.name}')

