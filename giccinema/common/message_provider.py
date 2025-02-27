def show_message(text, color):

    colors = {
        "err": "\033[91m",  # Red
        "reset": "\033[0m"  # Reset to default
    }

    # Get the color code, default to reset if color is not found
    color_code = colors.get(color, colors["reset"])
    print(f"\n{color_code}{text}{colors['reset']}\n")
