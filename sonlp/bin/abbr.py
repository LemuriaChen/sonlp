#!/usr/bin/env python


from ..abbrev import Abbrev
import click


# 懂了，所以也就是说，option规定要带前缀的情况，而argument可以无需前缀
@click.command()
@click.option('--method', '-i', help='default to get abbreviation list of a given string, '
                                     'add -i to use full name pattern', nargs=0)
@click.argument('query', nargs=-1)
def wrapper(query, method):
    if not method:
        Abbrev().get_abbreviation(' '.join(query))
    else:
        Abbrev().get_fullname(' '.join(query))


wrapper()
