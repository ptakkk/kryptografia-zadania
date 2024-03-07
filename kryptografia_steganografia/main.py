from PIL import Image
from bitarray import bitarray


def text_to_bitarray(text):
    bits = bitarray()
    bits.frombytes(bytearray(text.encode()))
    return bits


def bitarray_to_text(bits):
    byte_array = bits.tobytes()
    text = byte_array.decode('utf-8')
    return text


def encode_text(image, bits):
    if len(bits) > (image.width * image.height * 3) + 8:   # number of pixel in image *channels in RGB + length info
        print("za dlugi bitarray")
        return

    bits = value_to_bitarray(len(bits)) + bits
    bits.reverse()
    for y in range(image.height):
        for x in range(image.width):
            pixel = list(image.getpixel((x, y)))

            if pixel[3] != 0:  # check for alpha val
                for i in range(3):  # loop for 3 RGB channels
                    if bits:
                        bit_to_insert = bits.pop()  # remove last bit
                        pixel_bit = value_to_bitarray(pixel[i])
                        new_pixel = modify_pixel_bit(pixel_bit, bit_to_insert)
                        pixel[i] = new_pixel

                image.putpixel((x, y), tuple(pixel))

            if not bits:
                return


def value_to_bitarray(value):
    return bitarray(bin(value)[2:].zfill(8))


def modify_pixel_bit(pixel_bit, bit):
    pixel_bit[-1] = bit
    value = int(pixel_bit.to01(), 2)
    return value


def get_bits_from_image(image):
    bits = bitarray()
    length = bitarray()
    msg_len = -1
    for y in range(image.height):
        for x in range(image.width):
            pixel = image.getpixel((x, y))

            if pixel[3] != 0:
                for i in range(3):
                    if msg_len == -1:
                        length.append(value_to_bitarray(pixel[i])[-1])
                        if len(length) == 8:
                            msg_len = int(length.to01(), 2)  # if 8bits then convert to byte integer
                    else:
                        bits.append(value_to_bitarray(pixel[i])[-1])
                        if len(bits) == msg_len:
                            return bits



if __name__ == '__main__':
    text = "dupa dupa"

    image = Image.open('not_white.png')
    text_bits = text_to_bitarray(text)
    encode_text(image, text_bits)

    image.save('img_new.png')
    new_image = Image.open('img_new.png')

    read_bits = get_bits_from_image(new_image)
    new_text = bitarray_to_text(read_bits)

    if text == new_text:
        print("git")
    else:
        print("nie git")
