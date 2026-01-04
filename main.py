from classes.Parser import Parser
from classes.URLBuilder import URLBuilder

import click

@click.command()
@click.option('--letter', default='A', help='Letter to get items for (A-Z)', show_default=True, type=click.Choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ'), show_choices=True)
@click.option('--type', default='penny', help='Item type to get', show_default=True, type=click.Choice(['penny', 'biljet']), show_choices=True)
@click.option('--page', help='Page to get', type=click.INT, prompt_required=False, show_choices=True, default=1, show_default=True)
@click.option('--single-page', help="Get items from single page only", is_flag=True, show_default=True)
def main(letter, type, page, single_page):
    if single_page:
        click.echo(f"Getting items from page {page}")
    else:
        click.echo(f"Getting items from page {page} and all following pages")
    parser = Parser(URLBuilder(type, letter, page).get_url())
    parser.parse_images()
    click.echo(f"Found {len(parser.get_image_elements())} images")
    print(parser.get_image_elements())

if __name__ == '__main__':
    main()
