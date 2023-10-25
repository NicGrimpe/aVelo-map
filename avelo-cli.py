import click

from avelo.avelo import AVelo
from avelo.trajets_extraction import fetch_for_year
from avelo.stations import Stations

@click.group()
@click.option('--avelo_token', envvar='AVELO_TOKEN')
@click.pass_context
def cli(ctx, avelo_token):
    ctx.obj = AVelo(avelo_token)

@cli.command()
@click.pass_obj
def extract(avelo: AVelo):
    avelo_stations = Stations()
    trajets = fetch_for_year(avelo, 2023)
    for t in trajets:
        t.add_coordinates(avelo_stations.stations)
        print(t)

if __name__ == '__main__':
    cli()