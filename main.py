import click
from yt_dlp import YoutubeDL
from rich.console import Console

console = Console()

def parse_extra_args(args: tuple[str, ...]) -> dict:
    opts = {}
    i = 0
    while i < len(args):
        arg = args[i]
        if arg.startswith('--'):
            key = arg.lstrip('-').replace('-', '_')
            if i + 1 < len(args) and not args[i + 1].startswith('-'):
                opts[key] = args[i + 1]
                i += 1
            else:
                opts[key] = True
        i += 1
    return opts


@click.group(invoke_without_command=True)
@click.pass_context
def main(ctx):
    if ctx.invoked_subcommand is None:
        console.print("[bold green]Welcome to[/][bold cyan] Universal Downloader")
        console.print("[magenta]You can download video from YouTube, TikTok, Instagram, Pinterest and Reddit")
        console.print('[bold cyan]Use it with download {yt-dlp flags}')
        click.echo(ctx.get_help())

@main.command(
    'download',
    context_settings=dict(
        ignore_unknown_options=True,
        allow_extra_args=True
    )
)
@click.argument('url', required=True)
@click.pass_context
def download(ctx, url: str) -> None:
    try:
        # Вмикаємо режим 'quiet', щоб вимкнути дебаг та логи yt-dlp
        ydl_opts = {'quiet': True}
        extra_opts = parse_extra_args(ctx.args)
        ydl_opts.update(extra_opts)

        with console.status("[bold green]Downloading...", spinner='arrow3'):
            with YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])

        console.print("[bold green] Download finished!")
    except Exception as e:
        console.print(f"[bold red] ERROR! {e}")

if __name__ == '__main__':
  main()