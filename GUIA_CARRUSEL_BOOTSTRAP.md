# Guía de Implementación: Agregar Carrusel con Bootstrap al Proyecto Web

## Lista de Pasos de Implementación

### 1. **Preparación**
   - Incluir CDN de Bootstrap en el HTML
   - Agregar las dependencias necesarias (CSS y JavaScript de Bootstrap)
   - Preparar las imágenes para el carrusel

### 2. **Código HTML**
   - Crear la estructura del carrusel con Bootstrap
   - Agregar el contenedor principal con clase `.carousel`
   - Incluir las diapositivas (`.carousel-item`)
   - Implementar controles de navegación (anterior/siguiente)

### 3. **Código CSS**
   - Personalizar estilos del carrusel
   - Redimensionar imágenes del carrusel
   - Ajustar transiciones y animaciones

---

## CSS Específico para Redimensionar la Imagen del Carrusel

```css
/* CARRUSEL - REDIMENSIONAMIENTO DE IMAGEN */
.carousel-inner {
  max-width: 100%;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.2);
}

.carousel-item {
  height: 500px;
  position: relative;
}

.carousel-item img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: center;
}

/* Para pantallas medianas */
@media (max-width: 768px) {
  .carousel-item {
    height: 350px;
  }
}

/* Para pantallas pequeñas */
@media (max-width: 480px) {
  .carousel-item {
    height: 250px;
  }
}

/* Botones de control mejorados */
.carousel-control-prev,
.carousel-control-next {
  width: 50px;
  background: rgba(0, 0, 0, 0.5);
  border-radius: 50%;
  transition: all 0.3s ease;
}

.carousel-control-prev:hover,
.carousel-control-next:hover {
  background: rgba(0, 0, 0, 0.8);
  transform: scale(1.1);
}

/* Indicadores mejorados */
.carousel-indicators {
  position: absolute;
  bottom: 20px;
}

.carousel-indicators [data-bs-target] {
  width: 12px;
  height: 12px;
  border-radius: 50%;
  background-color: rgba(255, 255, 255, 0.5);
  transition: all 0.3s ease;
}

.carousel-indicators [data-bs-target].active {
  background-color: #fff;
  transform: scale(1.3);
}
```

---

## Ejemplo de Código HTML Completo

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Carrusel Bootstrap - Digital Assets Store</title>
  
  <!-- Bootstrap CSS -->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
  <link rel="stylesheet" href="/styles/common.css">
  <link rel="stylesheet" href="/styles/carrusel.css">
</head>
<body>
  <!-- Navbar -->
  <nav class="navbar">
    <div class="logo">💎 Digital Assets Store</div>
    <ul class="menu">
      <li><a href="/">Inicio</a></li>
      <li><a href="/productos">Productos</a></li>
      <li><a href="/contacto">Contacto</a></li>
      <li><a href="/nosotros">Nosotros</a></li>
    </ul>
  </nav>

  <!-- Carrusel Bootstrap -->
  <section class="container mt-5">
    <div id="carruselPrincipal" class="carousel slide" data-bs-ride="carousel">
      
      <!-- Indicadores -->
      <div class="carousel-indicators">
        <button type="button" data-bs-target="#carruselPrincipal" data-bs-slide-to="0" class="active" aria-current="true"></button>
        <button type="button" data-bs-target="#carruselPrincipal" data-bs-slide-to="1"></button>
        <button type="button" data-bs-target="#carruselPrincipal" data-bs-slide-to="2"></button>
      </div>

      <!-- Diapositivas -->
      <div class="carousel-inner">
        <div class="carousel-item active">
          <img src="/img/slide1.jpg" alt="Slide 1">
          <div class="carousel-caption">
            <h5>Diseño UX/UI Moderno</h5>
            <p>Crea experiencias visuales increíbles</p>
          </div>
        </div>
        <div class="carousel-item">
          <img src="/img/slide2.jpg" alt="Slide 2">
          <div class="carousel-caption">
            <h5>Desarrollo Web Profesional</h5>
            <p>Construye sitios web de clase mundial</p>
          </div>
        </div>
        <div class="carousel-item">
          <img src="/img/slide3.jpg" alt="Slide 3">
          <div class="carousel-caption">
            <h5>Marketing Digital Efectivo</h5>
            <p>Impulsa tu negocio al siguiente nivel</p>
          </div>
        </div>
      </div>

      <!-- Botones de Control -->
      <button class="carousel-control-prev" type="button" data-bs-target="#carruselPrincipal" data-bs-slide="prev">
        <span class="carousel-control-prev-icon"></span>
      </button>
      <button class="carousel-control-next" type="button" data-bs-target="#carruselPrincipal" data-bs-slide="next">
        <span class="carousel-control-next-icon"></span>
      </button>
    </div>
  </section>

  <!-- Footer -->
  <footer class="footer">
    <p>&copy; 2025 Digital Assets Store | Todos los derechos reservados.</p>
  </footer>

  <!-- Bootstrap JS -->
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
```

---

## Aspectos Esenciales de Bootstrap

### Los 4 Puntos Clave para que el Carrusel Funcione Correctamente

#### 1. **Inicialización**
- **¿Qué es?** Bootstrap necesita que inicialices el carrusel con sus estilos y funcionalidades.
- **Cómo implementarlo:**
  - Incluye el CDN de Bootstrap CSS en el `<head>`
  - Incluye el CDN de Bootstrap JS (Bundle) antes del cierre de `</body>`
  - El atributo `data-bs-ride="carousel"` activa la rotación automática
- **Código:**
  ```html
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
  ```

#### 2. **Contenedor Principal**
- **¿Qué es?** El div principal que envuelve todo el carrusel con identificador único.
- **Atributos importantes:**
  - `id="carruselPrincipal"` - Identificador único para referencia
  - `class="carousel slide"` - Clases Bootstrap requeridas
  - `data-bs-ride="carousel"` - Habilita rotación automática
- **Código:**
  ```html
  <div id="carruselPrincipal" class="carousel slide" data-bs-ride="carousel">
    <!-- Contenido del carrusel -->
  </div>
  ```

#### 3. **Diapositivas**
- **¿Qué es?** Cada imagen o contenido individual que se muestra en el carrusel.
- **Estructura requerida:**
  - `.carousel-inner` - Contenedor de todas las diapositivas
  - `.carousel-item` - Cada diapositiva individual
  - `.carousel-item.active` - La primera diapositiva visible
  - `<img>` - Imagen de la diapositiva
- **Código:**
  ```html
  <div class="carousel-inner">
    <div class="carousel-item active">
      <img src="imagen1.jpg" alt="Slide 1">
    </div>
    <div class="carousel-item">
      <img src="imagen2.jpg" alt="Slide 2">
    </div>
  </div>
  ```

#### 4. **Controles**
- **¿Qué es?** Los botones y indicadores que permiten navegar entre diapositivas.
- **Tipos de controles:**
  - **Indicadores:** Pequeños puntos que muestran la posición actual
  - **Botones Anterior/Siguiente:** Flechas para navegar manualmente
- **Código:**
  ```html
  <!-- Indicadores -->
  <div class="carousel-indicators">
    <button type="button" data-bs-target="#carruselPrincipal" data-bs-slide-to="0" class="active"></button>
    <button type="button" data-bs-target="#carruselPrincipal" data-bs-slide-to="1"></button>
  </div>

  <!-- Botones de Control -->
  <button class="carousel-control-prev" type="button" data-bs-target="#carruselPrincipal" data-bs-slide="prev">
    <span class="carousel-control-prev-icon"></span>
  </button>
  <button class="carousel-control-next" type="button" data-bs-target="#carruselPrincipal" data-bs-slide="next">
    <span class="carousel-control-next-icon"></span>
  </button>
  ```

---

## Checklist de Implementación

- [ ] CDN de Bootstrap CSS incluido en `<head>`
- [ ] CDN de Bootstrap JS (Bundle) incluido antes de `</body>`
- [ ] Contenedor principal con clase `.carousel` y `.slide`
- [ ] ID único asignado al contenedor
- [ ] `data-bs-ride="carousel"` presente en contenedor principal
- [ ] `.carousel-inner` envuelve todas las diapositivas
- [ ] Al menos una `.carousel-item` con clase `.active`
- [ ] Imágenes con ruta correcta y atributo `alt`
- [ ] Indicadores con `data-bs-target` y `data-bs-slide-to`
- [ ] Botones de control con `data-bs-slide="prev"` y `data-bs-slide="next"`
- [ ] CSS personalizado aplicado para redimensionamiento
- [ ] Responsive media queries configuradas

---

## Notas Importantes

- **Rotación automática:** Cambia `data-bs-ride="carousel"` a `data-bs-ride="false"` si deseas deshabilitarla
- **Velocidad de transición:** Personaliza con `data-bs-interval="5000"` (milisegundos)
- **Optimización de imágenes:** Usa imágenes comprimidas para mejor rendimiento
- **Accesibilidad:** Asegúrate de incluir atributos `alt` descriptivos en todas las imágenes

---

**Versión:** 1.0 | **Última actualización:** 12 de noviembre de 2025
