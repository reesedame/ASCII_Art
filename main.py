from PIL import Image

photo = Image.open("kitty.jpg")
ASCII_CHARS = '`^",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$'
MAX_B_VAL = 255


def get_rgb_data(img, height):
    img.thumbnail((height, 50))
    rgb_data = list(img.getdata())
    return rgb_data


def convert_rgb_to_brightness(rgb_data):
    brightness_data = []
    for i in range(len(rgb_data)):
        rgb_data[i] = (sum(rgb_data[i])) // 3
        brightness_data.append(rgb_data[i])
    return brightness_data


def invert_brightness(brightness_data):
    for i in range(len(brightness_data)):
        brightness_data[i] = 255 - brightness_data[i]
    return brightness_data


def convert_brightness_to_ASCII(brightness_data):
    ASCII_data = []
    for i in range(len(brightness_data)):
        ASCII_idx = int(((len(ASCII_CHARS) - 1) * brightness_data[i]) / MAX_B_VAL)
        brightness_data[i] = ASCII_CHARS[ASCII_idx]
        ASCII_data.append(brightness_data[i])
    return ASCII_data


def convert_to_2d_matrix(data):
    width, height = photo.size
    matrix = [data[i * width : (i + 1) * width] for i in range(height)]
    return matrix


def print_matrix(matrix):
    for row in matrix:
        print("".join(row))


rgb_data = get_rgb_data(photo, 240)
brightness_data = convert_rgb_to_brightness(rgb_data)
brightness_data = invert_brightness(brightness_data)
ASCII_data = convert_brightness_to_ASCII(brightness_data)
matrix = convert_to_2d_matrix(ASCII_data)
print_matrix(matrix)
