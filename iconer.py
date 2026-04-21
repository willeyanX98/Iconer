import os
import glob
from PIL import Image

def create_ico(input_image_path):
    if not os.path.exists(input_image_path):
        print(f"Error: File '{input_image_path}' not found.")
        return False

    file_name = os.path.splitext(input_image_path)[0]
    output_ico_path = f"{file_name}.ico"
    icon_sizes = [(256, 256), (128, 128), (64, 64), (48, 48), (32, 32), (16, 16)]
    
    try:
        with Image.open(input_image_path) as img:
            img = img.convert("RGBA")
            if img.width != img.height:
                size = max(img.size)
                new_img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
                new_img.paste(img, ((size - img.width) // 2, (size - img.height) // 2))
                img = new_img
            img.save(output_ico_path, format='ICO', sizes=icon_sizes)
            print(f"✔ Successfully converted: {output_ico_path}")
            return True
    except Exception as e:
        print(f"Error processing '{input_image_path}': {e}")
        return False

if __name__ == "__main__":
    # Define supported formats and find files at the start
    supported_formats = ['*.png', '*.jpg', '*.jpeg', '*.bmp', '*.webp']
    files = []
    for fmt in supported_formats:
        files.extend(glob.glob(fmt))
    
    print("--- Smart Icon Converter (Professional Edition) ---")
    print("Select an option:")
    print("1 - Convert a single image file")
    print("2 - Convert ALL images in this folder")
    
    choice = input("\nPlease enter your choice (1 or 2): ").strip()

    if choice == '2':
        if not files:
            print("No images found in this folder to convert!")
        else:
            print(f"Processing {len(files)} images...")
            for file in files:
                create_ico(file)
            print("\n--- Batch conversion completed successfully! ---")
            
    elif choice == '1':
        filename = input("Enter the image name with extension (e.g., image.png): ").strip().replace('"', '')
        create_ico(filename)
    else:
        print("Invalid choice. Please run the program again.")
    
    input("\nPress Enter to exit...")
