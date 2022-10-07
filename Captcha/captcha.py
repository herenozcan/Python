from captcha.image import ImageCaptcha

image = ImageCaptcha()

def generate_captcha(text):
    image.write(text, "captcha.png")

word = ""
generate_captcha(word)