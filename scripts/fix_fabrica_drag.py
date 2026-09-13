from pathlib import Path

p = Path('jogos/fabrica-de-pintinhos.html')
s = p.read_text(encoding='utf-8')

replacements = [
    (
        """    el.addEventListener('mousedown', (e) => startDrag(obj, e));
    el.addEventListener('touchstart', (e) => startDrag(obj, e), { passive: true });""",
        """    // Pointer Events unifica mouse, toque e caneta e evita perder o arraste.
    el.addEventListener('pointerdown', (e) => startDrag(obj, e));""",
    ),
    (
        """  function getPointFromEvent(e){
    const rect = fieldWrap.getBoundingClientRect();
    if (e.touches && e.touches.length > 0){
      return { x: e.touches[0].clientX - rect.left, y: e.touches[0].clientY - rect.top };
    }
    return { x: e.clientX - rect.left, y: e.clientY - rect.top };
  }""",
        """  function getPointFromEvent(e){
    const rect = fieldWrap.getBoundingClientRect();
    return { x: e.clientX - rect.left, y: e.clientY - rect.top };
  }""",
    ),
    (
        """  function startDrag(obj, e){
    if (!gameActive) return;
    const p = getPointFromEvent(e);
    dragState = { obj, offsetX: p.x - obj.x, offsetY: p.y - obj.y };
    obj.el.classList.add('dragging');
  }""",
        """  function startDrag(obj, e){
    if (!gameActive) return;
    if (e.button !== undefined && e.button !== 0) return;
    e.preventDefault();
    const p = getPointFromEvent(e);
    dragState = {
      obj,
      pointerId: e.pointerId,
      offsetX: p.x - obj.x,
      offsetY: p.y - obj.y
    };
    obj.el.classList.add('dragging');
    if (obj.el.setPointerCapture && e.pointerId != null){
      try { obj.el.setPointerCapture(e.pointerId); } catch (_) {}
    }
  }""",
    ),
    (
        """  function onMove(e){
    if (!dragState) return;
    const p = getPointFromEvent(e);
    const obj = dragState.obj;
    obj.x = p.x - dragState.offsetX;
    obj.y = p.y - dragState.offsetY;
    const size = parseFloat(obj.el.style.width);
    positionObj(obj, size);
  }""",
        """  function onMove(e){
    if (!dragState) return;
    if (dragState.pointerId != null && e.pointerId != null && e.pointerId !== dragState.pointerId) return;
    e.preventDefault();
    const p = getPointFromEvent(e);
    const obj = dragState.obj;
    const size = parseFloat(obj.el.style.width);
    const { w, h } = fieldSize();
    const half = size / 2;
    obj.x = Math.max(half, Math.min(w - half, p.x - dragState.offsetX));
    obj.y = Math.max(half, Math.min(h - half, p.y - dragState.offsetY));
    positionObj(obj, size);
  }""",
    ),
    (
        """  function onUp(){
    if (!dragState) return;
    const obj = dragState.obj;
    obj.el.classList.remove('dragging');""",
        """  function onUp(e){
    if (!dragState) return;
    if (dragState.pointerId != null && e && e.pointerId != null && e.pointerId !== dragState.pointerId) return;
    const obj = dragState.obj;
    obj.el.classList.remove('dragging');
    if (obj.el.releasePointerCapture && e && e.pointerId != null){
      try {
        if (!obj.el.hasPointerCapture || obj.el.hasPointerCapture(e.pointerId)) obj.el.releasePointerCapture(e.pointerId);
      } catch (_) {}
    }""",
    ),
    (
        """  fieldWrap.addEventListener('mousemove', onMove);
  window.addEventListener('mouseup', onUp);
  fieldWrap.addEventListener('touchmove', (e) => { onMove(e); }, { passive: true });
  window.addEventListener('touchend', onUp);""",
        """  window.addEventListener('pointermove', onMove, { passive: false });
  window.addEventListener('pointerup', onUp);
  window.addEventListener('pointercancel', onUp);""",
    ),
]

for old, new in replacements:
    if old not in s:
        raise SystemExit('Trecho esperado não encontrado; correção interrompida para não danificar o jogo.')
    s = s.replace(old, new, 1)

p.write_text(s, encoding='utf-8')
print('Fábrica de Pintinhos corrigida.')
