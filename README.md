PDF Image Compressor 📄✂️A lightweight Python utility to aggressively shrink PDF file sizes by re-encoding and downsampling embedded images.🚀 The ProblemStandard PDF "optimization" often just removes metadata or "deflates" text streams. If your PDF is "photo-heavy" (scans, high-res photos, or slide decks), these methods barely change the file size.✨ The SolutionThis script iterates through every page of a PDF, extracts the raw image data, and uses Pillow to:Downsample images that exceed a maximum dimension.Convert images to JPEG format.Compress images using a lossy quality factor (default 40%).Re-insert the compressed images back into the original PDF structure.🛠️ RequirementsYou will need Python 3.x and the following libraries:Bashpip install pymupdf pillow
💻 UsagePythonfrom compress import aggressive_shrink

# Parameters: input_path, output_path, max_dimension, quality
aggressive_shrink("large_input.pdf", "small_output.pdf", max_dimension=1200, quality=40)
⚙️ ConfigurationParameterDefaultDescriptionmax_dimension1200Resizes any image wider or taller than this (in pixels).quality40The JPEG compression quality (1-95). Lower = smaller file.
