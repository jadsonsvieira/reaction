import os
from PIL import Image

STATIC_DIR = r"C:\Users\jadso\Projetos\reaction\static"
MASTER_ICON = os.path.join(STATIC_DIR, "app_icon.png")

def generate_all_icons():
    print("Gerando todos os ícones PWA e Favicons a partir de static/app_icon.png...")
    
    if not os.path.exists(MASTER_ICON):
        print(f"Erro: {MASTER_ICON} não encontrado!")
        return

    master_img = Image.open(MASTER_ICON).convert("RGBA")

    # 512x512 PNG (PWA / Windows Desktop / Android)
    img_512 = master_img.resize((512, 512), Image.Resampling.LANCZOS)
    img_512.save(os.path.join(STATIC_DIR, "icon-512.png"), format="PNG")
    print(" -> Gerado: static/icon-512.png (512x512)")

    # 192x192 PNG (PWA / Android Launcher)
    img_192 = master_img.resize((192, 192), Image.Resampling.LANCZOS)
    img_192.save(os.path.join(STATIC_DIR, "icon-192.png"), format="PNG")
    print(" -> Gerado: static/icon-192.png (192x192)")

    # 180x180 PNG (Apple Touch Icon)
    img_180 = master_img.resize((180, 180), Image.Resampling.LANCZOS)
    img_180.save(os.path.join(STATIC_DIR, "apple-touch-icon.png"), format="PNG")
    print(" -> Gerado: static/apple-touch-icon.png (180x180)")

    # 64x64 PNG (Favicon PNG)
    img_64 = master_img.resize((64, 64), Image.Resampling.LANCZOS)
    img_64.save(os.path.join(STATIC_DIR, "favicon.png"), format="PNG")
    print(" -> Gerado: static/favicon.png (64x64)")

    # Favicon.ico multi-resolução
    ico_sizes = [(256, 256), (128, 128), (64, 64), (48, 48), (32, 32), (16, 16)]
    master_img.save(
        os.path.join(STATIC_DIR, "favicon.ico"),
        format="ICO",
        sizes=ico_sizes
    )
    print(" -> Gerado: static/favicon.ico")

    print("\n[SUCESSO PERFEITO] Todos os ícones PWA e atalhos de aplicativo foram atualizados!")

if __name__ == '__main__':
    generate_all_icons()
