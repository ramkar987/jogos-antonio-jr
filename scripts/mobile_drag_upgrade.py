#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def write_if_changed(path: Path, text: str) -> bool:
    old = path.read_text(encoding='utf-8', errors='replace') if path.exists() else None
    if old == text:
        return False
    path.write_text(text, encoding='utf-8')
    return True


def patch_mesa(text: str) -> str:
    text = text.replace(
        "  let dragging = false;\n  let dragTouchId = null;",
        "  let dragging = false;\n  let activePointerId = null;"
    )
    old = '''  function handlePointerDown(e){
    if (!gameActive) return;
    let clientX, clientY;
    if (e.type === 'touchstart'){
      const t = e.changedTouches[0];
      clientX = t.clientX; clientY = t.clientY;
      dragTouchId = t.identifier;
    } else {
      clientX = e.clientX; clientY = e.clientY;
    }
    const p = getSvgPoint(clientX, clientY);
    const dx = p.x - youMallet.x, dy = p.y - youMallet.y;
    if (Math.sqrt(dx*dx+dy*dy) < MALLET_R * 2.5){
      dragging = true;
    }
    e.preventDefault();
  }

  function handlePointerMove(e){
    if (!gameActive || !dragging) return;
    let clientX, clientY;
    if (e.type === 'touchmove'){
      let t = null;
      for (let i = 0; i < e.changedTouches.length; i++){
        if (e.changedTouches[i].identifier === dragTouchId){ t = e.changedTouches[i]; break; }
      }
      if (!t) t = e.changedTouches[0];
      if (!t) return;
      clientX = t.clientX; clientY = t.clientY;
    } else {
      clientX = e.clientX; clientY = e.clientY;
    }
    const p = getSvgPoint(clientX, clientY);
    youMallet.x = p.x;
    youMallet.y = p.y;
    clampMalletToHalf(youMallet);
    e.preventDefault();
  }

  function handlePointerUp(){
    dragging = false;
    dragTouchId = null;
  }

  tableWrap.addEventListener('mousedown', handlePointerDown);
  window.addEventListener('mousemove', handlePointerMove);
  window.addEventListener('mouseup', handlePointerUp);
  tableWrap.addEventListener('touchstart', handlePointerDown, { passive: false });
  window.addEventListener('touchmove', handlePointerMove, { passive: false });
  window.addEventListener('touchend', handlePointerUp);
  window.addEventListener('touchcancel', handlePointerUp);
'''
    new = '''  function handlePointerDown(e){
    if (!gameActive) return;
    if (e.pointerType === 'mouse' && e.button !== 0) return;
    const p = getSvgPoint(e.clientX, e.clientY);
    const dx = p.x - youMallet.x, dy = p.y - youMallet.y;
    if (Math.sqrt(dx*dx+dy*dy) < MALLET_R * 3){
      dragging = true;
      activePointerId = e.pointerId;
      try { tableWrap.setPointerCapture(e.pointerId); } catch (_) {}
      youMallet.x = p.x;
      youMallet.y = p.y;
      clampMalletToHalf(youMallet);
    }
    e.preventDefault();
  }

  function handlePointerMove(e){
    if (!gameActive || !dragging) return;
    if (activePointerId !== null && e.pointerId !== activePointerId) return;
    const p = getSvgPoint(e.clientX, e.clientY);
    youMallet.x = p.x;
    youMallet.y = p.y;
    clampMalletToHalf(youMallet);
    e.preventDefault();
  }

  function handlePointerUp(e){
    if (activePointerId !== null && e.pointerId !== activePointerId) return;
    if (activePointerId !== null){
      try { if (tableWrap.hasPointerCapture(activePointerId)) tableWrap.releasePointerCapture(activePointerId); } catch (_) {}
    }
    dragging = false;
    activePointerId = null;
  }

  tableWrap.addEventListener('pointerdown', handlePointerDown);
  tableWrap.addEventListener('pointermove', handlePointerMove);
  tableWrap.addEventListener('pointerup', handlePointerUp);
  tableWrap.addEventListener('pointercancel', handlePointerUp);
'''
    if old in text:
        text = text.replace(old, new, 1)
    return text


def patch_corta(text: str) -> str:
    text = text.replace(
        "  let pointerDown = false;",
        "  let pointerDown = false;\n  let activePointerId = null;"
    )
    old = '''  function handlePointerDown(e){
    if (!gameActive) return;
    pointerDown = true;
    const p = pointFromEvent(e);
    trailPoints.push({ x: p.x, y: p.y, t: performance.now() });
    checkSliceAt(p.x, p.y);
  }

  function handlePointerMove(e){
    if (!gameActive || !pointerDown) return;
    const p = pointFromEvent(e);
    trailPoints.push({ x: p.x, y: p.y, t: performance.now() });
    checkSliceAt(p.x, p.y);
  }

  function handlePointerUp(){
    pointerDown = false;
  }

  function pointFromEvent(e){
    if (e.touches && e.touches.length > 0){
      return getStageRelativePoint(e.touches[0].clientX, e.touches[0].clientY);
    }
    return getStageRelativePoint(e.clientX, e.clientY);
  }

  stageWrap.addEventListener('mousedown', handlePointerDown);
  stageWrap.addEventListener('mousemove', handlePointerMove);
  window.addEventListener('mouseup', handlePointerUp);

  stageWrap.addEventListener('touchstart', (e) => { handlePointerDown(e); e.preventDefault(); }, { passive: false });
  stageWrap.addEventListener('touchmove', (e) => { handlePointerMove(e); e.preventDefault(); }, { passive: false });
  stageWrap.addEventListener('touchend', handlePointerUp);
'''
    new = '''  function handlePointerDown(e){
    if (!gameActive) return;
    if (e.pointerType === 'mouse' && e.button !== 0) return;
    pointerDown = true;
    activePointerId = e.pointerId;
    try { stageWrap.setPointerCapture(e.pointerId); } catch (_) {}
    const p = getStageRelativePoint(e.clientX, e.clientY);
    trailPoints.push({ x: p.x, y: p.y, t: performance.now() });
    checkSliceAt(p.x, p.y);
    e.preventDefault();
  }

  function handlePointerMove(e){
    if (!gameActive || !pointerDown) return;
    if (activePointerId !== null && e.pointerId !== activePointerId) return;
    const p = getStageRelativePoint(e.clientX, e.clientY);
    trailPoints.push({ x: p.x, y: p.y, t: performance.now() });
    checkSliceAt(p.x, p.y);
    e.preventDefault();
  }

  function handlePointerUp(e){
    if (activePointerId !== null && e.pointerId !== activePointerId) return;
    if (activePointerId !== null){
      try { if (stageWrap.hasPointerCapture(activePointerId)) stageWrap.releasePointerCapture(activePointerId); } catch (_) {}
    }
    pointerDown = false;
    activePointerId = null;
  }

  stageWrap.addEventListener('pointerdown', handlePointerDown);
  stageWrap.addEventListener('pointermove', handlePointerMove);
  stageWrap.addEventListener('pointerup', handlePointerUp);
  stageWrap.addEventListener('pointercancel', handlePointerUp);
'''
    if old in text:
        text = text.replace(old, new, 1)
    return text


def patch_labirinto(text: str) -> str:
    text = text.replace(
        "  let dragging = false;",
        "  let dragging = false;\n  let activePointerId = null;",
        1
    )
    old = '''  function pointFromEvent(e){
    if (e.touches && e.touches.length > 0){
      return getSvgPoint(e.touches[0].clientX, e.touches[0].clientY);
    }
    return getSvgPoint(e.clientX, e.clientY);
  }

  function handleStart(e){
    if (!gameActive) return;
    const p = pointFromEvent(e);
    const dx = p.x - ballPos.x, dy = p.y - ballPos.y;
    if (Math.sqrt(dx*dx + dy*dy) < 8){
      dragging = true;
    }
  }

  function handleMove(e){
    if (!gameActive || !dragging) return;
    const p = pointFromEvent(e);

    if (checkWallCollision(p.x, p.y)){
      hitWall();
      return;
    }

    ballPos = p;
    drawMaze(false);

    if (checkGoalReached(p.x, p.y)){
      winLevel();
    }
  }

  function handleEnd(){
    dragging = false;
  }
'''
    new = '''  function moveBallSafely(p){
    const dx = p.x - ballPos.x, dy = p.y - ballPos.y;
    const dist = Math.hypot(dx, dy);
    const steps = Math.max(1, Math.ceil(dist / 1.1));
    for (let i = 1; i <= steps; i++){
      const x = ballPos.x + dx * (i / steps);
      const y = ballPos.y + dy * (i / steps);
      if (checkWallCollision(x, y)){
        hitWall();
        return false;
      }
    }
    ballPos = p;
    drawMaze(false);
    if (checkGoalReached(p.x, p.y)) winLevel();
    return true;
  }

  function handleStart(e){
    if (!gameActive) return;
    if (e.pointerType === 'mouse' && e.button !== 0) return;
    const p = getSvgPoint(e.clientX, e.clientY);
    const dx = p.x - ballPos.x, dy = p.y - ballPos.y;
    if (Math.sqrt(dx*dx + dy*dy) < 9){
      dragging = true;
      activePointerId = e.pointerId;
      try { mazeWrap.setPointerCapture(e.pointerId); } catch (_) {}
    }
    e.preventDefault();
  }

  function handleMove(e){
    if (!gameActive || !dragging) return;
    if (activePointerId !== null && e.pointerId !== activePointerId) return;
    moveBallSafely(getSvgPoint(e.clientX, e.clientY));
    e.preventDefault();
  }

  function handleEnd(e){
    if (activePointerId !== null && e.pointerId !== activePointerId) return;
    if (activePointerId !== null){
      try { if (mazeWrap.hasPointerCapture(activePointerId)) mazeWrap.releasePointerCapture(activePointerId); } catch (_) {}
    }
    dragging = false;
    activePointerId = null;
  }
'''
    if old in text:
        text = text.replace(old, new, 1)
    old_listeners = '''  mazeWrap.addEventListener('mousedown', handleStart);
  mazeWrap.addEventListener('mousemove', handleMove);
  window.addEventListener('mouseup', handleEnd);

  mazeWrap.addEventListener('touchstart', (e) => { handleStart(e); e.preventDefault(); }, { passive: false });
  mazeWrap.addEventListener('touchmove', (e) => { handleMove(e); e.preventDefault(); }, { passive: false });
  mazeWrap.addEventListener('touchend', handleEnd);
'''
    new_listeners = '''  mazeWrap.addEventListener('pointerdown', handleStart);
  mazeWrap.addEventListener('pointermove', handleMove);
  mazeWrap.addEventListener('pointerup', handleEnd);
  mazeWrap.addEventListener('pointercancel', handleEnd);
'''
    if old_listeners in text:
        text = text.replace(old_listeners, new_listeners, 1)
    return text


def patch_limpa(text: str) -> str:
    old = "ocean.addEventListener('pointermove',e=>{if(e.buttons||e.pointerType==='touch')moveFromPointer(e)});"
    new = "ocean.addEventListener('pointermove',e=>{if(!running||paused)return;if(e.pointerType==='mouse'&&e.buttons===0)return;moveFromPointer(e)});"
    return text.replace(old, new, 1)


PATCHERS = {
    'mesa-de-ar.html': patch_mesa,
    'corta-frutas.html': patch_corta,
    'labirinto-eletrico.html': patch_labirinto,
    'limpa-o-oceano.html': patch_limpa,
}


def patch_file(path: Path) -> bool:
    patcher = PATCHERS.get(path.name)
    if not patcher or not path.exists():
        return False
    text = path.read_text(encoding='utf-8', errors='replace')
    return write_if_changed(path, patcher(text))


def apply_current_repo():
    changed = []
    for name in PATCHERS:
        path = ROOT / 'jogos' / name
        if patch_file(path):
            changed.append(str(path.relative_to(ROOT)))
    return changed


if __name__ == '__main__':
    changed = apply_current_repo()
    print('Ajustados:', ', '.join(changed) if changed else 'nenhum')
