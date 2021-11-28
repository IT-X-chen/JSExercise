with open("background.png","wb")as f:
        f.write(background_data)
    image = Image.open('background.png')
    standard_img = Image.new("RGBA", (260, 160))
    position = [39, 38, 48, 49, 41, 40, 46, 47, 35, 34, 50, 51, 33, 32, 28, 29, 27, 26, 36, 37, 31, 30, 44, 45, 43,
                42, 12, 13, 23, 22, 14, 15, 21, 20, 8, 9, 25, 24, 6, 7, 3, 2, 0, 1, 11, 10, 4, 5, 19, 18, 16, 17]
    s, u = 80, 10
    for c in range(52):
        a = position[c] % 26 * 12 + 1
        b = s if position[c] > 25 else 0
        im = image.crop(box=(a, b, a + 10, b + 80))
        standard_img.paste(im, box=(c % 26 * 10, 80 if c > 25 else 0))
    standard_img.save("background.png")
    logger.info("图片保存成功！")