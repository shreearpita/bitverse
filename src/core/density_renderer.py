
from pathlib import Path
import math

import numpy as np
from PIL import Image, ImageDraw, ImageFont


#configuration

BASE_DIR = Path(__file__).resolve().parents[2]

OUTPUT_DIR = BASE_DIR / "output"
FONT_PATH = BASE_DIR / "assets" / "DejaVuSansMono.ttf"

TILE_SIZE = 4
FONT_SIZE = 14

BACKGROUND = (0, 0, 0)
ONE_COLOR = (245, 245, 245)
ZERO_COLOR = (22, 22, 22)


#grayscale matric

def generate_density_matrix(image: Image.Image) -> np.ndarray:
    grayscale = image.convert("L")
    return np.asarray(grayscale, dtype=np.uint8)


#binary density

def generate_binary_density(
    gray_matrix: np.ndarray
) -> np.ndarray:

    height, width = gray_matrix.shape

    bayer_matrix = np.array([
        [0,  8,  2, 10],
        [12, 4, 14, 6],
        [3, 11, 1,  9],
        [15, 7, 13, 5]
    ], dtype=np.uint8)

    brightness_levels = np.rint(
        gray_matrix.astype(np.float32) / 255 * 16
    ).astype(np.uint8)

    binary_tiles = (
        bayer_matrix[None, None, :, :]
        < brightness_levels[:, :, None, None]
    )

    binary_art = (
        binary_tiles
        .transpose(0, 2, 1, 3)
        .reshape(
            height * TILE_SIZE,
            width * TILE_SIZE
        )
        .astype(np.uint8)
    )

    return binary_art


#binary matrix

def export_binary_matrix(
    binary_art: np.ndarray,
    output_path: Path
) -> None:

    binary_text = "\n".join(
        "".join(str(value) for value in row)
        for row in binary_art
    )

    output_path.write_text(
        binary_text,
        encoding="utf-8"
    )


#monospace font

def load_monospace_font() -> ImageFont.FreeTypeFont:

    if not FONT_PATH.exists():
        raise FileNotFoundError(
            f"Required font not found: {FONT_PATH}"
        )

    return ImageFont.truetype(
        str(FONT_PATH),
        FONT_SIZE
    )


#binary typography

def render_binary_art(
    binary_art: np.ndarray
) -> Image.Image:

    font = load_monospace_font()

    bbox = font.getbbox("0")

    char_advance = max(
        1.0,
        float(font.getlength("0"))
    )

    char_height = max(
        1,
        bbox[3] - bbox[1]
    )

    # Compensate for rectangular character proportions.
    horizontal_repeat = max(
        1,
        round(char_height / char_advance)
    )

    display_matrix = np.repeat(
        binary_art,
        horizontal_repeat,
        axis=1
    )

    height, width = display_matrix.shape

    canvas_width = math.ceil(width * char_advance)
    canvas_height = height * char_height

    canvas = Image.new(
        "RGB",
        (canvas_width, canvas_height),
        BACKGROUND
    )

    draw = ImageDraw.Draw(canvas)

    for y, row in enumerate(display_matrix):

        for x, value in enumerate(row):

            character = "1" if value == 1 else "0"

            color = (
                ONE_COLOR if value == 1
                else ZERO_COLOR
            )

            draw.text(
                (
                    round(x * char_advance),
                    y * char_height - bbox[1]
                ),
                character,
                font=font,
                fill=color
            )

    return canvas


#density artwork

def generate_density_artwork(
    image: Image.Image,
    output_name: str = "bitverse_output"
) -> Image.Image:

    OUTPUT_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    gray_matrix = generate_density_matrix(image)

    binary_art = generate_binary_density(gray_matrix)

    # Export binary matrix
    text_path = OUTPUT_DIR / f"{output_name}.txt"

    export_binary_matrix(
        binary_art,
        text_path
    )

    # Render typography
    canvas = render_binary_art(binary_art)

    image_path = OUTPUT_DIR / f"{output_name}.png"

    canvas.save(image_path)

    return canvas
