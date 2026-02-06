<h1>PDF Image Shrinker 📄✂️</h1>

A high-performance Python utility designed to aggressively reduce the size of "photo-heavy" PDFs. Unlike standard tools, this script re-encodes embedded images using lossy compression to achieve maximum space savings.

<h3>🚀 Why this exists</h3>

Standard optimization often fails because it only cleans up metadata. This tool dives into the PDF structure to:

<b>Resize:</b> Downscales massive images to a web-friendly resolution.

<b>Compress:</b> Re-encodes images as JPEGs with adjustable quality.

<b>Clean:</b> Removes orphaned objects and deflates data streams.

<h3>🛠️ Installation</h3>
Ensure you have Python installed, then run:

    pip install pymupdf pillow
