# Rudier Web

Sitio web simple para mostrar productos, contacto y nosotros.

## Estructura
- `index.html` - Página principal
- `productos.html`, `tienda.html` - Páginas de productos
- `contacto.html` - Formulario de contacto
- `nosotros.html` - Página de información
- `styles/` - CSS
- `img/` - Imágenes usadas en el sitio
- `api/` - Endpoints del backend (si aplica)

## Subir a GitHub
1. Inicializar repo local:

   ```powershell
   cd "C:\Users\A-01\Desktop\Rudier-web-main"
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   ```

2. Crear el repositorio remoto en GitHub: "rudier-web" (vía web o `gh repo create`).

3. Añadir remote y subir:

   ```powershell
   git remote add origin https://github.com/<TU_USUARIO>/rudier-web.git
   git push -u origin main
   ```

(Ver instrucciones detalladas para autenticación segura en el archivo `GUIA_CARRUSEL_BOOTSTRAP.md`).
