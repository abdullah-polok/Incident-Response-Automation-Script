from pyfiglet import Figlet
from rich.console import Console

console = Console()

# ASCII banner
fig = Figlet(font="ansi_shadow")  # you can try 'big', 'slant', 'rectangles'
ascii_banner = fig.renderText("Incident Response Automate Script")

# Print ASCII banner in neon green
console.print(ascii_banner, style="bold #00ff66")
