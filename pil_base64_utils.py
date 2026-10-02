from PIL import Image
import base64
from io import BytesIO

def open_image_as_base64(file) -> str:
    '''
    Parameters:
        file (str): 
            file path.

    Return:
        base64 format string.
    '''
    with open(file, 'rb') as f:
        data = base64.b64encode(f.read()).decode('utf-8')
    return data

def base64_to_pil(base64_str: str) -> Image.Image:
    '''
    Parameters:
        base64_str (str): 
            base64 format string.

    Return:
        PIL image object.
    '''
    img_bytes = base64.b64decode(base64_str)
    img = Image.open(BytesIO(img_bytes))
    return img

def pil_to_base64(image: Image.Image) -> str:
    '''
    Parameters:
        image (PIL.Image.Image): 
            PIL image object.

    Return:
        base64 format string.
    '''
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    img_bytes = buffered.getvalue()
    base64_str = base64.b64encode(img_bytes).decode('utf-8')
    return base64_str