from raparse.parse import parse_line, parse_text
from rautils.dictutils import find_integer_key
from ranet.network import get_wiktionary_content
from radb.db import maybe_create_table, upsert_item, set_db_path
import json
import click


@click.command()
@click.argument('db_location')
def main(db_location):
    # create db if it doesn't exist
    with open(db_location, 'w') as file:
        pass
    set_db_path(db_location)

    page_name = "Справка:Условные_сокращения"
    page_info = get_wiktionary_content(page_name)
    pages = page_info['query']['pages']

    # The pageid probably does not change but as a hedge against the bey
    # that it does not, we'll find the page id key by looking for the
    # one key that is an integer represented as a string
    page_id_key = find_integer_key(pages)
    content = pages[str(page_id_key)]['revisions'][0]['*']
    maybe_create_table()

    for p in parse_text(content.split('\n')):
        (idx, abbrev, expanded, category) = p
        upsert_item(idx, abbrev, expanded, category)


if __name__ == '__main__':
    main()

