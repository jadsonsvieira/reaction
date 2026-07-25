import os
import resvg_py
from PIL import Image

SVG_PATH = r"C:\Users\jadso\Projetos\reaction\static\favicon.svg"

def convert_svg_to_png(svg_path, output_png_path, size):
    # Renderizar o SVG nativo com resvg_py em alta definição
    png_bytes = resvg_py.svg_to_bytes(svg_path=svg_path, width=size, height=size)
    
    with open(output_png_path, "wb") as out_f:
        out_f.write(png_bytes)
        
    print(f" -> Gerado: {output_png_path} ({size}x{size}px)")

def generate_all_icons():
    print("Gerando ícones PWA e Favicons 100% idênticos a partir de static/favicon.svg via resvg...")
    
    # 512x512 PNG (PWA / Windows Desktop / Android)
    convert_svg_to_png(SVG_PATH, r"C:\Users\jadso\Projetos\reaction\static\icon-512.png", 512)
    
    # 192x192 PNG (PWA / Android Launcher)
    convert_svg_to_png(SVG_PATH, r"C:\Users\jadso\Projetos\reaction\static\icon-192.png", 192)
    
    # 180x180 PNG (Apple Touch Icon)
    convert_svg_to_png(SVG_PATH, r"C:\Users\jadso\Projetos\reaction\static\apple-touch-icon.png", 180)
    
    # 64x64 PNG (Favicon PNG)
    convert_svg_to_png(SVG_PATH, r"C:\Users\jadso\Projetos\reaction\static\favicon.png", 64)
    
    # Favicon.ico
    img_64 = Image.open(r"C:\Users\jadso\Projetos\reaction\static\favicon.png")
    img_64.save(r"C:\Users\jadso\Projetos\reaction\static\favicon.ico", format="ICO", sizes=[(64, 64), (32, 32), (16, 16)])
    print(" -> Gerado: static/favicon.ico")
    
    # Atualizar também na pasta de versão v0.0.0 se existir
    dest_v0 = r"C:\Users\jadso\Projetos\reaction\versoes\reaction_v0.0.0\static"
    if os.path.exists(dest_v0):
        for fname in ["icon-512.png", "icon-192.png", "apple-touch-icon.png", "favicon.png", "favicon.ico"]:
            src = os.path.join(r"C:\Users\jadso\Projetos\reaction\static", fname)
            dst = os.path.join(dest_v0, fname)
            if os.path.exists(src):
                import shutil
                shutil.copy2(src, dst)
        print(" -> Copiado para a pasta versoes/reaction_v0.0.0/static")

    print("\n[SUCESSO PERFEITO] Todos os ícones PWA foram regerados com 100% de fidelidade ao SVG original!")

if __name__ == '__main__':
    generate_all_icons()
