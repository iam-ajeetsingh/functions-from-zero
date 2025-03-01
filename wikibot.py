import click
#import wikipedia
from mylib.bot import scrape


@click.command()
@click.option("--name", prompt = 'Wikipedia page to scrape', help="Web page we want to scrape")


#@click.option('length',help= 'length if the output from wikipedia')

def cli(name = "Microsoft"):
    result = scrape(name)
    click.echo(click.style(f"{result}:", bg ="blue", fg = "red"))

if __name__ == "__main__":
    cli()