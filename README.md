PDF Image Shrinker 📄✂️
A high-performance Python utility designed to aggressively reduce the size of "photo-heavy" PDFs. Unlike standard tools, this script re-encodes embedded images using lossy compression to achieve maximum space savings.
🚀 Why this exists
Standard optimization often fails because it only cleans up metadata. This tool dives into the PDF structure to:

Resize: Downscales massive images to a web-friendly resolution.

Compress: Re-encodes images as JPEGs with adjustable quality.

Clean: Removes orphaned objects and deflates data streams.

🛠️ Installation
Ensure you have Python installed, then run:
pip install pymupdf pillow
