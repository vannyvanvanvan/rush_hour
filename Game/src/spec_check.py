import platform
import psutil

def get_system_specs() -> dict[str, str]:
    specs = {}
    
    # Checking CPU Information
    specs["CPU"] = platform.processor()
    specs["Cores"] = str(psutil.cpu_count(logical=False))
    specs["Threads"] = str(psutil.cpu_count(logical=True))
    
    # Ram
    mem = psutil.virtual_memory()
    specs["RAM"] = f"{round(mem.total / (1024**3), 1)} GB"

    return specs

def wrap_text(text, font, max_width):
    words = text.split()
    lines = []
    current_line = []
    for word in words:
        test_line = ' '.join(current_line + [word])
        width, _ = font.size(test_line)
        if width <= max_width:
            current_line.append(word)
        else:
            lines.append(' '.join(current_line))
            current_line = [word]
    lines.append(' '.join(current_line))
    return lines

if __name__ == "__main__":
    print(get_system_specs())