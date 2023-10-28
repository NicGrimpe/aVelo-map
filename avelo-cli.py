import click

from avelo.avelo import AVelo
from avelo.trajets_extraction import fetch_for_year
from avelo.stations import Stations
from avelo.map import generate_interractive_map

@click.group()
@click.option('--avelo_token', envvar='AVELO_TOKEN')
@click.pass_context
def cli(ctx, avelo_token):
    ctx.obj = AVelo(avelo_token)

@cli.command()
@click.option('--year', default=2023)
@click.pass_obj
def extract(avelo: AVelo, year):
    avelo_stations = Stations()
    trajets = fetch_for_year(avelo, year)
    for t in trajets:
        t.add_coordinates(avelo_stations.stations)
        print(t)

@cli.command()
@click.option('--year', default=2023)
@click.pass_obj
def generate_map(avelo: AVelo, year):
    avelo_stations = Stations()
    trajets = fetch_for_year(avelo, year)
    for t in trajets:
        t.add_coordinates(avelo_stations.stations)
    generate_interractive_map(trajets)


if __name__ == '__main__':
    cli()