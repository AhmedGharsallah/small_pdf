import fitz  # PyMuPDF
from PIL import Image
import io

def aggressive_shrink(input_path, output_path, max_dimension=1200, quality=40):
    doc = fitz.open(input_path)
    
    for page in doc:
        image_list = page.get_images(full=True)
        
        for img in image_list:
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            
            img_obj = Image.open(io.BytesIO(image_bytes))
            
            if max(img_obj.size) > max_dimension:
                img_obj.thumbnail((max_dimension, max_dimension), Image.Resampling.LANCZOS)
            

            byte_io = io.BytesIO()

            if img_obj.mode in ("RGBA", "P"):
                img_obj = img_obj.convert("RGB")
                
            img_obj.save(byte_io, format="JPEG", quality=quality, optimize=True)
            new_image_bytes = byte_io.getvalue()
            

            page.replace_image(xref, stream=new_image_bytes)


    doc.save(
        output_path,
        garbage=4,
        deflate=True,
        clean=True
    )
    doc.close()

aggressive_shrink("your_file.pdf", "shrunk_final.pdf")