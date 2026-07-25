import os
from PIL import Image, ImageDraw

def draw_reaction_icon(size):
    # Supersampling 4x para renderização vetorial suave e sem serrilhado
    scale = 4
    s = size * scale
    img = Image.new('RGBA', (s, s), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Arredondamento exato de 28% (rounded-xl / App Icon iOS/Android)
    radius = int(s * 0.28)
    # Laranja Vibrante oficial da marca Reaction (#ff6b35)
    orange_color = (255, 107, 53, 255)
    
    # Desenhar fundo do app icon
    draw.rounded_rectangle([0, 0, s - 1, s - 1], radius=radius, fill=orange_color)
    
    cx, cy = s / 2, s / 2
    # Tamanho perfeitamente 1:1 e centralizado
    icon_size = s * 0.50
    half = icon_size / 2
    
    # Coordenadas proporcionais idênticas ao SVG Lucide shield-check (24x24 viewBox)
    def map_xy(x_24, y_24):
        # 12, 12 é o centro
        px = cx + (x_24 - 12) / 24.0 * icon_size
        py = cy + (y_24 - 12) / 24.0 * icon_size
        return (px, py)

    stroke_w = max(4, int(s * 0.068))
    white_color = (255, 255, 255, 255)
    
    # Pontos do Escudo Lucide: V5l-8-3-8 3v7c0 6 8 10 8 10z
    # p1 (12, 2), p2 (20, 5), p3 (20, 12), p4 (12, 22), p5 (4, 12), p6 (4, 5)
    p1 = map_xy(12, 2.5)
    p2 = map_xy(19.5, 5.2)
    p3 = map_xy(19.5, 12)
    p4 = map_xy(12, 21.5)
    p5 = map_xy(4.5, 12)
    p6 = map_xy(4.5, 5.2)
    
    shield_pts = [p1, p2, p3, p4, p5, p6, p1]
    
    # Desenhar o contorno do escudo com cantos arredondados
    for i in range(len(shield_pts) - 1):
        draw.line([shield_pts[i], shield_pts[i+1]], fill=white_color, width=stroke_w)
    
    r_cap = stroke_w / 2
    for p in shield_pts:
        draw.ellipse([p[0]-r_cap, p[1]-r_cap, p[0]+r_cap, p[1]+r_cap], fill=white_color)
    
    # Checkmark Lucide: M9 12l2 2 4-4
    chk1 = map_xy(8.8, 12.0)
    chk2 = map_xy(11.2, 14.5)
    chk3 = map_xy(15.5, 9.8)
    
    draw.line([chk1, chk2], fill=white_color, width=stroke_w)
    draw.line([chk2, chk3], fill=white_color, width=stroke_w)
    
    for p in [chk1, chk2, chk3]:
        draw.ellipse([p[0]-r_cap, p[1]-r_cap, p[0]+r_cap, p[1]+r_cap], fill=white_color)
        
    # Redimensionar com filtro LANCZOS para resolução final nítida
    img_final = img.resize((size, size), Image.Resampling.LANCZOS)
    return img_final

if __name__ == '__main__':
    os.makedirs("static", exist_ok=True)
    print("Gerando ícones PNG perfeitos da marca Reaction em proporção 1:1...")
    
    # 512x512 PNG
    img_512 = draw_reaction_icon(512)
    img_512.save("static/icon-512.png", "PNG")
    
    # 192x192 PNG
    img_192 = draw_reaction_icon(192)
    img_192.save("static/icon-192.png", "PNG")
    
    # 180x180 Apple Touch Icon
    img_180 = draw_reaction_icon(180)
    img_180.save("static/apple-touch-icon.png", "PNG")
    
    # 64x64 Favicon PNG
    img_64 = draw_reaction_icon(64)
    img_64.save("static/favicon.png", "PNG")
    
    # Favicon ICO
    img_64.save("static/favicon.ico", format="ICO", sizes=[(64, 64), (32, 32), (16, 16)])
    
    print("Ícones PWA redesenhados com sucesso!")
