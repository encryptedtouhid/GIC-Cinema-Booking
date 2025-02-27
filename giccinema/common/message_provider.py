def show_message(text, color):

    colors = {
        "failed": "\033[91m",  # Red
        "success": "\033[92m",  # Green
        "warning": "\033[93m",  # Yellow
        "reset": "\033[0m"  # Reset to default
    }

    # Get the color code, default to reset if color is not found
    color_code = colors.get(color, colors["reset"])
    print(f"\n{color_code}{text}{colors['reset']}\n")
