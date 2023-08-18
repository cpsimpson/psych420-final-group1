from shiny import ui


def render_recalled_words_from_stm(recalled_from_stm):
    o = []
    for memory in recalled_from_stm:
        original, recalled, strength = memory
        o.append(f"{'/'.join(recalled)}")

    return ", ".join(o)


def render_recalled_words_from_ltm(recalled_from_ltm):
    o = []
    for memory in recalled_from_ltm:
        # original, recalled, strength = memory
        o.append(f"{'/'.join(memory)}")

    return ", ".join(o)


def get_all_markdown(report_path):
    controls = []
    markdown_files = report_path.glob('*.md')
    for filename in markdown_files:
        with open(filename) as f:
            controls.append(ui.markdown(f.read()))

    return controls


def get_markdown(section, report_path):
    filename = report_path / f"{section}.md"
    with open(filename) as f:
        return ui.markdown(f.read())
